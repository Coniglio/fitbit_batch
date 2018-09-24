import datetime
import fitbit

if __name__ == '__main__':
    fitbit = Fitbit()
    today = datetime.datetime.now()
    heart_rate = fitbit.get_heart_rate(today)
    print("Get heart rate.count:%d " % len(heart_rate))
