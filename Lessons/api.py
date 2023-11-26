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
sensor = {"name": "sensor2", "type": "temperature", "location": "asama25", "unit": "C"}

#put cookie in headers of request
headers = {"Authorization": f"Bearer {cookie}"} 

# crate new sensor
#ans = requests.post(f"http://{ip}/sensor/new", json=sensor, headers=headers)
#print(ans.json())

# add data to sensor
record = {"sensor_id": 24, "value": 18}
ans = requests.post(f"http://{ip}/reading/new", json=record, headers=headers)
print(ans.json())

# get data from my sensor
readings = requests.get(f"http://{ip}/user/readings", headers=headers)
print(readings.json())

# get my sensors
#sen = requests.get(f"http://{ip}/sensors", headers=headers)
#print(sen.json())
