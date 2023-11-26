import requests
def get_sensor(ip = "192.168.6.153", id = 1):
    ans = requests.get(f"http://{ip}/readings")
    data = ans.json()

    sensors = data["readings"][0]
    sensor = []
    for s in sensors:
        if s["sensor_id"] == id:
            sensor.append(s["value"])
    return sensor

def smoothing(x, smoothing_win = 5, overlap = 1):
    smooth_x = []
    t = []
    for i in range(0, len(x), int(smoothing_win*overlap)):
        smooth_x.append(sum(x[i:i+smoothing_win])/smoothing_win)
        t.append(i)
    return t, smooth_x


