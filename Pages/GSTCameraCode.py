
from fileinput import filename
import sys
import traceback
import argparse
import time
from cv2 import CamShift
import gi
from multiprocessing import Process, Value, Array
import board
from adafruit_motorkit import MotorKit
import subprocess
from subprocess import call
import cv2
import os
import shutil
import datetime
import json
global p
p = None
kit = MotorKit(i2c=board.I2C())

gi.require_version('Gst', '1.0')
from gi.repository import Gst, GLib 
def on_message(bus: Gst.Bus, message: Gst.Message, loop: GLib.MainLoop):
        mtype = message.type
        """
            Gstreamer Message Types and how to parse
            https://lazka.github.io/pgi-docs/Gst-1.0/flags.html#Gst.MessageType
        """
        if mtype == Gst.MessageType.EOS:
            print("End of stream")
            loop.quit()

        elif mtype == Gst.MessageType.ERROR:
            err, debug = message.parse_error()
            print(err, debug)
            loop.quit()

        elif mtype == Gst.MessageType.WARNING:
            err, debug = message.parse_warning()
            print(err, debug)

        return True

def deleteallwithinfolder(pathtofolder):    
    for filename in os.listdir(pathtofolder):
        file_path = os.path.join(pathtofolder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))
            #args=(num,ti,ti2,pip,AssName,Res,fr)
