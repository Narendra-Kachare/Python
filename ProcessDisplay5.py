"""
    Automation script which display all running process. Display memory consume by each process
"""

################################################
# Python import modules
################################################
import os
import schedule
from sys import *
import psutil
import time

################################################
# Function Name : Createlogfile 
# Description : function create logfile having running process list
# Input : listprocess
# Output : 
# Author : Narendra Mahadev Kachare
# Date : 17/11/2023
################################################

def Createlogfile(listprocess,dir_path = "Marvellous"):

    # Create log folder
    exist = os.path.isdir(dir_path)
    if exist:
        pass 
    else:
        os.mkdir(dir_path)
        print("Folder sucessfully created")
    
    # create and Rename the file
    Sep = "-"*98
    filepath = os.path.join(dir_path,time.ctime())
    filepath = filepath.replace(' ','_').replace(':','.')
    afile = open((filepath+".log"),'w')

    # Header
    afile.write("\n"+Sep+"\n"+(time.ctime())+"\n"+Sep+"\n")
    for element in listprocess:
        afile.write(str(element)+"\n")
    print("Log file successfully created")
    afile.close()



################################################
# Function Name : ProcessMemoryDisplay 
# Description : function returns each process inforamtion with memory in bytes
# Input : 
# Output : 
# Author : Narendra Mahadev Kachare
# Date : 17/11/2023
################################################

def ProcessMemoryDisplay():
    # Create Empty list
    listprocess = []
    # fetch, minimize and append
    try:
        for proc in psutil.process_iter():
            pinfo = proc.as_dict(['pid','name','username'])
            vms = proc.memory_info().vms / (1024 * 1024)

            listprocess.append(pinfo)
    except (psutil.AccessDenied, psutil.NoSuchProcess, psutil.ZombieProcess):
        pass

    # return list
    return Createlogfile(listprocess,argv[1])




################################################
# Function Name : main 
# Description : function where execution starts
# Input : 
# Output : 
# Author : Narendra Mahadev Kachare
# Date : 18/11/2023
################################################

def main():
    print("----------------Process  Automation Script----------------")

    print("Application name : "+argv[0])

    if len(argv) == 2:
        if(argv[1] == "-u" or argv[1] == "-U"):
            print("Usage : ApplicationName AbsolutePath_of_Directory")
            print("Demo.py Marvellous")
            exit()
        elif(argv[1] == "-h" or argv[1] == "-H"):
            print("This script is used to store log record of running processess")
            exit()
        else:
            
            schedule.every(2).seconds.do(ProcessMemoryDisplay)
    
            while True:
                schedule.run_pending()
                time.sleep(1)
    else:
        print("Invalid number of arguments")
        exit()
            
################################################
# Python starter kit
################################################
if __name__ == "__main__":
    main()