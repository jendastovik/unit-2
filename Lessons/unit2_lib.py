import requests
from datetime import datetime
import matplotlib.pyplot as plt

def get_sensor(ip = "192.168.6.153", id = 1):
    ans = requests.get(f"http://{ip}/readings")
    data = ans.json()

    sensors = data["readings"][0]
    sensor = []
    for s in sensors:
        if s["sensor_id"] == id:
            sensor.append(s["value"])
    return sensor

def get_sensor_whole(ip = "192.168.6.153", id = 1):
    ans = requests.get(f"http://{ip}/readings")
    data = ans.json()

    sensors = data["readings"][0]
    sensor = []
    for s in sensors:
        if s["sensor_id"] == id:
            sensor.append(s)
    return sensor

def smoothing(x, smoothing_win = 5, overlap = 1):
    smooth_x = []
    t = []
    for i in range(0, len(x), int(smoothing_win*overlap)):
        smooth_x.append(sum(x[i:i+smoothing_win])/smoothing_win)
        t.append(i)
    return t, smooth_x

def get_data_from_date(yr, month, day, records):
    date = datetime(yr, month, day).date()
    data = []
    for r in records:
        d = r["datetime"]
        datetime_object = datetime.strptime(d, '%Y-%m-%dT%H:%M:%S.%f')
        if datetime_object.date() == date:
            data.append(r)
    return data

def print_dates_from_data(data):
    dates = []
    for r in data:
        d = r["datetime"]
        datetime_object = datetime.strptime(d, '%Y-%m-%dT%H:%M:%S.%f')
        if datetime_object.date() not in dates:
            dates.append(datetime_object.date())
            print(datetime_object.date())
    return dates



sen = get_sensor_whole(id=4)
print_dates_from_data(sen)
sensors = get_data_from_date(2023, 12, 9, sen)

val = []
time = []

for s in sensors:
    val.append(s["value"])
    time.append(datetime.strptime(s["datetime"], '%Y-%m-%dT%H:%M:%S.%f'))

plt.style.use("ggplot")
plt.scatter(time, val)
plt.gcf().autofmt_xdate()
plt.show()

# because in 2.12. the weather was 7 degrees in a day and 1 degree in a night
# we use data from 20.11 where the weather was 8 degree in a day and 2 degree in a night
# wich is by far the most similar to the 2.12. data from our options from 17.11. to 21.11. and 7.12. onwards


