import os
import shutil
source = "H:\\PYTHON_2018\\Advance_python_learning\\testdir"  #double slash is for windows
targetfolder = "H:\\PYTHON_2018\\PROJECTS\\project4_file_move"
entries = os.listdir(source)
print("hey below files are in directory" , entries)
part = int(len(entries)/4)
folderlist = os.listdir(targetfolder)
#Below is to part out index of list object file lsit in entries
list1 = entries[:part]
print(list1) # print to see splitting of file list can be commented after go live
list2 = entries[part:part+part]
print(list2)
list3 = entries [part+part:part*3]
print(list3)
list4 = entries [part*3:]
print(list4)
# below copying the files from source to destination , it can handle odd number files in folder also , last folder will
#additional file
for f in list1:
    shutil.copy(source+'\\'+f , targetfolder+'\\'+folderlist[0])
for f in list2:
    shutil.copy(source+'\\'+f , targetfolder+'\\'+folderlist[1])
for f in list3:
    shutil.copy(source+'\\'+f , targetfolder+'\\'+folderlist[2])
for f in list4:
    shutil.copy(source+'\\'+f , targetfolder+'\\'+folderlist[3])
