import fitbit
import configparser
import datetime

from datetime import datetime, date, timedelta
from pymongo import MongoClient

class Fitbit:

    def __init__(self):

        inifile = configparser.ConfigParser()
        inifile.read('./config.ini', 'UTF-8')

        self.client_id = inifile.get('fitbit', 'client_id')
        self.client_secret = inifile.get('fitbit', 'client_secret')
        self.access_token = inifile.get('fitbit', 'access_token')
        self.refresh_token = inifile.get('fitbit', 'refresh_token')

        self.authd_client = fitbit.Fitbit(self.client_id, self.client_secret, access_token=self.access_token, refresh_token=self.refresh_token)

    def get_heart_rate(self, date):
        data_sec = self.authd_client.intraday_time_series('activities/heart', "{0:%Y-%m-%d}".format(date), detail_level='1sec')
        heart_sec = data_sec["activities-heart-intraday"]["dataset"]
        return heart_sec

class MongoDB:

    def __init__(self):
        
        inifile = configparser.ConfigParser()
        inifile.read('./config.ini', 'UTF-8')

        self.host = inifile.get('mongodb', 'host')
        self.port = int(inifile.get('mongodb', 'port'))
        self.db = inifile.get('mongodb', 'db')
        self.collection = inifile.get('mongodb', 'collection')

        self.client = MongoClient(self.host, self.port)

    def insert_heart_rate(self, heart_rates, date):

        db = self.client[self.db]
        collection = db[self.collection + "{0:%Y-%m-%d}".format(date)]
        result = collection.insert_many(heart_rates) 

if __name__ == '__main__':

    # 前日の心拍数を取得
    fb = Fitbit()
    today = datetime.today()
    yesterday = today - timedelta(days = 1)
    heart_rates = fb.get_heart_rate(yesterday)
    print("Get heart rate.count:%d date: %s" % (len(heart_rates), "{0:%y-%m-%d}".format(yesterday)))

    # MongoDBに格納
    mongodb = MongoDB()
    mongodb.insert_heart_rate(heart_rates, yesterday)
    print("Insert MongoDB.")

    # Kafkaにメッセージ登録

