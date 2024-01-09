"""
    Automation script which display all running processess.
    Display memory consumed by each process

"""
################################################
# Python import modules
################################################
import psutil
from sys import argv

################################################
# Function Name : ProcessDisplay 
# Description : function display memory usage
# Input  :   
# Output : 
# Author : Narendra Mahadev Kachare
# Date : 19/11/2023
################################################
def ProcessDisplay():
    # Create empty list
    listprocess = []

    # fetch process, minimize data, append
    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['username','name','pid'])
            pinfo['vms'] = str(proc.memory_info().vms / (1024*1024))+" MB"
    
            listprocess.append(pinfo)
        except (psutil.AccessDenied, psutil.NoSuchProcess, psutil.ZombieProcess):
            pass
    # return process
    return listprocess


################################################
# Function Name : main 
# Description : function where execution starts
# Input : 
# Output : 
# Author : Narendra Mahadev Kachare
# Date : 19/11/2023
################################################
def main():
    print("Process Automation Script")

    print("Application name : ",argv[0])

    if(len(argv) == 2):
        if(argv[1] == "-u" or argv[1] == "-U"):
            print("Usage : Application_name Path_of_Directory")
            print("Example : Demo.py Marvellous")
            exit()
        elif(argv[1] == "-h" or argv[1] == "-H"):
            print("These script is used to display memory consumed by each process")
            exit()

    listprocess = ProcessDisplay()
    for elements in listprocess:
        print(elements)


################################################
# Starter kit
################################################
if __name__ == "__main__":
    main()
