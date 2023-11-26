import serial
import matplotlib.pyplot as plt

ardruino = serial.Serial(port="COM6", baudrate=9600, timeout=0.1)
temperatures = []
humidities = []

def read():
    data = ""
    while len(data) < 1:
        data = ardruino.readline()
    return data.decode("utf-8")

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