from practicum import findDevices,McuBoard
from peri import PeriBoard

import time

devices = findDevices()
b = PeriBoard(devices[0])

for i in range (100):
    print (b.getAcceleroX(),b.getAcceleroY())
    time.sleep(1)
