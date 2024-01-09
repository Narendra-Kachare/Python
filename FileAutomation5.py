"""
    Automation 
"""

import os
from sys import *
import time

def DirectoryTravel(DirName):
    print("The name of the script is : ",argv[0])

    flag = os.path.isabs(DirName)

    if flag == False:
        DirName = os.path.abspath(DirName)
    
    exist = os.path.isdir(DirName)
    if exist:
        for foldername, subfoldername, filename in os.walk(DirName):
            print("Current Directory name is : ",foldername)

            for subname in subfoldername:
                print("Subfolder name is : ",subname)
            
            for fname in filename:
                print(fname," with size : %d bytes"%os.path.getsize(os.path.join(fname,foldername)))
    else:
        print("Directory not exists")



def main():
    print("---------------Automation Script---------------")

    if len(argv) != 2:
        print("Invalid number of arguments")
        exit()
    
    if(argv[1] == "-u" or argv[1] == "-U"):
        print("Usage : Name_of_script First_argument")
        print("Example : Demo.py Marvellous")
        exit()

    if(argv[1] == "-h" or argv[1] == "-H"):
        print("These script is used to travel the directory")
        exit()
    
    else:
        StartT = time.time()
        DirectoryTravel(argv[1])
        EndT = time.time()

        print("Time required to execute the script is : ",(EndT - StartT))
    



if __name__ == "__main__":
    main()