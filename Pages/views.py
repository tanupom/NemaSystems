from ast import Div
from cmath import nan
from http.client import HTTPResponse
import profile
from tkinter import CENTER
from .GSTCameraCode import CancelThread
from .GSTCameraCode import StartCameras
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from .PostWash_Sterilization import Postwashster
from .PreWash_Sterilization import Prewashster
from .Custom_Sterilization import Customwashster
from .Stop_All_Pumps import StopAllPumps
from .Stop_All_Pumps_1 import StopPumpNumber
from .Start_All_Pumps_1 import StartPumpNumber
from .models import ToDoList, Item
from .uploadsfiles import Uploadallfiles
import json
from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model, logout
from django.db import models
from django.contrib import auth
from django.urls import reverse
from django.contrib.auth.models import User
import os
from datetime import datetime, timedelta
from .cleanjsondata import cleanjson
from .dropbloxsaver import megarun
from .dropbloxsaver import megarun_process_Failsafe
from .tasks import stoppa
from .forms import UploadFileForm
import time
from django.core.files.storage import FileSystemStorage
from .forms import DocumentForm
import shutil
import pandas as pd
from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages
from datetime import date, datetime
import fnmatch

def check_pid(pid):
    """ Check For the existence of a unix pid. """
    try:
        os.kill(pid, 0)
    except OSError:
        return False
    else:
        return True
def strtosec(timestr):
    print(timestr, "ARR")
    print(type(timestr))
    # return(int(timestr))
    seconds = 0
    hour = 0
    min = 0
    str(timestr)
    timearr = timestr.split(':')
    try:
        if (timearr[0] != ''):
            hour = 60 * 60 * int(timearr[0])
    except:
        hour = 0
        print("Error1", hour)
    try:
        if (timearr[1] != ''):
            min = 60 * int(timearr[1])
    except:
        min = 60
        print("Error2")
    try:
        if (timearr[2] != ''):

            seconds = int(timearr[2])
    except:
        seconds = 30
        print("Error3")
    return hour + min + seconds


def register(response, request):
    username = request.POST['username']
    print(username)
    return render(response, "Pages/home.html", {})


def index(response, id):
    ls = ToDoList.objects.get(id=id)
    return render(response, "Pages/list.html", {"ls": ls})


def home(response):
    return render(response, "Pages/home.html", {})


jsonpath = r"/home/jetson/Documents/Infinity2.0Django_09122022/AssayProfiles.json"
f = open(jsonpath)
global profiledata
profiledata = json.load(f)
f.close()

CurrentProfilejsonpath = r"/home/jetson/Documents/Infinity2.0Django_09122022/Pages/currentprofile.json"
f = open(CurrentProfilejsonpath)
global Currentprofiledata
Currentprofiledata = json.load(f)
f.close()


def updateJson():
    global profiledata
    f = open(jsonpath)
    profiledata = json.load(f)
    f.close()


def CurrentProfileupdateJson():
    global profiledata
    f = open(CurrentProfilejsonpath)
    Currentprofiledata = json.load(f)
    f.close()


