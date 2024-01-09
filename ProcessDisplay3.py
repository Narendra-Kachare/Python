"""
    Automation script which display all running process. Display memory consume by each process
"""


################################################
# Python import modules
################################################
import psutil
import time
import os
import schedule
from sys import *

################################################
# Function Name : logfile 
# Description : function create logfile 
# Input : 
# Output : listprocess
# Author : Narendra Mahadev Kachare
# Date : 17/11/2023
################################################
def Createlogfile(listprocess,log_dir = "Marvellous"):

    exist = os.path.isdir(log_dir)
    if exist:
        pass
    else:
        # Create directory where your logfiles are saved
        os.mkdir(log_dir)

    # join file path with directory
    filepath = os.path.join(log_dir,"Marvellous %s.txt"%(time.ctime()))
    filepath = (filepath.replace(" ","_").replace(":","."))
    # Create file
    afile = open(filepath,'w')

    # Header
    Sep = "-"*98
    afile.write(Sep+"\n"+time.ctime()+"\n"+Sep+"\n")

    for elements in listprocess:
        afile.write(str(elements)+"\n")
    afile.write("\n\n")
    afile.close()
    print("log file of running process successfully created")

################################################
# Function Name : ProcessDisplay 
# Description : function return list of running process list inforamation
# Input : 
# Output : listprocess
# Author : Narendra Mahadev Kachare
# Date : 17/11/2023
################################################
def DisplayProcess():
    # Create empty list
    listprocess = []

    # fetch process, minimize info, append data
    for proc in psutil.process_iter():
        pinfo = proc.as_dict(['pid','name','username'])
        listprocess.append(pinfo)

    # return list
    return Createlogfile(listprocess)

    

################################################
# Function Name : main 
# Description : function where execution starts
# Input : 
# Output : 
# Author : Narendra Mahadev Kachare
# Date : 17/11/2023
################################################

def main():
    print("-------------Automation script---------------")
    print("Application name : ",argv[0])
    print("Process Monitor")
    

    schedule.every(2).seconds.do(DisplayProcess)

    while True:
        schedule.run_pending()
        time.sleep(1)
    
################################################
# Starter
################################################
if __name__ == "__main__":
    main()