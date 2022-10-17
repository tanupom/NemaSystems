from io import BytesIO
from django.test import TestCase
import os, json, shutil
from ast import Div
from datetime import date
import json
import pandas as pd
from datetime import datetime























def startsession():
    #code to get curprofname
    curprofjsonpath = "/home/infinitysystem/Documents/Infinity2.0Django_09122022/Pages/currentprofile.json"
    f = open(curprofjsonpath)
    curprofprofiledata = json.load(f)
    data = {'col1': curprofprofiledata.keys(), 'col2': curprofprofiledata.values()}
    dataframe = pd.DataFrame.from_dict(data, orient="index").T
    # dataframe = pd.DataFrame.from_dict(curprofprofiledata, orient="index")
    f.close()
    curprofname = curprofprofiledata['clientcode'] + '_' + \
        curprofprofiledata['assaycode'] + '_' + curprofprofiledata['biorep']
    #code to upload assay log
    today = str(date.today())
    dailyexceldst = r'/home/infinitysystem/Documents/Infinity2.0Django_09122022/Templates/DailyExcelFiles/'
    dailyexcelsrc = r'/home/infinitysystem/Documents/Infinity2.0Django_09122022/Pages/AssayLogOverviewTemplate.xlsx'
    excelfilenamecheckifexists = dailyexceldst + curprofname + '__' + today + '.xlsx' #remove extra underscore when done with testing
    #check if file exists, if it does not, start uploading it with certain criteria.
    checkiffileexists = os.path.isfile(excelfilenamecheckifexists)
    if checkiffileexists == True:
        pass
    else:
        #step 1 copy file from dst to src
        nameofblankexcelfile = 'AssayLogOverviewTemplate.xlsx'
        shutil.copy(dailyexcelsrc, dailyexceldst)

        #step 2 rename new file with curprofname and the date
        old_name = dailyexceldst + nameofblankexcelfile
        new_name = dailyexceldst + curprofname + '_' + today + '.xlsx'
        os.rename(old_name, new_name)
        dynamic_new_excel_name = new_name
        #step 3 pandas read new excel file and:
        # a. add date 
        # b. add start time and end time 
        # c. add end time
        Detailedexcelpath = r'/home/infinitysystem/Documents/Infinity2.0Django_09122022/media/' + curprofname + '.xlsx'


        detaileddf = pd.read_excel(Detailedexcelpath, index=False, sheet_name='General Metadata Structure')
        assaylogdf = pd.read_excel(dailyexcelsrc, index=False,sheet_name='Assay Log')
        blankdf = pd.read_excel(dailyexcelsrc, index=False,sheet_name='blank')
        k = datetime.now()
        assaylogdf.at[2, 'Start Time'] = k.time()
        assaylogdf.at[2, 'End Time'] = ''


        
            # writer1 = pd.ExcelWriter(b, engine="openpyxl")
            
            # writer1.save()

        # with BytesIO() as b:
        #     # with pd.ExcelWriter(dynamic_new_excel_name) as writer:
        with pd.ExcelWriter(dynamic_new_excel_name, engine="openpyxl") as writer:
            detaileddf.to_excel(writer, sheet_name='Detailed Project Overview')
            assaylogdf.to_excel(writer, sheet_name='Assay Log')
        #         # assaylogdf.at[2, 'G'] = today
        #         # assaylogdf.at[2, 'H'] = 'thing'
            dataframe.to_excel(writer, sheet_name='Summarized_Project_Overview')
        #         dataframe.to_excel(writer, sheet_name="Summarized", startrow=0, startcol=0)
        #         # Summarized_Project_Overview = writer.book.create_sheet(title='Summarized_Project_Overview')
           
        #     # Summarized_Project_Overview.cell(column=1, row=1, value=summarizeddata)

        # file_name = 'MarksData.xlsx'

        # dataframe.to_excel(file_name)
        
                    


        #newexceldfassaylog = pd.read_excel(dynamic_new_excel_name, sheet_name='Assay Log')
        #newexceldfsummarized = pd.read_excel(dynamic_new_excel_name, sheet_name='Summarized Project Overview')
        #newexceldfdetailed = pd.read_excel(dynamic_new_excel_name, sheet_name='Detailed Project Overview')


def clickofcheckboxes():
    #run the thing to update excel rows with chip id and thing that is wrong
    thing = 'cancer'




startsession()























# CurrentProfilejsonpath = r"/home/infinitysystem/Documents/Infinity2.0Django_09122022/Pages/currentprofile.json"

# def thing(timestr):
#     try:
#         seconds = 0
#         str(timestr)
#         timearr = timestr.split(':')
#         hour = 60 * 60 * int(timearr[0])
#         min = 60 * int(timearr[1])
#         seconds = int(timearr[2])
#         return hour + min + seconds
#     except:
#         return -1


# print(thing("00:01:30"))



# Create your tests here.
# curprofjsonpath = "/home/infinitysystem/Documents/Infinity2.0Django_09122022/Pages/currentprofile.json"
# f = open(curprofjsonpath)
# curprofprofiledata = json.load(f)
# f.close()
# curprofname = curprofprofiledata['assaycode'] + '_' + curprofprofiledata['clientcode'] + '_' + curprofprofiledata['biorep']
# videopath = '/home/infinitysystem/Documents/Infinity2.0Django_09122022/Videos'
# print(str(curprofname))
# curprofnamenestpath = '/home/infinitysystem/Documents/Infinity2.0Django_09122022/Videos/' + str(curprofname) + '/'
# try:
#     path = os.path.join(videopath, curprofname)
#     os.mkdir(path)
# except:
#     pass
# try:
#     path = os.path.join(curprofnamenestpath, 'Pre-Split')
#     os.mkdir(path)
# except:
#     pass
# try:
#     path = os.path.join(curprofnamenestpath, 'Post-Wash')
#     os.mkdir(path)
# except:
#     pass
# try:
#     path = os.path.join(curprofnamenestpath, 'Wash')
#     os.mkdir(path)
# except:
#     pass



# #to move files



# source_dir = '/path/to/source_folder'
# target_dir = '/path/to/dest_folder'
    
# file_names = os.listdir(source_dir)
    
# for file_name in file_names:
#     shutil.move(os.path.join(source_dir, file_name), target_dir)