def MainMenu_view(request, *args, **kwargs):
    global number_of_active_presplit_videos
    print(request.POST)
    print("Here")
    if ((request.method == 'POST' and 'run_script' in request.POST)):

        if request.user.is_authenticated:
            userss = {"user": request.user.username}
            usersss = {"Puser": userss,
                       }

        datas = {
            "profiles": profiledata,
}
        #from Custom_Sterilization import function_to_run
        return render(request, "MainMenu.html", datas)

    elif ((request.method == 'POST' and 'StopOne' in request.POST)):
        print("Stop1")
        StopPumpNumber(1)
        datas = {
            "profiles": profiledata,
        }
        render(request, "MainMenu.html", datas)
    elif ((request.method == 'POST' and 'StartOne' in request.POST)):
        print("Start1")
        StartPumpNumber(1)
        datas = {
            "profiles": profiledata,
        }
        render(request, "MainMenu.html", datas)
    elif ((request.method == 'POST' and 'StopTwo' in request.POST)):
        print("Stop2")
        StopPumpNumber(2)
        datas = {
            "profiles": profiledata,
        }
        render(request, "MainMenu.html", datas)
    elif ((request.method == 'POST' and 'StartTwo' in request.POST)):
        print("Start2")
        StartPumpNumber(2)
        datas = {
            "profiles": profiledata,
        }
        render(request, "MainMenu.html", datas)
    elif ((request.method == 'POST' and 'StopThree' in request.POST)):
        print("Stop3")
        StopPumpNumber(3)
        datas = {
            "profiles": profiledata,
        }
        render(request, "MainMenu.html", datas)
    elif ((request.method == 'POST' and 'StartThree' in request.POST)):
        print("Start3")
        StartPumpNumber(3)
        datas = {
            "profiles": profiledata,
        }
        render(request, "MainMenu.html", datas)
    elif ((request.method == 'POST' and 'StopFour' in request.POST)):
        print("Stop4")
        StopPumpNumber(4)
        datas = {
            "profiles": profiledata,
        }
        render(request, "MainMenu.html", datas)
    elif ((request.method == 'POST' and 'StartFour' in request.POST)):
        print("Start4")
        StartPumpNumber(4)
        datas = {
            "profiles": profiledata,
        }
        render(request, "MainMenu.html", datas)
    elif ((request.method == 'POST' and 'StartPumps' in request.POST)):
        foti = str((request.POST.get('Ti')))
        Customwashster(foti)
        datas = {
            "profiles": profiledata,
        }
        render(request, "MainMenu.html", datas)
    elif ((request.method == 'POST' and 'StopPumps' in request.POST)):
        StopAllPumps()
        datas = {
            "profiles": profiledata,
        }
        render(request, "MainMenu.html", datas)
    elif ((request.method == 'POST' and 'run_script_cam' in request.POST)):
        CancelThread()
        try:
            curprofjsonpath = "/home/jetson/Documents/Infinity2.0Django_09122022/Pages/currentprofile.json"
            if request.user.is_authenticated:
                userss = {"user": request.user.username}
                usersss = {"Puser": userss,
                        }

            datas = {
                "profiles": profiledata,
            }
            f = open(curprofjsonpath)
            curprofprofiledata = json.load(f)
            f.close()
            curprofname = curprofprofiledata['clientcode'] + '_' + \
                curprofprofiledata['assaycode'] + \
                '_' + curprofprofiledata['biorep']
            nikeshopen = open("/home/jetson/Documents/Infinity2.0Django_09122022/AssayLog4Chips.json")
            df = pd.DataFrame.from_dict(json.load(nikeshopen),orient="index")
            df = df.replace("true", u'\u2713')
            df = df.replace("false", nan)
            today = str(date.today())
            dailyexceldst = '/mnt/InternamDrive/Videos/' + str(curprofname) + '/' + 'Data' + '/'
            dailyexcelsrc = r'/home/jetson/Documents/Infinity2.0Django_09122022/Pages/AssayLogOverviewTemplatee.xlsx'
            excelfilenamecheckifexists = dailyexceldst + curprofname + '_' + today + '.xlsx' #remove extra underscore when done with testing
            #check if file exists, if it does not, start uploading it with certain criteria.
            checkiffileexists = os.path.isfile(excelfilenamecheckifexists)
            if checkiffileexists == True:
                pass
            else:
                #step 1 copy file from dst to src
                nameofblankexcelfile = 'AssayLogOverviewTemplatee.xlsx'
                shutil.copy(dailyexcelsrc, dailyexceldst)

                #step 2 rename new file with curprofname and the date
                old_name = dailyexceldst + nameofblankexcelfile
                new_name = dailyexceldst + curprofname + '_' + today + '.xlsx'
                os.rename(old_name, new_name)
                dynamic_new_excel_name = new_name
                Detailedexcelpath = r'/home/jetson/Documents/Infinity2.0Django_09122022/media/' + curprofname + '.xlsx'
                detaileddf = pd.read_excel(Detailedexcelpath, index=False, sheet_name='General Metadata Structure')
                data = {'col1': curprofprofiledata.keys(), 'col2': curprofprofiledata.values()}
                dataframe = pd.DataFrame.from_dict(data, orient="index").T
                #matt code to get assay start time
                starttimejsonpath = '/home/jetson/Documents/Infinity2.0Django_09122022/Pages/starttime.json'
                l = open(starttimejsonpath)
                starttime = json.load(l)
                with pd.ExcelWriter(dynamic_new_excel_name, engine="openpyxl") as writer:
                    detaileddf.to_excel(writer, sheet_name='Detailed Project Overview')
                    dataframe.to_excel(writer, sheet_name='Summarized_Project_Overview')
                    df.to_excel(writer, sheet_name='Assay Log')
                    try:
                        k = datetime.now()
                        detaileddf = pd.read_excel(Detailedexcelpath, index=False, sheet_name='General Metadata Structure')
                        assaylogdf = pd.read_excel(dailyexcelsrc, index=False,sheet_name='Assay Logg')
                        time.sleep(2)

                    except:
                        print("Assay Log Failure")


            
            megarun()
            # psutil.pid_exists(pid)
        except:
            print("Failed")
        return render(request, "MainMenu.html", datas)
    elif ((request.method == 'POST' and 'Go_to_Live_View' in request.POST)):

        if request.user.is_authenticated:
            userss = {"user": request.user.username}
            usersss = {"Puser": userss,
                       }

        datas = {
            "profiles": profiledata,
        }
        StartCameras(90001, 90001, '1920x1080', 5, 'Live', 2)
        return render(request, "LiveFeed.html", datas)
    elif ((request.method == 'POST' and 'End_Live' in request.POST)):

        if request.user.is_authenticated:
            userss = {"user": request.user.username}
            usersss = {"Puser": userss,
                       }

        datas = {
            "profiles": profiledata,
        }
        CancelThread()
        StopAllPumps()
        return render(request, "MainMenu.html", datas)

    elif (request.method == 'POST' and 'button_to_upload_excel' in request.POST):
        try:
            myfile = str(request.FILES['myfile'])
            excelpath = '/home/jetson/Documents/Infinity2.0Django_09122022/media/' + myfile
           # renamedPath = '/home/infinitysystem/Documents/Infinity2.0Django_09122022/media/' +
            os.rename(excelpath,)

            dataframes = pd.read_excel(
                excelpath, sheet_name='General Metadata Structure', header=1)
            d = 20
            usersss = {'thingg': d
                       }
            mediapath = '/home/jetson/Documents/Infinity2.0Django_09122022/media'
            myfile = request.FILES['myfile']
            myfilepath = mediapath + '/' + str(myfile)
            fs = FileSystemStorage()

            if os.path.isfile(myfilepath):
                curexcel = myfile
                print('i already exist')
            else:
                print('i have made it here')
                filename = fs.save(myfile.name, myfile)
                uploaded_file_url = fs.url(filename)
                curexcel = myfile
                excelprofilesjsonpath = "/home/jetson/Documents/Infinity2.0Django_09122022/Pages/allexcelprofiles.json"
                l = open(excelprofilesjsonpath)
                allexcelprofiles = json.load(l)
                uploadedexcelfilename = {
                    str(myfilepath): 'uploaded excel file'}

                with open(excelprofilesjsonpath, "w") as w:
                    json.dump(uploadedexcelfilename, w, sort_keys=True,
                              indent=4, separators=(',', ': '))
                allexcelprofiles.update(uploadedexcelfilename)
                l.close()

        except:

            return render(request, 'newassayimport.html', {})

    elif (request.method == 'POST' and 'savefile/upload' in request.POST):
        print('im here')
