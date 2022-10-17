import sys
import time
import os
'''shutdown = input("Do you wish to shutdown your computer ? (yes / no): ")
  
if shutdown == 'no':
    exit()
else:
    os.system("shutdown /s /t 1")
'''

#import board
#from adafruit_motorkit import MotorKit

#kit = MotorKit(i2c=board.I2C())
#Request = '00:00:05'


'''def to_seconds(timestr):
    seconds= 0
    for part in timestr.split(':'):
        seconds= seconds*60 + int(part, 10)
    return(seconds)
#Converts user input from 00:00:00 Hour:min:sec into a string of the number of seconds
 = str(input('Enter Time as 00:00:00 Hour:Mins:Secs'))
#This line prompts the user for the time and takes a input of 00:00:00
# 
# 
# def to_seconds(timestr):
    seconds= 0
    for part in timestr.split(':'):
        seconds= seconds*60 + int(part, 10)
    return(seconds)
'''







def Customwashster(timestr):
    seconds= 0
    str(timestr)
    for part in timestr.split(':'):
        seconds= seconds*60 + int(part, 10)
        continue

    try:
        motor1 = 1.0
        motor2 = 1.0
        motor3 = 1.0
        motor4 = 1.0
        print('running motor for', seconds, 'seconds')
        time.sleep(seconds)
            
        motor1 = 0
        motor2 = 0
        motor3 = 0
        motor4 = 0
        print('done', motor1)

    except KeyboardInterrupt:
        print('script interrupted')
        motor1 = 0
        motor2 = 0
        motor3 = 0
        motor4 = 0
        sys.exit()
