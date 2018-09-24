import fitbit
import configparser
import datetime

class Fitbit:

    def __init__(self):

        inifile = configparser.ConfigParser()
        inifile.read('./config.ini', 'UTF-8')

        self.client_id = inifile.get('fitbit', 'client_id')
        self.client_secret = inifile.get('fitbit', 'client_secret')
        self.access_token = inifile.get('fitbit', 'access_token')
        self.refresh_token = inifile.get('fitbit', 'refresh_token')

        self.authd_client = fitbit.Fitbit(client_id, client_secret, access_token=access_token, refresh_token=refresh_token)

    def get_heart_rate(self, date):

        
        data_sec = authd_client.intraday_time_series('activities/heart', "{0:%Y-%m-%d}".format(date), detail_level='1sec')
        rt', DATE, detail_level='1sec')
        heart_sec = data_sec["activities-heart-intraday"]["dataset"]
        return heart_sec

