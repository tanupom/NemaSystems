import time
import sys
import board
from adafruit_motorkit import MotorKit

kit = MotorKit(i2c=board.I2C())
def Postwashster():
    try:
        kit.motor1.throttle = 1
        time.sleep(60)
        kit.motor1.throttle = 0
    except KeyboardInterrupt:
        print('script interrupted')
        kit.motor1.throttle = 0
        sys.exit()
#Postwashster()