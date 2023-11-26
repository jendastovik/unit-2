# bubble sort
def bubble_sort(x: list):
    changed = True
    while changed:
        changed = False
        for i in range(len(x)-1):
            if x[i] > x[i+1]:
                x[i], x[i+1] = x[i+1], x[i]
                changed = True
    return x    

import random
#x = [random.randint(0, 100) for _ in range(20)]
#print(bubble_sort(x))

# quiz 28 with bubble sort
def bubble_sort2(x, keys):
    changed = True
    while changed:
        changed = False
        for i in range(len(x)-1):
            if x[i] > x[i+1]:
                x[i], x[i+1] = x[i+1], x[i]
                keys[i], keys[i+1] = keys[i+1], keys[i]
                changed = True
    return x    

def dic_sort(dic):
    keys = list(dic.keys())
    vals = list(dic.values())
    vals, keys = bubble_sort2(vals, keys)
    dic = {}
    for i in range(len(keys)):
        dic[keys[i]] = vals[i]
    return dic

# api request
import requests
import matplotlib.pyplot as plt

ip = "192.168.6.153"

from unit2_lib import get_sensor, smoothing

sensor1 = get_sensor()
x, y = smoothing(sensor1, smoothing_win=10, overlap=0.5)
plt.subplot(2, 1, 1)
plt.plot(sensor1)
plt.subplot(2, 1, 2)
plt.plot(x, y, color="red")
plt.show()

# quiz 29
sensor1 = get_sensor(id=2)
x, y = smoothing(sensor1, smoothing_win=4, overlap=0.5)
plt.subplot(2, 1, 1)
plt.plot(sensor1)
plt.subplot(2, 1, 2)
plt.plot(x, y, color="red")
plt.show()





    