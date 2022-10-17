import time
import sys
import board
from adafruit_motorkit import MotorKit
from django.shortcuts import HttpResponse

kit = MotorKit(i2c=board.I2C())
def StartPumpNumber(pumpNumber):
    if(pumpNumber==1):
        try:
            kit.motor1.throttle = 1
            print('pumps stopped')
        except KeyboardInterrupt:
            print('script interrupted')
            kit.motor1.throttle = 1
            sys.exit()
    elif(pumpNumber==2):
        try:
            kit.motor2.throttle = 1
            print('pumps stopped')
        except KeyboardInterrupt:
            print('script interrupted')
            kit.motor2.throttle = 1
            sys.exit()
    elif(pumpNumber==3):
        try:
            kit.motor3.throttle = 1
            print('pumps stopped')
        except KeyboardInterrupt:
            print('script interrupted')
            kit.motor3.throttle = 1
            sys.exit()
    elif(pumpNumber==4):
        try:
            kit.motor4.throttle = 1
            print('pumps stopped')
        except KeyboardInterrupt:
            print('script interrupted')
            kit.motor4.throttle = 1
            sys.exit()

#StopAllPumps()