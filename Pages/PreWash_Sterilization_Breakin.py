import time
import sys
import board
from adafruit_motorkit import MotorKit

kit = MotorKit(i2c=board.I2C())
def Prewashster():
    print("Testing")
    try:
        x = 0
        while x < 120:
            t_end = time.time() + 60 * 2
            kit.motor1.throttle = 1.0
            kit.motor2.throttle = 1.0
            kit.motor3.throttle = 1.0
            kit.motor4.throttle = 1.0
            while time.time() < t_end:
                print(t_end-time.time())
            kit.motor1.throttle = 0
            kit.motor2.throttle = 0
            kit.motor3.throttle = 0
            kit.motor4.throttle = 0
            t_end = time.time() + 60 * 5
            while time.time() < t_end:
                print(t_end-time.time())
            x = x + 1
    except KeyboardInterrupt:
        print('script interrupted')
        kit.motor1.throttle = 0
        kit.motor2.throttle = 0
        kit.motor3.throttle = 0
        kit.motor4.throttle = 0
        sys.exit()
Prewashster()
