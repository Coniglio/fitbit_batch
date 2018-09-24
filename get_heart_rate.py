import fitbit
import configparser

inifile = configparser.ConfigParser()
inifile.read('./config.ini', 'UTF-8')
client_id = inifile.get('fitbit', 'client_id')
client_secret = inifile.get('fitbit', 'client_secret')
access_token = inifile.get('fitbit', 'access_token')
refresh_token = inifile.get('fitbit', 'refresh_token')

DATE = "2018-09-22"

authd_client = fitbit.Fitbit(client_id, client_secret, access_token=access_token, refresh_token=refresh_token)

# Fitbit APIから心拍数を取得
data_sec = authd_client.intraday_time_series('activities/heart', DATE, detail_level='1sec')
heart_sec = data_sec["activities-heart-intraday"]["dataset"]
print("Get heart rate.count:%d " % len(heart_sec))

