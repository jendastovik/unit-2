from pyfirmata import Arduino
import pyfirmata
import time


board = Arduino('/dev/COM')
print("Communication Successfully started")

data = pyfirmata.util.Iterator(board)
data.start()

LED_12 = board.digital[12]
LED_12.mode = pyfirmata.OUTPUT
LED_12.write(0)

for _ in range(100):
    LED_12.write(1)
    time.sleep(0.5)
    LED_12.write(0)
    time.sleep(0.5)

board.exit()