def StartCamerasFunction(num,s,s2,pi,a,r,f):
    t = time.time()
    x = datetime.datetime.now()
    Filename1 = a + "_Cam1_" + str(x) +".mp4"
    Filename1 = Filename1.replace(" ", "_")
    print(Filename1)
    Filename2 = a + "_Cam2_" + str(x) +".mp4"
    Filename2 = Filename2.replace(" ", "_")
    print(Filename2)
    Filename3 = a + "_Cam3_" + str(x) +".mp4"
    Filename3 = Filename3.replace(" ", "_")
    print(Filename3)
    Filename4 = a + "_Cam4_" + str(x) +".mp4"
    Filename4 = Filename4.replace(" ", "_")
    print(Filename4)
    CamerasSelected = "/home/jetson/Documents/Infinity2.0Django_09122022/SelectedCameras.json"
    f = open(CamerasSelected)
    CameraData = json.load(f)
    f.close()
    # Initializes Gstreamer, it's variables, paths
    Gst.init(Gst.init(sys.argv))
    if(pi.value == 0): #Timelapse
        Filename1 = Filename1.replace(".mp4","")
        Filename2 = Filename2.replace(".mp4","")
        Filename3 = Filename3.replace(".mp4","")
        Filename4 = Filename4.replace(".mp4","")
        print(Filename1)
        print(Filename2)
        print(Filename3)
        print(Filename4)
        try:
            os.mkdir("/home/jetson/Documents/Infinity2.0Django_09122022/videos"+Filename1+"/")
        except:
            pass
        try:
            os.mkdir("/home/jetson/Documents/Infinity2.0Django_09122022/videos"+Filename2+"/")
        except:
            pass
        try:
            os.mkdir("/home/jetson/Documents/Infinity2.0Django_09122022/videos"+Filename3+"/")
        except:
            pass
        try:
            os.mkdir("/home/jetson/Documents/Infinity2.0Django_09122022/videos"+Filename4+"/")
        except:
            pass
        DEFAULT_PIPELINE = "v4l2src device=/dev/video0 \
! image/jpeg,width=(int)3264, height=(int)2448 \
! jpegdec \
! video/x-raw \
! videocrop top=350 left=0 right=0 bottom=350 \
! videoconvert \
! videorate \
! video/x-raw, framerate=1/5 \
! tee name=t t. \
! queue \
! videoscale \
! video/x-raw,width=1920, height=1080 \
! theoraenc \
! oggmux \
! tcpserversink host=0.0.0.0 port=8084 t.\
! queue \
! videoconvert \
! jpegenc \
! multifilesink location=/home/infinitysystem/Documents/Infinity2.0Django_09122022/Videos/TimelapseFolders/"+Filename1+"/"+"Frame_%06d.jpg \
v4l2src device=/dev/video2 \
! image/jpeg,width=(int)3264, height=(int)2448 \
! jpegdec \
! video/x-raw \
! videocrop top=350 left=0 right=0 bottom=350 \
! videoconvert \
! videorate \
! video/x-raw, framerate=1/5 \
! tee name=t2 t2. \
! queue \
! videoscale \
! video/x-raw,width=1920, height=1080 \
! theoraenc \
! oggmux \
! tcpserversink host=0.0.0.0 port=8085 t2.\
! queue \
! videoconvert \
! jpegenc \
! multifilesink location=/home/infinitysystem/Documents/Infinity2.0Django_09122022/Videos/TimelapseFolders/"+Filename2+"/"+"Frame_%06d.jpg \
v4l2src device=/dev/video4 \
! image/jpeg,width=(int)3264, height=(int)2448 \
! jpegdec \
! video/x-raw \
! videocrop top=350 left=0 right=0 bottom=350 \
! videoconvert \
! videorate \
! video/x-raw, framerate=1/5 \
! tee name=t3 t3. \
! queue \
! videoscale \
! video/x-raw,width=1920, height=1080 \
! theoraenc \
! oggmux \
! tcpserversink host=0.0.0.0 port=8086 t3.\
! queue \
! videoconvert \
! jpegenc \
! multifilesink location=/home/infinitysystem/Documents/Infinity2.0Django_09122022/Videos/TimelapseFolders/"+Filename3+"/"+"Frame_%06d.jpg \
v4l2src device=/dev/video6 \
! image/jpeg,width=(int)3264, height=(int)2448 \
! jpegdec \
! video/x-raw \
! videocrop top=350 left=0 right=0 bottom=350 \
! videoconvert \
! videorate \
! video/x-raw, framerate=1/5 \
! tee name=t4 t4. \
! queue \
! videoscale \
! video/x-raw,width=1920, height=1080 \
! theoraenc \
! oggmux \
! tcpserversink host=0.0.0.0 port=8087 t4.\
! queue \
! videoconvert \
! jpegenc \
! multifilesink location=/home/infinitysystem/Documents/Infinity2.0Django_09122022/Videos/TimelapseFolders/"+Filename4+"/"+"Frame_%06d.jpg"

    elif(pi.value == 1):
        DEFAULT_PIPELINE = "v4l2src device=/dev/video2 \
! image/jpeg,width=(int)3264, height=(int)2448 \
! jpegdec \
! video/x-raw \
! videocrop top=350 left=0 right=0 bottom=350 \
! videoconvert \
! videorate \
! video/x-raw, framerate=5/1 \
! tee name=t t. \
! queue \
! videoscale \
! video/x-raw,width=1920, height=1080 \
! theoraenc \
! oggmux \
! tcpserversink host=192.168.1.59 port=8084 t.\
! queue \
! nvvideoconvert \
! nvv4l2h265enc \
! h265parse \
! qtmux \
! filesink location=/mnt/InternamDrive/Videos/Recorded_Video/"+Filename1+" \
v4l2src device=/dev/video0 \
! image/jpeg,width=(int)3264, height=(int)2448 \
! jpegdec \
! video/x-raw \
! videocrop top=350 left=0 right=0 bottom=350 \
! videoconvert \
! videorate \
! video/x-raw, framerate=5/1 \
! tee name=t1 t1. \
! queue \
! videoscale \
! video/x-raw,width=1920, height=1080 \
! theoraenc \
! oggmux \
! tcpserversink host=192.168.1.59 port=8085 t1.\
! queue \
! nvvideoconvert \
! nvv4l2h265enc \
! h265parse \
! qtmux \
! filesink location=/mnt/InternamDrive/Videos/Recorded_Video/"+Filename2+" \
v4l2src device=/dev/video4 \
! image/jpeg,width=(int)3264, height=(int)2448 \
! jpegdec \
! video/x-raw \
! videocrop top=350 left=0 right=0 bottom=350 \
! videoconvert \
! videorate \
! video/x-raw, framerate=5/1 \
! tee name=t2 t2. \
! queue \
! videoscale \
! video/x-raw,width=1920, height=1080 \
! theoraenc \
! oggmux \
! tcpserversink host=192.168.1.59 port=8086 t2.\
! queue \
! nvvideoconvert \
! nvv4l2h265enc \
! h265parse \
! qtmux \
! filesink location=/mnt/InternamDrive/Videos/Recorded_Video/"+Filename3+" \
v4l2src device=/dev/video6 \
! image/jpeg,width=(int)3264, height=(int)2448 \
! jpegdec \
! video/x-raw \
! videocrop top=350 left=0 right=0 bottom=350 \
! videoconvert \
! videorate \
! video/x-raw, framerate=5/1 \
! tee name=t3 t3. \
! queue \
! videoscale \
! video/x-raw,width=1920, height=1080 \
! theoraenc \
! oggmux \
! tcpserversink host=192.168.1.59 port=8087 t3.\
! queue \
! nvvideoconvert \
! nvv4l2h265enc \
! h265parse \
! qtmux \
! filesink location=/mnt/InternamDrive/Videos/Recorded_Video/"+Filename4
    else:
        DEFAULT_PIPELINE = "v4l2src device=/dev/video2 \
    ! image/jpeg,width=(int)3264, height=(int)2448 \
    ! jpegdec \
    ! video/x-raw \
    ! videoflip method=rotate-180 \
    ! videocrop top=350 left=0 right=0 bottom=350 \
    ! videoconvert \
    ! videorate \
    ! video/x-raw,framerate=5/1 \
    ! videoscale \
    ! video/x-raw,width=1920, height=1080 \
    ! theoraenc \
    ! oggmux \
    ! tcpserversink host=192.168.1.59 port=8080 \
    v4l2src device=/dev/video0 \
    ! image/jpeg,width=(int)3264, height=(int)2448 \
    ! jpegdec \
    ! video/x-raw \
    ! videoflip method=rotate-180 \
    ! videocrop top=350 left=0 right=0 bottom=350 \
    ! videoconvert \
    ! videorate \
    ! video/x-raw,framerate=5/1 \
    ! videoscale \
    ! video/x-raw,width=1920, height=1080 \
    ! theoraenc \
    ! oggmux \
    ! tcpserversink host=192.168.1.59 port=8081 \
    v4l2src device=/dev/video4 \
    ! image/jpeg,width=(int)3264, height=(int)2448 \
    ! jpegdec \
    ! video/x-raw \
    ! videocrop top=350 left=0 right=0 bottom=350 \
    ! videoconvert \
    ! videorate \
    ! video/x-raw,framerate=5/1 \
    ! videoscale \
    ! video/x-raw,width=1920, height=1080 \
    ! theoraenc \
    ! oggmux \
    ! tcpserversink host=192.168.1.59 port=8082 \
    v4l2src device=/dev/video6 \
    ! image/jpeg,width=(int)3264, height=(int)2448 \
    ! jpegdec \
    ! video/x-raw \
    ! videocrop top=350 left=0 right=0 bottom=350 \
    ! videoconvert \
    ! videorate \
    ! video/x-raw,framerate=5/1 \
    ! videoscale \
    ! video/x-raw,width=1920, height=1080 \
    ! theoraenc \
    ! oggmux \
    ! tcpserversink host=192.168.1.59 port=8083"

    print(DEFAULT_PIPELINE)

    #ap = argparse.ArgumentParser()
   # ap.add_argument("-p", "--pipeline", required=False,
                 #   default=DEFAULT_PIPELINE, help="Gstreamer pipeline without gst-launch")

   # args = vars(ap.parse_args())
    command = DEFAULT_PIPELINE

    # Gst.Pipeline https://lazka.github.io/pgi-docs/Gst-1.0/classes/Pipeline.html
    # https://lazka.github.io/pgi-docs/Gst-1.0/functions.html#Gst.parse_launch
    global pipeline
    pipeline = Gst.parse_launch(command)
    # https://lazka.github.io/pgi-docs/Gst-1.0/classes/Bus.html
    bus = pipeline.get_bus()

    # allow bus to emit messages to main thread
    bus.add_signal_watch()

    # Start pipeline
    pipeline.set_state(Gst.State.PLAYING)

    # Init GObject loop to handle Gstreamer Bus Events
    #loop = GLib.MainLoop()

    # Add handler to specific signal
    # https://lazka.github.io/pgi-docs/GObject-2.0/classes/Object.html#GObject.Object.connect
    #bus.connect("message", on_message, loop)
    print("S1",s.value,"S2",s2.value)
    call(["v4l2-ctl", "-d", "/dev/video0", "-c", "focus_auto=0"])# min=1 max=0 step=1 default=1 value=528
    call(["v4l2-ctl", "-d", "/dev/video2", "-c", "focus_auto=0"])
    call(["v4l2-ctl", "-d", "/dev/video4", "-c", "focus_auto=0"])
    call(["v4l2-ctl", "-d", "/dev/video6", "-c", "focus_auto=0"])
    time.sleep(.2)
    call(["v4l2-ctl", "-d", "/dev/video0", "-c", "focus_absolute=490"])# min=1 max=1023 step=1 default=1 value=528
    call(["v4l2-ctl", "-d", "/dev/video2", "-c", "focus_absolute=490"])
    call(["v4l2-ctl", "-d", "/dev/video4", "-c", "focus_absolute=490"])
    call(["v4l2-ctl", "-d", "/dev/video6", "-c", "focus_absolute=432"])
    time.sleep(.2)
    
    while(abs(time.time()-t)<s.value + s2.value + 25 and num.value == 0.0):
        #print(s.value,s2.value,num.value)
        if(time.time()-t<s.value):
            if(time.time()-t<5 and s.value != 0 and s.value != 90001):
                print("Pumps Started")
                
                call(["v4l2-ctl", "-d", "/dev/video0", "-c", "focus_absolute=490"])# min=1 max=1023 step=1 default=1 value=528
                call(["v4l2-ctl", "-d", "/dev/video2", "-c", "focus_absolute=490"])
                call(["v4l2-ctl", "-d", "/dev/video4", "-c", "focus_absolute=490"])
                call(["v4l2-ctl", "-d", "/dev/video6", "-c", "focus_absolute=432"])
                time.sleep(.2)
                call(["v4l2-ctl", "-d", "/dev/video0", "-c", "brightness=20"]) # min=-64 max=64 step=1 default=0 value=0
                call(["v4l2-ctl", "-d", "/dev/video2", "-c", "brightness=20"])
                call(["v4l2-ctl", "-d", "/dev/video4", "-c", "brightness=20"])
                call(["v4l2-ctl", "-d", "/dev/video6", "-c", "brightness=20"])
                time.sleep(.2)
                call(["v4l2-ctl", "-d", "/dev/video0", "-c", "saturation=0"])# min=0 max=128 step=1 default=64 value=128
                call(["v4l2-ctl", "-d", "/dev/video2", "-c", "saturation=0"])
                call(["v4l2-ctl", "-d", "/dev/video4", "-c", "saturation=0"])
                call(["v4l2-ctl", "-d", "/dev/video6", "-c", "saturation=0"])
                time.sleep(.2)
                call(["v4l2-ctl", "-d", "/dev/video0", "-c", "contrast=32"])# min=0 max=64 step=1 default=32 value=32
                call(["v4l2-ctl", "-d", "/dev/video2", "-c", "contrast=32"])
                call(["v4l2-ctl", "-d", "/dev/video4", "-c", "contrast=32"])
                call(["v4l2-ctl", "-d", "/dev/video6", "-c", "contrast=32"])
                time.sleep(.2)
                call(["v4l2-ctl", "-d", "/dev/video0", "-c", "sharpness=4"])# min=0 max=6 step=1 default=3 value=3
                call(["v4l2-ctl", "-d", "/dev/video2", "-c", "sharpness=4"])
                call(["v4l2-ctl", "-d", "/dev/video4", "-c", "sharpness=4"])
                call(["v4l2-ctl", "-d", "/dev/video6", "-c", "sharpness=4"])
                time.sleep(.2)
                call(["v4l2-ctl", "-d", "/dev/video0", "-c", "backlight_compensation=0"])# min=0 max=2 step=1 default=1 value=1
                call(["v4l2-ctl", "-d", "/dev/video2", "-c", "backlight_compensation=0"])
                call(["v4l2-ctl", "-d", "/dev/video4", "-c", "backlight_compensation=0"])
                call(["v4l2-ctl", "-d", "/dev/video6", "-c", "backlight_compensation=0"])
                time.sleep(.2)
                call(["v4l2-ctl", "-d", "/dev/video0", "-c", "gamma=100"])# min=72 max=500 step=1 default=100 value=0
                call(["v4l2-ctl", "-d", "/dev/video2", "-c", "gamma=100"])
                call(["v4l2-ctl", "-d", "/dev/video4", "-c", "gamma=100"])
                call(["v4l2-ctl", "-d", "/dev/video6", "-c", "gamma=100"])
                time.sleep(.2)
                call(["v4l2-ctl", "-d", "/dev/video0", "-c", "gain=0"])# min=0 max=100 step=1 default=0 value=0
                call(["v4l2-ctl", "-d", "/dev/video2", "-c", "gain=0"])
                call(["v4l2-ctl", "-d", "/dev/video4", "-c", "gain=0"])
                call(["v4l2-ctl", "-d", "/dev/video6", "-c", "gain=0"])
            elif time.time()-t<5:
                call(["v4l2-ctl", "-d", "/dev/video0", "-c", "focus_absolute=490"])# min=1 max=1023 step=1 default=1 value=528
                call(["v4l2-ctl", "-d", "/dev/video2", "-c", "focus_absolute=490"])
                call(["v4l2-ctl", "-d", "/dev/video4", "-c", "focus_absolute=490"])
                call(["v4l2-ctl", "-d", "/dev/video6", "-c", "focus_absolute=432"])
                time.sleep(.2)
                call(["v4l2-ctl", "-d", "/dev/video0", "-c", "brightness=20"]) # min=-64 max=64 step=1 default=0 value=0
                call(["v4l2-ctl", "-d", "/dev/video2", "-c", "brightness=20"])
                call(["v4l2-ctl", "-d", "/dev/video4", "-c", "brightness=20"])
                call(["v4l2-ctl", "-d", "/dev/video6", "-c", "brightness=20"])
                time.sleep(.2)
                call(["v4l2-ctl", "-d", "/dev/video0", "-c", "saturation=0"])# min=0 max=128 step=1 default=64 value=128
                call(["v4l2-ctl", "-d", "/dev/video2", "-c", "saturation=0"])
                call(["v4l2-ctl", "-d", "/dev/video4", "-c", "saturation=0"])
                call(["v4l2-ctl", "-d", "/dev/video6", "-c", "saturation=0"])
                time.sleep(.2)
                call(["v4l2-ctl", "-d", "/dev/video0", "-c", "contrast=32"])# min=0 max=64 step=1 default=32 value=32
                call(["v4l2-ctl", "-d", "/dev/video2", "-c", "contrast=32"])
                call(["v4l2-ctl", "-d", "/dev/video4", "-c", "contrast=32"])
                call(["v4l2-ctl", "-d", "/dev/video6", "-c", "contrast=32"])
                time.sleep(.2)
                call(["v4l2-ctl", "-d", "/dev/video0", "-c", "sharpness=4"])# min=0 max=6 step=1 default=3 value=3
                call(["v4l2-ctl", "-d", "/dev/video2", "-c", "sharpness=4"])
                call(["v4l2-ctl", "-d", "/dev/video4", "-c", "sharpness=4"])
                call(["v4l2-ctl", "-d", "/dev/video6", "-c", "sharpness=4"])
                time.sleep(.2)
                call(["v4l2-ctl", "-d", "/dev/video0", "-c", "backlight_compensation=0"])# min=0 max=2 step=1 default=1 value=1
                call(["v4l2-ctl", "-d", "/dev/video2", "-c", "backlight_compensation=0"])
                call(["v4l2-ctl", "-d", "/dev/video4", "-c", "backlight_compensation=0"])
                call(["v4l2-ctl", "-d", "/dev/video6", "-c", "backlight_compensation=0"])
                time.sleep(.2)
                call(["v4l2-ctl", "-d", "/dev/video0", "-c", "gamma=100"])# min=72 max=500 step=1 default=100 value=0
                call(["v4l2-ctl", "-d", "/dev/video2", "-c", "gamma=100"])
                call(["v4l2-ctl", "-d", "/dev/video4", "-c", "gamma=100"])
                call(["v4l2-ctl", "-d", "/dev/video6", "-c", "gamma=100"])
                time.sleep(.2)
                call(["v4l2-ctl", "-d", "/dev/video0", "-c", "gain=0"])# min=0 max=100 step=1 default=0 value=0
                call(["v4l2-ctl", "-d", "/dev/video2", "-c", "gain=0"])
                call(["v4l2-ctl", "-d", "/dev/video4", "-c", "gain=0"])
                call(["v4l2-ctl", "-d", "/dev/video6", "-c", "gain=0"])
            elif s.value != 90001 and (CameraData['Camera1']=="true" or CameraData['Camera2']=="true" or CameraData['Camera3']=="true" or CameraData['Camera4']=="true"):
                if(CameraData['Camera1']=="true" and abs(time.time()-t)>15 and abs(time.time()-t)<18):
                        kit.motor1.throttle = 1
                if(CameraData['Camera2']=="true" and abs(time.time()-t)>15 and abs(time.time()-t)<18):
                        kit.motor2.throttle = 1
                if(CameraData['Camera3']=="true" and abs(time.time()-t)>15 and abs(time.time()-t)<18):
                        kit.motor3.throttle = 1
                if(CameraData['Camera4']=="true" and abs(time.time()-t)>15 and abs(time.time()-t)<18):
                        kit.motor4.throttle = 1
        elif s.value != 90001:
                kit.motor1.throttle = 0
                kit.motor2.throttle = 0
                kit.motor3.throttle = 0
                kit.motor4.throttle = 0
    print("Done",pipeline)
    pipeline.send_event(Gst.Event.new_eos())
    print("EOS")
    time.sleep(5)
    print("EndSleep")
    pipeline.set_state(Gst.State.NULL)
    print("Recordings Finished Saving")


def StartCameras(tim,tim2,Res,Frame,AssName,pipe):
    global p
    global num
    num = Value('d', 0.0)
    ti = Value('d', tim)
    ti2 = Value('d', tim2)
    pip = Value('d',pipe)
    fr = Value('d', Frame)
    print(Res)
    p = Process(target=StartCamerasFunction,args=(num,ti,ti2,pip,AssName,Res,fr))
    p.start()
    time.sleep(5)
def CancelThread():
    global p
    print(p)
    if p is not None:
        with num.get_lock():
            num.value = 1
        time.sleep(15)
        print("KillingP")
        p.kill()
        print("P_Killed")
    else:
        print("P_Not_Initialized")
    p = None
    print("Canceled")

#StartCameras(15,15,"1920x1080",5,"Testing1.0",1)