import json
import datetime
import configparser

FITBIT_BASE_URL = "https://api.fitbit.com/"

inifile = configparser.ConfigParser()
inifile.read('/opt/fitbit/config.ini', 'UTF-8')
client_id = inifile.get('fitbit', 'client_id')
client_secret = inifile.get('fitbit', 'client_secret')
access_token = inifile.get('fitbit', 'access_token')
refresh_token = inifile.get('fitbit', 'refresh_token') 

host = inifile.get('mysql', 'host')
db = inifile.get('mysql', 'db')
user = inifile.get('mysql', 'user')
password = inifile.get('mysql', 'password')
 
def getRestingHeartRate(day):
    """
    安静時心拍数を取得する
    """
    import requests
    from requests.auth import HTTPBasicAuth as hba
 
    api_ver = "1"
    url = FITBIT_BASE_URL + api_ver + "/user/-/activities/heart/date/" + \
            day.strftime('%Y-%m-%d') + "/1d.json" 
    headers = {"Authorization" : "Bearer " + access_token} 
    res = requests.get(url,headers=headers)
    jsonStr = json.loads(res.text)

    return jsonStr['activities-heart'][0]['value']['restingHeartRate']

def insertRestingHeartRate(date, heart_rate):
    """
    安静時心拍数を格納する
    """
    import pymysql.cursors
    conn = pymysql.connect(
        host=host,
        user=user,
        password=password,
        db=db,
        cursorclass=pymysql.cursors.DictCursor
     )
    try:
        with conn.cursor() as cursor:
            sql = "insert into resting_heart_rate (resting_date, resting_heart_rate) values(%s, %s)"
            cursor.execute(sql, (date.strftime('%Y-%m-%d'), heart_rate))
            conn.commit()
    finally:
        conn.close()
    
if __name__ == "__main__":
    # 安静時心拍数を取得する年月日を取得
    day = datetime.datetime.now() - datetime.timedelta(days=1)

    # 安静時心拍数を取得
    heart_rate = getRestingHeartRate(day)

    print(day, heart_rate)

    # 安静時心拍数を格納
    insertRestingHeartRate(day, heart_rate)

