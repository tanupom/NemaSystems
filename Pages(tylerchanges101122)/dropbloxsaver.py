from multiprocessing import current_process
from multiprocessing import Process, Value, Array
import multiprocessing
import dropbox
import dropbox
import os
import shutil
import datetime
import http.client as httplib
import json
import requests
from time import sleep
import time
import cv2
import glob
from datetime import date
import pandas as pd

# from Pages.views import Currentprofiledata


def SplitVideos(s, videoFolder, wash, post, archive):
    trimPoint = (5 * s) + 25
    # Post-Process into 2 videos
    file_folder_Videos = videoFolder
    file_path = ''
    for filename in os.listdir(file_folder_Videos):
        f = os.path.join(file_folder_Videos, filename)
        if os.path.isfile(f):
            file_name = os.path.basename(f)
            file, file_extension = os.path.splitext(file_name)
            # print(file)
            # print(file_name)
            if (file_extension == '.mp4'):
                file_path = f
                vidcap = cv2.VideoCapture(file_path)
                frameSize = (3264, 1798)  # Size of the video frame
                fourcc = cv2.VideoWriter_fourcc(*'MP4V')
                TL = cv2.VideoWriter(wash+"//"+file+'.mp4',
                                     fourcc, 5, frameSize)  # makes and AVI
                TL2 = cv2.VideoWriter(
                    post+"//"+file+'.mp4', fourcc, 5, frameSize)  # makes and AVI
                success, image = vidcap.read()  # Reads an image
                count = 1  # Frame Number
                while success:
                    # cv2.imwrite("frame%d.jpg" % count, image)     # save frame as JPEG file
                    if (success):
                        print('Read a new frame: ', success)
                        print(count, "-", trimPoint)
                        if (count < trimPoint and count > 25):
                            TL2.write(image)
                        elif (count > trimPoint+25):
                            TL.write(image)
                        success, image = vidcap.read()
                        count += 1
                TL.release()
                TL2.release()
    print("VideosCreated")
    pathtofolder = videoFolder
    for filename in os.listdir(pathtofolder):
        file_path = os.path.join(pathtofolder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))


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

    # name of assay in thing_notherthing_lastthing


class TransferData:
    def __init__(self, access_token):
        self.access_token = nemakey

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)
        for file in os.listdir(file_from):
            if file.endswith(".mp4") or file.endswith(".xlsx"):
                filename = file_from + "/" + file
                with open(filename, 'rb') as f:
                    dbx.files_upload(f.read(), file_to+file)


def makedir(parentdir, nameofdir):  # makes directory
    url = "https://api.dropboxapi.com/2/files/create_folder_v2"
    headers = {
        "Authorization": "Bearer " + nemakey,
        "Content-Type": "application/json"}
    data = {"path": '/' + str(parentdir) + '/' + str(nameofdir)}
    r = requests.post(url, headers=headers, data=json.dumps(data))


def makedir2(parentdir, nameofdir, nameof2nddir):  # makes 2nd directory
    url = "https://api.dropboxapi.com/2/files/create_folder_v2"
    headers = {
        "Authorization": "Bearer " + nemakey,
        "Content-Type": "application/json"}
    data = {"path": '/Infinity System Demo/' +
            str(parentdir) + '/' + str(nameofdir) + '/' + str(nameof2nddir)}
    r = requests.post(url, headers=headers, data=json.dumps(data))


def main(nemakey, ff, ft):  # moves files over to argumented directories
    access_token = nemakey
    transferData = TransferData(access_token)

    file_from = ff
    file_to = ft  # The full path to upload the file to, including the file name

    # API v2
    transferData.upload_file(file_from, file_to)


