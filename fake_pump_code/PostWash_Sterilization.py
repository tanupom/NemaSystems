import time
import sys

def Postwashster():
    try:
        motor1 = 1.0
        motor2 = 1.0
        motor3 = 1.0
        motor4 = 1.0
        print('running motor for 5 seconds')
        time.sleep(5)
            
        motor1 = 0
        motor2 = 0
        motor3 = 0
        motor4 = 0

    except KeyboardInterrupt:
        print('script interrupted')
        motor1 = 0
        motor2 = 0
        motor3 = 0
        motor4 = 0
        sys.exit()

