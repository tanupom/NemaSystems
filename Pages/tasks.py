from .PreWash_Sterilization import Prewashster
from .Stop_All_Pumps import StopAllPumps
import os
import cv2
import shutil

from Infinity.celery import app
from celery import shared_task
from Infinity.celery import app

@shared_task
def SplitVideos(s,videoFolder,wash,post,archive):
    trimPoint = (5 * s) + 25
    #Post-Process into 2 videos
    file_folder_Videos = videoFolder
    file_path = ''
    for filename in os.listdir(file_folder_Videos):
        f = os.path.join(file_folder_Videos,filename)
        if os.path.isfile(f):
            file_name = os.path.basename(f)
            file, file_extension = os.path.splitext(file_name)
            #print(file)
            #print(file_name)
            if(file_extension=='.mp4'):
                file_path = f
                vidcap = cv2.VideoCapture(file_path)
                frameSize = (3264, 2448)#Size of the video frame
                fourcc = cv2.VideoWriter_fourcc(*'MP4V')
                TL = cv2.VideoWriter(wash+"//"+file+'.mp4',fourcc, 5, frameSize)#makes and AVI
                TL2 = cv2.VideoWriter(post+"//"+file+'.mp4',fourcc, 5, frameSize)#makes and AVI
                success,image = vidcap.read()#Reads an image 
                count = 1#Frame Number
                while success:
                    #cv2.imwrite("frame%d.jpg" % count, image)     # save frame as JPEG file      
                    if(success):
                        print('Read a new frame: ', success)
                        print(count,"-",trimPoint)
                        if(count<trimPoint and count > 25):
                            TL2.write(image)
                        elif(count>trimPoint+25):
                            TL.write(image)
                        success,image = vidcap.read()
                        count += 1
                TL.release()
                TL2.release()
    print("VideosCreated")
    pathtofolder = '/home/infinitysystem/Documents/Infinity2.0Django_09122022/Videos/Recorded_Video'
    for filename in os.listdir(pathtofolder):
        file_path = os.path.join(pathtofolder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))



@shared_task
def stoppa():
    StopAllPumps()