def megarun_process_Failsafe():
    # print("StartDropboxFailsafe")
    rootdir = r"/mnt/InternamDrive/Videos/Recorded Video"
    
    
    global nemakey
    nemakey = 'O7-yGUOXuesAAAAAAAAAAUeNXA538nJriu-IOfSdU4VHaROvZjx4mWcbqNfQAC0E'
    for dir in os.listdir(rootdir):
        if dir != 'Recorded_Video':
            print("Root: ", dir)
            path2 = os.listdir(os.path.join(rootdir, dir))
            for directory in path2:
                if (directory == 'Pre-Split'):
                    washvideopath = os.path.join(os.path.join(
                        os.path.join(rootdir, dir), 'Wash'))
                    postwashvideopath = os.path.join(os.path.join(
                        os.path.join(rootdir, dir), 'Post-Wash'))
                    archivedpath = os.path.join(os.path.join(
                        os.path.join(rootdir, dir), 'Archive'))
                    presplitpath = os.path.join(os.path.join(
                        os.path.join(rootdir, dir), 'Pre-Split'))
                    Datapath = os.path.join(os.path.join(
                        os.path.join(rootdir, dir), 'Data'))
                    if not any(fname.endswith('.mp4') for fname in os.listdir(os.path.join(os.path.join(rootdir, dir), 'Pre-Split'))):
                        print("None Found")
                    else:
                        # Erase wash and Post-Wash
                        jsonpath = r"/home/infinitysystem2/Documents/Infinity2.0Django_09122022/AssayProfiles.json"
                        f = open(jsonpath)
                        data = json.load(f)
                        f.close()

                        washingtime = int(data[dir]['washingtime'])
                        SplitVideos(washingtime, presplitpath,
                                    washvideopath, postwashvideopath, archivedpath)
                        print("Splitting Videos Started")

                    if any(fname.endswith('.mp4') for fname in os.listdir(os.path.join(os.path.join(rootdir, dir), 'Archive'))) or any(fname.endswith('.mp4') for fname in os.listdir(os.path.join(os.path.join(rootdir, dir), 'Post-Wash'))) or any(fname.endswith('.mp4') for fname in os.listdir(os.path.join(os.path.join(rootdir, dir), 'Wash'))):
                        print("Create Directories")
                        current_date = datetime.date.today()
                        formatted_date = datetime.datetime.strptime(
                            str(current_date), "%Y-%m-%d").strftime('%m%d%Y')
                        makedir(dir, str(formatted_date))
                        main(nemakey, washvideopath, '/Infinity System Demo'+'/' +
                             dir+'/'+str(formatted_date)+'/'+'Wash/')
                        main(nemakey, postwashvideopath, '/Infinity System Demo'+'/' +
                             dir+'/'+str(formatted_date)+'/'+'Post-Wash/')
                        main(nemakey, archivedpath, '/Infinity System Demo'+'/' +
                             dir+'/'+str(formatted_date)+'/'+'Archive/')
                        main(nemakey, Datapath, '/Infinity System Demo'+'/' +
                             dir+'/'+str(formatted_date)+'/'+'Data/')
                        print('UploadedVideos')
                        sleep(15)
                        deleteallwithinfolder(archivedpath)
                        deleteallwithinfolder(washvideopath)
                        deleteallwithinfolder(postwashvideopath)
                        deleteallwithinfolder(presplitpath)
                       # deleteallwithinfolder(Datapath)
                        print("Upload Directories")
                    else:
                        print("Nothing to upload")
        else:
            # Archive Videos
            print("Cleaned Recorded_Video Folder")


def megarun_process():
    print("StartDropbox")
    curprofjsonpath = "/home/infinitysystem/Documents/Infinity2.0Django_09122022/Pages/currentprofile.json"
    f = open(curprofjsonpath)
    curprofprofiledata = json.load(f)
    f.close()

    curprofname = curprofprofiledata['clientcode'] + '_' + curprofprofiledata['assaycode'] + '_' + curprofprofiledata['biorep']

    washingtime = int(curprofprofiledata['washingtime'])

    nemakey = 'O7-yGUOXuesAAAAAAAAAAUeNXA538nJriu-IOfSdU4VHaROvZjx4mWcbqNfQAC0E'

    current_date = datetime.date.today()
    formatted_date = datetime.datetime.strptime(
        str(current_date), "%Y-%m-%d").strftime('%m%d%Y')

    curprofnamenestpath = '/home/infinitysystem/Documents/Infinity2.0Django_09122022/Videos/' + \
        str(curprofname) + '/'

    washvideopath = os.path.join(curprofnamenestpath, 'Wash')
    postwashvideopath = os.path.join(curprofnamenestpath, 'Post-Wash')
    archivedpath = os.path.join(curprofnamenestpath, 'Archive')
    presplitpath = os.path.join(curprofnamenestpath, 'Pre-Split')
    Datapath = os.path.join(curprofnamenestpath, 'Data')
    SplitVideos(washingtime, presplitpath, washvideopath,
                postwashvideopath, archivedpath)


    makedir(curprofname, str(formatted_date))
    print("MadeDirectory")
    main(nemakey, washvideopath, '/Infinity System Demo'+'/' +
         curprofname+'/'+str(formatted_date)+'/'+'Wash/')
    main(nemakey, postwashvideopath, '/Infinity System Demo'+'/' +
         curprofname+'/'+str(formatted_date)+'/'+'Post-Wash/')
    main(nemakey, archivedpath, '/Infinity System Demo'+'/' +
         curprofname+'/'+str(formatted_date)+'/'+'Archive/')
    main(nemakey, Datapath, '/Infinity System Demo'+'/' +
         curprofname+'/'+str(formatted_date)+'/'+'Data/')
    print('UploadedVideos')
    sleep(15)
    deleteallwithinfolder(archivedpath)
    deleteallwithinfolder(washvideopath)
    deleteallwithinfolder(postwashvideopath)
    deleteallwithinfolder(presplitpath)
   # deleteallwithinfolder(Datapath)


    

    print("DropBoxComplete")


def megarun():
    global p
    p = Process(target=megarun_process)
    p.start()
    ProcessJson = "/home/infinitysystem/Documents/Infinity2.0Django_09122022/Process.json"
    f = open(ProcessJson)
    data = json.load(f)
    newdata = {p.pid:"megarun"}
    data.update(newdata)
    f.close()
    with open(ProcessJson, "w") as w:
            json.dump(data, w, indent=4, separators=(',', ': '))
    print("Started")
   
    time.sleep(5)
    print("Done")
    


megarun_process_Failsafe()