#        try:
        jsonpath = r"/home/jetson/Documents/Infinity2.0Django_09122022/AssayProfiles.json"
        print(request.POST.get('txtmovielength'))
        Profiles = {
            request.POST.get('txtclientcode') + "_" + str((request.POST.get('txtassaycode'))) + "_" + str((request.POST.get('txtbiorep'))): {
                "clientcode": str((request.POST.get('txtclientcode'))),
                "assaycode": str((request.POST.get('txtassaycode'))),
                "substratetype": str((request.POST.get('txtsubstratetype'))),
                "biorep": str((request.POST.get('txtbiorep'))),
                "loaddate": str((request.POST.get('txtLoaddate'))),
                "temperature": str((request.POST.get('txttemperature'))),
                "media": str((request.POST.get('txtmedia'))),
                "bacteria": str((request.POST.get('txtbacteria'))),
                "technicalreplicate": str((request.POST.get('txttechnicalreplicate'))),
                "operator": str((request.POST.get('txtoperator'))),
                "chips": str((request.POST.get('txtchips'))),
                "enddate": str((request.POST.get('txtenddate'))),
                "washingtime": strtosec(((request.POST.get('txtwashingtime')))),
                "resolution": str((request.POST.get('txtresolution'))),
                "framerate": str((request.POST.get('txtframerate'))),
                "movielength": strtosec(request.POST.get('txtmovielength')),
                "sessionlength": str((request.POST.get('txtsessionlength'))),
                "numberofsessions": str((request.POST.get('txtnumberofsessions'))),
                "tltimeinterval": strtosec(((request.POST.get('tltimeinterval')))),
                "tltresolution": str((request.POST.get('tlresolution'))),
                "tltsessionlength": str((request.POST.get('tlmovielength'))),
                "tltplaybackspeed": str((request.POST.get('tlplaybackspeed'))),
            }
        }
        f = open(jsonpath)
        data = json.load(f)
        data.update(Profiles)
        f.close()
        with open(jsonpath, "w") as w:
            json.dump(data, w, indent=4, separators=(',', ': '))
        updateJson()
        mediapath = r'/home/jetson/Documents/Infinity2.0Django_09122022/media'
        myfile = request.FILES['myfile']
        myfilepath = mediapath + '/' + str(myfile)
        fs = FileSystemStorage()
        if os.path.isfile(myfilepath):
            pass
        else:
            excelfilename = fs.save(myfile.name, myfile)
            curexcel = str(myfile)
            print(str(curexcel))

        newFileName = mediapath + '/' + str((request.POST.get('txtclientcode'))) + '_' + str(
            (request.POST.get('txtassaycode'))) + '_' + str((request.POST.get('txtbiorep'))) + ".xlsx"
        os.rename(myfilepath, newFileName)
        return render(request, 'MainMenu.html', {})

    elif (request.method == 'POST' and 'Go_to_new_assay' in request.POST):

        # print(request.POST['username'])
        #print("new assay is being created")

        if request.user.is_authenticated:
            userss = {"user": request.user.username}
            usersss = {"Puser": userss}
        else:
            userss = {"user": "Unknown"}

        return render(request, "NewAssay.html", usersss)

    elif (request.method == 'POST' and 'Go_to_new_assayimport' in request.POST):
       # print(request.POST['username'])
        print("new assay is being created")

        if request.user.is_authenticated:
            userss = {"user": '30'}
            usersss = {"Puser": userss,
                       "thing": 30}
        else:
            userss = {"user": "Unknown"}

        return render(request, "newassayimport.html", usersss)

    elif (request.method == 'POST' and 'Logoutfunction' in request.POST):
       # print(request.POST['username'])
        #print("new assay is being created")

        logout(request)
        return HttpResponseRedirect('/')

    elif (request.method == 'POST' and 'Go_to_sys_ster' in request.POST):
        if request.user.is_authenticated:
            userss = {"user": request.user.username}
            usersss = {"Puser": userss}
        else:
            userss = {"user": "Unknown"}
        return render(request, "SystemSterilization.html", usersss)

    elif (request.method == 'POST' and 'Go_to_pre_ster' in request.POST):
        return render(request, "presterilization.html", {})
    elif (request.method == 'POST' and 'Go_to_post_ster' in request.POST):
        return render(request, "poststerilization.html", {})

    elif (request.method == 'POST' and 'Pre_Sterilization2' in request.POST):
        Prewashster()
        return render(request, "presterilizationgreen2.html", {})

    elif (request.method == 'POST' and 'Pre_Sterilization1' in request.POST):
        Prewashster()
        return render(request, "presterilizationgreen1.html", {})

    elif (request.method == 'POST' and 'Post_Sterilization' in request.POST):
        Postwashster()
        return render(request, "poststerilization.html", {})
    elif (request.method == 'POST' and 'Stop_All_Pumpspre' in request.POST):
        print('i am stopping')
        StopAllPumps()
        return render(request, "presterilization.html", {})
    elif (request.method == 'POST' and 'Stop_All_Pumpspre1' in request.POST):
        print('i am stopping')
        StopAllPumps()
        return render(request, "presterilizationgreen1.html", {})
    elif (request.method == 'POST' and 'Stop_All_Pumpspre2' in request.POST):
        print('i am stopping')
        StopAllPumps()
        return render(request, "presterilization.html", {})
    elif (request.method == 'POST' and 'Stop_All_Pumpspost' in request.POST):
        StopAllPumps()
        return render(request, "poststerilization.html", {})
    elif (request.method == 'POST' and 'Stop_All_Pumpspost2' in request.POST):
        StopAllPumps()
        return render(request, "poststerilizationgreen1.html", {})
    elif (request.method == 'POST' and 'Stop_All_Pumpspost3' in request.POST):
        StopAllPumps()
        return render(request, "poststerilizationgreen2.html", {})
    elif (request.method == 'POST' and 'Post_Sterilization1' in request.POST):
        Postwashster()
        return render(request, "poststerilizationgreen1.html", {})
    elif (request.method == 'POST' and 'Post_Sterilization2' in request.POST):
        Postwashster()
        return render(request, "poststerilizationgreen2.html", {})
    elif (request.method == 'POST' and 'Go_Back_to_login' in request.POST):
        return render(request, "Login.html", {})
    elif (request.method == 'POST' and 'Go_to_existingassayexcel' in request.POST):
        if request.user.is_authenticated:
            userss = {"user": request.user.username, }
            usersss = {"Puser": userss}
        else:
            userss = {"user": "Unknown"}

        assaynames = {}
        x = 0
        for i in profiledata.keys():
            x += 1
            assaynames[i] = x
        f = open(CurrentProfilejsonpath)
        data = json.load(f)

        headername = str(data['clientcode'] + '_' +
                         data['assaycode'] + '_' + data['biorep'])
        print('i am here')
        print('i made it here')

        # rename excel file to headername

        # try:
        pathforfilenameofselectedexcel = headername
        print(headername)
        pathforcurrentprofileexceldatainmediafolder = "/home/jetson/Documents/Infinity2.0Django_09122022/media/" + headername + ".xlsx"
        # os.rename(pathforfilenameofselectedexcel,pathforcurrentprofileexceldatainmediafolder)

        print('i updated excel')
        # except Exception as e:
        #     print(e)
        #     print('i broke')
        #     pass


        cleanjson()
        # updateJson()
        datas = {
            "profiles": profiledata,
            "assaynames": assaynames,
            "CurrentProfile": data,
            "puser": userss,
        }
        return render(request, "ExistingAssayExcel.html", datas)

    elif ((request.method == 'POST' and 'Go_to_existing_assay' in request.POST)) or 'sortby' in request.POST:

        try:
            curprof = profiledata[request.POST.get('sortby')]
        except:
            curprof = profiledata['---_---_---']

        if request.user.is_authenticated:
            userss = {"user": request.user.username, }
            usersss = {"Puser": userss}
        else:
            userss = {"user": "Unknown"}

        assaynames = {}
        x = 0
        for i in profiledata.keys():
            x += 1
            assaynames[i] = x
        f = open(CurrentProfilejsonpath)
        data = json.load(f)
        data.update(curprof)
        global headernamemega
        headernamemega = str(data['clientcode'] + '_' +
                         data['assaycode'] + '_' + data['biorep'])
        print('i am here')
        print('i made it here')

        # rename excel file to headername

        # try:
        pathforfilenameofselectedexcel = headernamemega #/mnt/InternamDrive/media/---_---_---.xlsx
        pathforcurrentprofileexceldatainmediafolder = "/home/jetson/Documents/Infinity2.0Django_09122022/media/" + headernamemega + ".xlsx"
        # os.rename(pathforfilenameofselectedexcel,pathforcurrentprofileexceldatainmediafolder)
        print('brohemian rhapsody')
        df = pd.read_excel(pathforcurrentprofileexceldatainmediafolder,
                           sheet_name='General Metadata Structure')
        readexcelsheet = pd.DataFrame(df)
        htmlresult = readexcelsheet.to_html(col_space=150, justify='center')
        function_to_open_html_file = open(
            r'/home/jetson/Documents/Infinity2.0Django_09122022/Templates/Currentexcelprofile.html', 'w')
        function_to_open_html_file.write('')
        function_to_open_html_file.write(
            '<html>\n<head>\n</head>\n<body>\n<div>\n' + htmlresult + '\n' + '</div>\n</body>\n</html>')
        function_to_open_html_file.close()
        with open(CurrentProfilejsonpath, "w") as w:
            json.dump(data, w, sort_keys=True,
                      indent=4, separators=(',', ': '))
        CurrentProfileupdateJson()
        f.close()

        # pandas obtain all chip id numbers
        currentprofilechipidsjsonpath = '/home/jetson/Documents/Infinity2.0Django_09122022/Pages/CurrentprofilechipIDs.json'
        chipidfile = open(currentprofilechipidsjsonpath)
        #data2 = json.load(chipidfile)
        chipIDdataframe = pd.read_excel(pathforcurrentprofileexceldatainmediafolder,
                                        sheet_name='General Metadata Structure')
        substrateidcolumn = chipIDdataframe['Substrate ID']
        chipidfile.close()
        global chips
        chips = {}
        x = 0
        for id in substrateidcolumn:
            chips[id] = 1
            x = x + 1
            print(chips)
        print("Printing")
        filenameJson = "/home/jetson/Documents/Infinity2.0Django_09122022/AssayLog4Chips.json"
        with open(filenameJson, "w") as write:
            json.dump({}, write, indent=4, separators=(',', ': '))

        with open(currentprofilechipidsjsonpath, "w") as w:
            json.dump(chips, w, indent=4, separators=(',', ': '))


        try: number_of_active_presplit_videos
        except NameError: number_of_active_presplit_videos = 0
        
        datas = {
            "profiles": profiledata,
            "assaynames": assaynames,
            "CurrentProfile": data,
            "puser": userss,
            "ChipIds": chips,
            "headername": headernamemega,
            "Numberofvideostoupload": number_of_active_presplit_videos
        }
        global globaldatas
        globaldatas = datas
        nikeshopen = open("/home/jetson/Documents/Infinity2.0Django_09122022/AssayLog4Chips.json")
