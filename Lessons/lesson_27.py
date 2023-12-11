import serial
import matplotlib.pyplot as plt
import adafruit_dht 

dht_device = adafruit_dht.DHT11
temp, hum = adafruit_dht.read_retry(dht_device, 13)

print(f"temp: {temp}, hum: {hum}")


ardruino = serial.Serial(port="COM5", baudrate=9600, timeout=0.1)
temperatures = []
humidities = []



def read():
    data = ""
    while not data:
        data = ardruino.readline()
    print(data)
    return data.decode("utf-8")

print(read())

while True:
    print(read())
    res = read()
    hum, temp = res.split()
    hum = int(hum.split(":")[1].strip())
    temp = int(temp.split(":")[1].strip())
    temperatures.append(temp)
    humidities.append(hum)
    print(f"hum: {hum}, temp: {temp}")

plt.figure()
plt.subplot(2, 1, 1)
plt.plot(temperatures)
plt.subplot(2, 1, 2)
plt.plot(humidities)