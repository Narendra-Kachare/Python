"""
    Automation script which display all running process. Display memory consume by each process
"""


################################################
# Python import modules
################################################
import psutil
import time

################################################
# Function Name : logfile 
# Description : function create logfile 
# Input : 
# Output : listprocess
# Author : Narendra Mahadev Kachare
# Date : 17/11/2023
################################################
def Createlogfile(listprocess):
    # Create file
    afile = open('logfile.txt','w')
    Sep = "-"*98

    # Header
    afile.write(Sep+"\n"+time.ctime()+"\n"+Sep+"\n\n")

    for elements in listprocess:
        afile.write(str(elements)+"\n")
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
    return listprocess 

    

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

    print("Process Monitor")

    listprocess = DisplayProcess()

    Createlogfile(listprocess)
    



################################################
# Starter
################################################
if __name__ == "__main__":
    main()