#        with open(nikeshopen, "w") as w:
        #    json.dump({}, w, sort_keys=True,
          #          indent=4, separators=(',', ': '))



        return render(request, "ExistingAssay.html", datas)

    elif ((request.method == 'POST' and 'Go_to_existing_assaysummarized' in request.POST)):

        f = open(CurrentProfilejsonpath)
        data = json.load(f)

        try:
            headername = str(data['clientcode'] + '_' +
                             data['assaycode'] + '_' + data['biorep'])
            curprof = profiledata[request.POST.get('sortby')]
            print('i made it here')
        except:
            print('i made it here 2')
            curprof = profiledata['---_---_---']
            headername = '---_---_---'

        pathforfilenameofselectedexcel = headername
        print(headername)
        pathforcurrentprofileexceldatainmediafolder = "/home/jetson/Documents/Infinity2.0Django_09122022/media/" + headername + ".xlsx"

        print('i updated excel')

        if request.user.is_authenticated:
            userss = {"user": request.user.username,
                      "header": headername}
            usersss = {"Puser": userss}
        else:
            userss = {"user": "Unknown"}

        assaynames = {}
        x = 0
        for i in profiledata.keys():
            x += 1
            assaynames[i] = x
        f = open(CurrentProfilejsonpath)
        data = json.load(f)

        f.close()

        f = open(CurrentProfilejsonpath)

        datas = {
            "profiles": profiledata,
            "assaynames": assaynames,
            "CurrentProfile": data,
            "puser": userss,
            "headername": headernamemega
        }

        return render(request, "ExistingAssay.html", globaldatas)

    elif (request.method == 'POST' and 'Pre_Sterilization' in request.POST):
        Prewashster()
        return render(request, "presterilization.html", {})
    elif (request.method == 'POST' and 'Post_Sterilization' in request.POST):
        print('thing')
        # Postwashster()
        return render(request, "SystemSterilization.html", {})

    elif (request.method == 'POST' and 'Custom_Sterilization' in request.POST):
        # Customwashster(request.POST.get('FormatedTime'))
        return render(request, "customsterilization.html", {})

    elif (request.method == 'POST' and 'Custom_Sterilization2' in request.POST):
        try:

            formattime = request.POST.get('FormatedTime')
            print(formattime)
            Customwashster(formattime)
        except:
            print()
        return render(request, "customsterilization2.html", {})

    elif (request.method == 'POST' and 'movetoggledvideos' in request.POST):
        curprofjsonpath = "/home/jetson/Documents/Infinity2.0Django_09122022/Pages/currentprofile.json"
        f = open(curprofjsonpath)
        curprofprofiledata = json.load(f)
        f.close()
        s = open(CurrentProfilejsonpath)
        data = json.load(s)

        curprofname = curprofprofiledata['clientcode'] + '_' + \
            curprofprofiledata['assaycode'] + \
            '_' + curprofprofiledata['biorep']
        videopath = '/mnt/InternamDrive/Videos/'
        curprofnamenestpath = '/mnt/InternamDrive/Videos/' + str(curprofname) + '/'
        try:
            path = os.path.join(videopath, curprofname)
            os.mkdir(path)
        except:
            pass
        # if(curprofprofiledata['tltimeinterval']=="Choose..." or curprofprofiledata['tltimeinterval']=="---"):
        if (True):
            try:
                path = os.path.join(curprofnamenestpath, 'Pre-Split')
                os.mkdir(path)
            except:
                pass
            try:
                path = os.path.join(curprofnamenestpath, 'Post-Wash')
                os.mkdir(path)
            except:
                pass
            try:
                path = os.path.join(curprofnamenestpath, 'Wash')
                os.mkdir(path)
            except:
                pass
            try:
                path = os.path.join(curprofnamenestpath, 'Archive')
                os.mkdir(path)
            except:
                pass
            try:
                path = os.path.join(curprofnamenestpath, 'Data')
                os.mkdir(path)
            except:
                pass
            print(str((request.POST.get('movie1'))))
            print(str((request.POST.get('movie2'))))
            print(str((request.POST.get('movie3'))))
            print(str((request.POST.get('movie4'))))
            for filename in os.listdir("/mnt/InternamDrive/Videos/Recorded_Video"):
                f = os.path.join(
                    "/mnt/InternamDrive/Videos/Recorded_Video", filename)
                if os.path.isfile(f):
                    if (str((request.POST.get('movie1'))) == "on" and "Cam1" in filename):
                        print("Moving Movie1")
                        shutil.move(f, os.path.join(
                            curprofnamenestpath, 'Pre-Split'))
                    elif (str((request.POST.get('movie2'))) == "on" and "Cam2" in filename):
                        print("Moving Movie2")
                        shutil.move(f, os.path.join(
                            curprofnamenestpath, 'Pre-Split'))
                    elif (str((request.POST.get('movie3'))) == "on" and "Cam3" in filename):
                        print("Moving Movie3")
                        shutil.move(f, os.path.join(
                            curprofnamenestpath, 'Pre-Split'))
                    elif (str((request.POST.get('movie4'))) == "on" and "Cam4" in filename):
                        print("Moving Movie4")
                        shutil.move(f, os.path.join(
                            curprofnamenestpath, 'Pre-Split'))
                    else:
                        shutil.move(f, os.path.join(
                            curprofnamenestpath, 'Archive'))
        else:

            try:
                path = os.path.join(curprofnamenestpath, 'Pre-Split-Timelapse')
                os.mkdir(path)
            except:
                pass
            try:
                path = os.path.join(curprofnamenestpath, 'Archive-Timelapse')
                os.mkdir(path)
            except:
                pass

        # CancelThread()
        StartCameras(90001, 90001, '1920x1080', 5, 'Live', 2)

        #matt. Code for number of videos in presplit counter that will go into end session modal 10/7/22
        try:
            currentheadername = curprofname
            path_to_presplit_videos = r'/mnt/InternamDrive/Videos/' + currentheadername + '/' + 'Pre-Split'
          #  global number_of_active_presplit_videos
            number_of_active_presplit_videos = len(fnmatch.filter(os.listdir(path_to_presplit_videos), '*.mp4'))
            print(number_of_active_presplit_videos)
        except:
            print("exception:",number_of_active_presplit_videos)

        datas = {
            "profiles": curprofprofiledata,
            "ChipIds": chips,
            "headername": headernamemega,
            "CurrentProfile" : data,
            "Numberofvideostoupload": number_of_active_presplit_videos
        }


        return render(request, "RunningAssayLive.html", datas)


    # function to save all videos, should change to take in arguments later
    elif (request.method == 'POST' and 'uploadallvideos' in request.POST):
        curprofjsonpath = "/home/jetson/Documents/Infinity2.0Django_09122022/Pages/currentprofile.json"
        f = open(curprofjsonpath)
        curprofprofiledata = json.load(f)
        f.close()
        curprofname = curprofprofiledata['clientcode'] + '_' + \
            curprofprofiledata['assaycode'] + \
            '_' + curprofprofiledata['biorep']

        userss = {"user": request.user.username}
        datas = {"Puser": userss,
                 "CurrentProfile": curprofprofiledata,
                 "headername": headernamemega,
                 "Numberofvideostoupload": number_of_active_presplit_videos}
        # megarun()
        return render(request, "RunningAssayLive.html", datas)

    elif (request.method == 'POST' and 'Running_Assay' in request.POST):

        curprofjsonpath = "/home/jetson/Documents/Infinity2.0Django_09122022/Pages/currentprofile.json"
        f = open(curprofjsonpath)
        curprofprofiledata = json.load(f)
        f.close()
        f = open(CurrentProfilejsonpath)
        data = json.load(f)
        # data.update(curprof)
        with open(CurrentProfilejsonpath, "w") as w:
            json.dump(data, w)
        CurrentProfileupdateJson()
        f.close()
        curprofname = curprofprofiledata['clientcode'] + '_' + \
            curprofprofiledata['assaycode'] + \
            '_' + curprofprofiledata['biorep']
        #matt code to add start time to json file
        starttimejsonpath = '/home/jetson/Documents/Infinity2.0Django_09122022/Pages/starttime.json'
        now1 = datetime.now()

        current_time = {1: now1.strftime("%H:%M:%S")}
        with open(starttimejsonpath, "w") as l:
            json.dump(current_time, l)




