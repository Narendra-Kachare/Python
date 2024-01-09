"""
Automation script which display all running process

"""

################################################
# Python import modules
################################################
import psutil


################################################
# Function Name : ProcessDisplay 
# Description : function displays running process 
# Input : 
# Output : 
# Author : Narendra Mahadev Kachare
# Date : 14/11/2023
################################################
def ProcessDisplay():
    listprocess = []

    try:
        for proc in psutil.process_iter():
            pinfo = proc.as_dict(attrs=['pid','username','name'])

            listprocess.append(pinfo)
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        pass
    return listprocess


################################################
# Function Name : main 
# Description : function where execution starts
# Input : 
# Output : 
# Author : Narendra Mahadev Kachare
# Date : 14/11/2023
################################################

def main():
    print("Demonstration of process automation")

    print("Process Monitor")

    listprocess = ProcessDisplay()

    for element in listprocess:
        print(element)
 

################################################
# starter kit
################################################
if __name__ == "__main__":
    main()