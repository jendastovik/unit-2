def sel_sort(x, keys):
    for i in range(len(x)-1):
        for n in range(i + 1, len(x)):
            if x[i] > x[n]:
                x[i], x[n] = x[n], x[i]
                keys[i], keys[n] = keys[n], keys[i]
    return x, keys

def dic_sort(dic):
    keys = list(dic.keys())
    vals = list(dic.values())
    vals, keys = sel_sort(vals, keys)
    dic = {}
    for i in range(len(keys)):
        dic[keys[i]] = vals[i]
    return dic

dic = {"a": 5, "b": 2, "c": 3, "d": 1, "e": 4}
#print(dic_sort(dic))

#api part 2
import requests

user = {"username": "Jenda", "password": "stoikForPres"}
ip = "192.168.6.153"

# register user
#ans = requests.post(f"http://{ip}/register", json=user)
#print(ans.json())

# login user
ans = requests.post(f"http://{ip}/login", json=user)
#print(ans.json())
cookie = ans.json()["access_token"]

#create sensor
sensor = {"name": "sensor1", "type": "temperature", "location": "asama25", "unit": "C"}

#put cookie in headers of request
headers = {"Authorization": f"Bearer {cookie}"} 

# crate new sensor
#ans = requests.post(f"http://{ip}/sensor/new", json=sensor, headers=headers)
#print(ans.json())

# add data to sensor
record = {"sensor_id": 12, "value": 28}
ans = requests.post(f"http://{ip}/reading/new", json=record, headers=headers)
print(ans.json())

# get data from my sensor
readings = requests.get(f"http://{ip}/user/readings", headers=headers)
print(readings.json())

# get my sensors
sen = requests.get(f"http://{ip}/sensors", headers=headers)
print(sen.json())

