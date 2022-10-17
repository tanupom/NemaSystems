import time
import sys
import board
from adafruit_motorkit import MotorKit
from django.shortcuts import HttpResponse

kit = MotorKit(i2c=board.I2C())
def StopAllPumps():
    try:
        kit.motor1.throttle = 0
        kit.motor2.throttle = 0
        kit.motor3.throttle = 0
        kit.motor4.throttle = 0
        print('pumps stopped')
    except KeyboardInterrupt:
        print('script interrupted')
        kit.motor1.throttle = 0
        kit.motor2.throttle = 0
        kit.motor3.throttle = 0
        kit.motor4.throttle = 0
        sys.exit()
def StopAllPumpsHTML():
    try:
        kit.motor1.throttle = 0
        kit.motor2.throttle = 0
        kit.motor3.throttle = 0
        kit.motor4.throttle = 0
        print('pumps stopped')
    except KeyboardInterrupt:
        print('script interrupted')
        kit.motor1.throttle = 0
        kit.motor2.throttle = 0
        kit.motor3.throttle = 0
        kit.motor4.throttle = 0
        sys.exit()
    return HttpResponse("Hello World")
#StopAllPumps()