#/mnt/InternamDrive/media/---_---_---.xlsx
        userss = {"user": request.user.username}
        datas = {"Puser": userss,
                 "CurrentProfile": data,
                 "CurrentProfilesss": data,
                 "ChipIds": chips,
                 "headername": headernamemega,
                 "Numberofvideostoupload": number_of_active_presplit_videos}

        StartCameras(90001, 90001, '1920x1080', 5, 'Live', 2)
        time.sleep(5)

        

        return render(request, "RunningAssayLive.html", datas)

    elif (request.method == 'POST' and 'Stop_All_Pumps' in request.POST):
        StopAllPumps()
        return render(request, "SystemSterilization.html", {})

    elif (request.method == 'POST' and 'Stop_All_Pumps2' in request.POST):
        StopAllPumps()
        return render(request, "customsterilization2.html", {})

    elif (request.method == 'POST' and 'System_Shutdown' in request.POST):
        ProcessJson = "/home/jetson/Documents/Infinity2.0Django_09122022/Process.json"
        f = open(ProcessJson)
        Processdata = json.load(f)
        f.close()
        while True:
            x = 0
            for key in Processdata:
                if (key != 'null'):
                    if (check_pid(int(key))):  # process is alive
                        x = x+1
                        print(key)
                        time.sleep(1)
            if (x == 0):
                break
            else:
                print("Processes Remaining: ", x)
        megarun_process_Failsafe()
        os.system("shutdown now -h")
        return render(request, "registration/login.html", {})

    elif (request.method == 'POST' and 'Logout' in request.POST):
        # os.system("shutdown now -h")
        return render(request, "registration/login.html", {})

    elif (request.method == 'POST' and 'createnewuser' in request.POST):

        def register_request(request):
            if request.method == "POST":
                form = NewUserForm(request.POST)
                if form.is_valid():
                    user = form.save()
                    login(request, user)
                    messages.success(request, "Registration successful.")
                    return redirect("main:homepage")
                messages.error(
                    request, "Unsuccessful registration. Invalid information.")
            form = NewUserForm()
            return render(request=request, template_name="registration/login.html", context={"register_form": form})

    elif (request.method == 'POST' and 'Save_all_files_to_db' in request.POST):
        # code to run assay
        return render(request, "RunningAssayLive.html", {})
    elif (request.method == 'POST' and 'startlivefeed' in request.POST):
        curprofjsonpath = "/home/jetson/Documents/Infinity2.0Django_09122022/Pages/currentprofile.json"
        f = open(curprofjsonpath)
        curprofprofiledata = json.load(f)
        f.close()
        AssayName = curprofprofiledata['clientcode'] + "_" + \
            curprofprofiledata['assaycode'] + \
            "_" + curprofprofiledata['biorep']
        datas = {
            "CurrentProfile": curprof,
            "timeuser": strpassingtime,
            "headername": headernamemega,
            "Numberofvideostoupload": number_of_active_presplit_videos}
        CancelThread()
        StartCameras(90001, 90001, '1920x1080', 5, 'Live', 2)
        time.sleep(5)
        return render(request, "RunningAssayLive.html", datas)

    elif (request.method == 'POST' and 'tcameras' in request.POST):
       # print(curprof,"Hello")
        curprofjsonpath = "/home/jetson/Documents/Infinity2.0Django_09122022/Pages/currentprofile.json"
        f = open(curprofjsonpath)
        curprofprofiledata = json.load(f)
        f.close()
        movielength = int(curprofprofiledata['movielength'])
        washinglength = int(curprofprofiledata['washingtime'])
        passinglength = movielength + washinglength + 25
        Resolution = (curprofprofiledata['resolution'])
        print(curprofprofiledata['resolution'])

        AssayName = curprofprofiledata['clientcode'] + "-" + \
            curprofprofiledata['assaycode'] + \
            "-" + curprofprofiledata['biorep']
        strpassingtime = str(passinglength+25)
        CamerasSelected = "/home/jetson/Documents/Infinity2.0Django_09122022/SelectedCameras.json"
        f = open(CamerasSelected)
        CameraData = json.load(f)
        f.close()
        ChipsSelected = "/home/jetson/Documents/Infinity2.0Django_09122022/CurrentFourChips.json"
        f2 = open(ChipsSelected)
        ChipsData = json.load(f2)
        f2.close()
        datas = {
            "CurrentProfile": curprofprofiledata,
            "timeuser": strpassingtime,
            "WashTime": str(washinglength),
            "CameraData": CameraData,
            "ChipsData": ChipsData,
            "headername": headernamemega}
        CancelThread()
       # if(curprofprofiledata['tltimeinterval']=="Choose..." or curprofprofiledata['tltimeinterval']=="---"):
        if (True):
            Framerate = int(curprofprofiledata['framerate'])
            StartCameras(washinglength, movielength,
                         Resolution, Framerate, AssayName, 1)
        else:
            Resolution = (curprofprofiledata['tltresolution'])
            movielength = int(curprofprofiledata['movielength'])
            #washinglength = 0
            Framerate = 1/int(curprofprofiledata['tltimeinterval'])
            StartCameras(washinglength, movielength,
                         Resolution, Framerate, AssayName, 0)
        time.sleep(5)
        return render(request, "RunningAssay.html", datas)
    elif (request.method == 'POST' and 'Rewashed' in request.POST):  # rename to camera1
        ChipsSelected = "/home/jetson/Documents/Infinity2.0Django_09122022/CurrentFourChips.json"
        f2 = open(ChipsSelected)
        ChipsData = json.load(f2)
        f2.close()
        #matt code to add start time to json file
        starttimejsonpath = '/home/jetson/Documents/Infinity2.0Django_09122022/starttime.json'
        l = open(starttimejsonpath)
        starttime = json.load(l)
        k = datetime.now()
        starttimee = {'Assay Start Time': str(starttime['1']), 'Assay End Time': str(k.time())}

        Chip1 = {ChipsData['Ch1']:{
                "Rewashed": str((request.POST.get('Rewashed'))),
               "Progeny": str((request.POST.get('Progeny'))),
               "Debonded": str((request.POST.get('Debonded'))),
               "Finished": str((request.POST.get('Finished'))),
               "Issues": str((request.POST.get('Issues1'))),
               "Assay Start Time": str(starttime['1']),
               "Assay End Time": str(k.time())}}
        Chip2 = {ChipsData['Ch2']:{
                "Rewashed": str((request.POST.get('Rewashed2'))),
               "Progeny": str((request.POST.get('Progeny2'))),
               "Debonded": str((request.POST.get('Debonded2'))),
               "Finished": str((request.POST.get('Finished2'))),
               "Issues": str((request.POST.get('Issues2')))}}
        Chip3 = {ChipsData['Ch3']:{
                "Rewashed": str((request.POST.get('Rewashed3'))),
               "Progeny": str((request.POST.get('Progeny3'))),
               "Debonded": str((request.POST.get('Debonded3'))),
               "Finished": str((request.POST.get('Finished3'))),
               "Issues": str((request.POST.get('Issues3')))}}
        Chip4 = {ChipsData['Ch4']:{
                "Rewashed": str((request.POST.get('Rewashed4'))),
               "Progeny": str((request.POST.get('Progeny4'))),
               "Debonded": str((request.POST.get('Debonded4'))),
               "Finished": str((request.POST.get('Finished4'))),
               "Issues": str((request.POST.get('Issues4'))),
               }}


        



        # p = Chip1, Chip2, Chip3, Chip4
        filenameJson = "/home/jetson/Documents/Infinity2.0Django_09122022/AssayLog4Chips.json"

        f = open(filenameJson)
        data2 = json.load(f)
        data2.update(Chip1)
        data2.update(Chip2)
        data2.update(Chip3)
        data2.update(Chip4)
        f.close()
        print(data2)
        with open(filenameJson, "w") as write:
            json.dump(data2, write, indent=4, separators=(',', ': '))
            
        return render(request, "RunningAssay.html", {})
               

    elif (request.method == 'POST' and 'Camera3' in request.POST):  # rename to camera1
        cameraPath = "/home/jetson/Documents/Infinity2.0Django_09122022/SelectedCameras.json"
        chipPath = "/home/jetson/Documents/Infinity2.0Django_09122022/CurrentFourChips.json"
        dat = {"Camera1": str((request.POST.get('Camera1'))),
               "Camera2": str((request.POST.get('Camera2'))),
               "Camera3": str((request.POST.get('Camera3'))),
               "Camera4": str((request.POST.get('Camera4')))}
        dat2 = {"Ch1": str((request.POST.get('Ch1'))),
                "Ch2": str((request.POST.get('Ch2'))),
                "Ch3": str((request.POST.get('Ch3'))),
                "Ch4": str((request.POST.get('Ch4')))}
        with open(cameraPath, "w") as w:
            json.dump(dat, w, indent=4, separators=(',', ': '))
        print("CamerasSaved")
        with open(chipPath, "w") as w:
            json.dump(dat2, w, indent=4, separators=(',', ': '))
        print("ChipsSaved")
        # return render(request, "RunningAssay.html", {})

    elif (request.method == 'POST' and 'Go_to_Settings' in request.POST):
        return render(request, "settings.html", {})

    elif (request.method == 'POST' and 'StartSterilization' in request.POST):
        sterilizationnumbersinhtml = {}

        if request.POST.get('txt1') != '':
            sterilizationnumbersinhtml['ster1'] = "Reagent 1 running for " + \
                str(strtosec(request.POST.get('txt1'))) + " seconds "
        else:
            pass

        if request.POST.get('txt2') != '':
            sterilizationnumbersinhtml['ster2'] = "Reagent 2 running for " + \
                str(strtosec(request.POST.get('txt2'))) + " seconds "
        else:
            pass

        if request.POST.get('txt3') != '':
            sterilizationnumbersinhtml['ster3'] = "Reagent 3 running for " + \
                str(strtosec(request.POST.get('txt3'))) + " seconds "
        else:
            pass

        if request.POST.get('txt4') != '':
            sterilizationnumbersinhtml['ster4'] = "Reagent 4 running for " + \
                str(strtosec(request.POST.get('txt4'))) + " seconds "
        else:
            pass

        if request.POST.get('txt5') != '':
            sterilizationnumbersinhtml['ster5'] = "Reagent 5 running for " + \
                str(strtosec(request.POST.get('txt5'))) + " seconds "
        else:
            pass

        sterilizationdict = {
            "Times": sterilizationnumbersinhtml
        }
        return render(request, "customsterilization2.html", sterilizationdict)

    elif (request.method == 'POST' and 'Enter_time_page' in request.POST):
        return render(request, "Enter_Time_for_Sterilization.html", sterilizationdict)

    elif (request.method == 'POST' and 'testingscript' in request.POST):
        return render(request, "Enter_Time_for_Sterilization.html", {})

    elif (request.method == 'POST' and 'StopRecording' in request.POST):
        StopAllPumps()
        curprofjsonpath = "/home/jetson/Documents/Infinity2.0Django_09122022/Pages/currentprofile.json"
        f = open(curprofjsonpath)
        curprofprofiledata = json.load(f)
        f.close()
        curprofname = curprofprofiledata['clientcode'] + '_' + \
            curprofprofiledata['assaycode'] + \
            '_' + curprofprofiledata['biorep']

        curprofnamenestpath = '/mnt/InternamDrive/Videos/' + str(curprofname) + '/'
        datas = {
            "CurrentProfile": curprofprofiledata,
            "headername": headernamemega,
            "ChipIds": chips,
            "Numberofvideostoupload": number_of_active_presplit_videos}
        videopath = '/mnt/InternamDrive/Videos/'
        try:
            path = os.path.join(videopath, curprofname)
            os.mkdir(path)
        except:
            pass
        try:
            path = os.path.join(curprofnamenestpath, 'Archive')
            os.mkdir(path)
        except:
            pass
        for filename in os.listdir("/mnt/InternamDrive/Videos/Recorded_Video/"):
            try:
                f = os.path.join(
                    "/mnt/InternamDrive/Videos/Recorded_Video/", filename)
                if os.path.isfile(f):
                    shutil.move(f, os.path.join(
                        curprofnamenestpath, 'Archive'), datas)
            except:
                print("Failed to Move to Archive")
        CancelThread()
        StartCameras(90001, 90001, '1920x1080', 5, 'Live', 2)
        return render(request, "RunningAssayLive.html", datas)

    elif (request.method == 'POST' and 'meatlaof' in request.POST):
        jsonpath = r"/home/jetson/Documents/Infinity2.0Django_09122022/AssayProfiles.json"
        r = str(request.POST.get('txtstartdate'))
        Profiles = {
            request.POST.get('txtclientcode') + "_" + str((request.POST.get('txtassaycode'))) + "_" + str((request.POST.get('txtbiorep'))): {
                "clientcode": str((request.POST.get('txtclientcode'))),
                "assaycode": str((request.POST.get('txtassaycode'))),
                "substratetype": str((request.POST.get('txtsubstratetype'))),
                "substrateid": str((request.POST.get('txtsubstrateid'))),
                "biorep": str((request.POST.get('txtbiorep'))),
                "loaddate": str((request.POST.get('txtLoaddate'))),
                "temperature": str((request.POST.get('txttemperature'))),
                "strain": str((request.POST.get('txtstrain'))),
                "media": str((request.POST.get('txtmedia'))),
                "bacteria": str((request.POST.get('txtbacteria'))),
                "liveordead": str((request.POST.get('txtliveordead'))),
                "technicalreplicate": str((request.POST.get('txttechnicalreplicate'))),
                "imagingdate": str((request.POST.get('txtimagingdate'))),
                "imagingtimepoint": str((request.POST.get('txtimagingtimepoint'))),
                "operator": str((request.POST.get('txtoperator'))),
                "chips": str((request.POST.get('txtchips'))),
                "startdate": r,
                "enddate": str((request.POST.get('txtenddate'))),
                "washingtime": str((request.POST.get('txtwashingtime'))),
                "resolution": str((request.POST.get('txtresolution'))),
                "framerate": str((request.POST.get('txtframerate'))),
                # "movielength": str((request.POST.get('txtmovielength'))),
                "sessionlength": str((request.POST.get('txtsessionlength'))),
                "numberofsessions": str((request.POST.get('txtnumberofsessions'))),
                "tltimeinterval": str((request.POST.get('tltimeinterval'))),
                "tltresolution": str((request.POST.get('tlresolution'))),
                "tltsessionlength": str((request.POST.get('tlmovielength'))),
                "tltplaybackspeed": str((request.POST.get('tlplaybackspeed'))),
            }
        }
        f = open(jsonpath)
        data = json.load(f)
        data.update(Profiles)
        f.close()
        with open(jsonpath, "w") as w:
            json.dump(data, w, sort_keys=True,
                      indent=4, separators=(',', ': '))
        updateJson()
        return render(request, "MainMenu.html", {})
    else:
        return render(request, "MainMenu.html", {})


def NewAssay_view(request, *args, **kwargs):
    return render(request, "NewAssay.html", {})


def RunningAssay_view(request, *args, **kwargs):
    print()
    # return render(request,"RunningAssay.html",{})


def SystemSterilization_view(request, *args, **kwargs):
    print()
    # return render(request,"SystemSterilization.html",{})


def Start_Pumps(request, *args, **kwargs):
    print("Starting Pumps")


def ExistingAssay_view(request, *args, **kwargs):
    ccode = request.GET['txtclientcode']
    {'txtclientcode': ccode}
    return render(request, "MainMenu.html",)

    # return render(request,"ExistingAssay.html",{})
