import sys
import time
import board
from adafruit_motorkit import MotorKit
from multiprocessing import Process, Value, Array

kit = MotorKit(i2c=board.I2C()) #initializes motors, takes 10 seconds
times = "00:00:10"
def Customwashster(timestr):
    seconds = 0
    timestr
    for part in timestr.split(':'):
        seconds= seconds*60 + int(part, 10)
    try:
        kit.motor1.throttle = 1.0
        kit.motor2.throttle = 1.0
        kit.motor3.throttle = 1.0
        kit.motor4.throttle = 1.0
        print('running motor for', seconds, 'seconds')
        time.sleep(seconds)
            
        kit.motor1.throttle = 0
        kit.motor2.throttle = 0
        kit.motor3.throttle = 0
        kit.motor4.throttle = 0
        print('done')

    except KeyboardInterrupt:
        print('script interrupted')
        kit.motor1.throttle = 0
        kit.motor2.throttle = 0
        kit.motor3.throttle = 0
        kit.motor4.throttle = 0
        sys.exit()
