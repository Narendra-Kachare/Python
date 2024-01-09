"""
    Automation 
"""

import os
from sys import *
import time

def DirectoryTravel(DirName):
    
    print("We are going to scan directory : ",DirName)
    iMax = 0
    MaxsizefilePath = ""

    flag = os.path.isabs(DirName)
    if flag == False:
        DirName = os.path.abspath(DirName)
    
    exist = os.path.isdir(DirName)
    if exist:
        for foldername, subfoldername, filename in os.walk(DirName):
            for fname in filename:
                filepath = os.path.join(foldername,fname)
                if(iMax < os.path.getsize(filepath)):
                    iMax = os.path.getsize(filepath)
                    MaxsizefilePath = filepath
        print("Maximum size file name is ",MaxsizefilePath," with filesize : ",iMax)
        print("We are going to remove the file : ")
        Decision = input()
        if Decision == "Yes" or Decision == "yes" or Decision == "Y" or Decision == "y":
            os.remove(MaxsizefilePath)
            print("File Successfully Deleted")
        else:
            print("File is not Deleted")
    else:
        print("File not exists")

def main():
    print("-------------------Automation Script-------------------")
    if(argv[1] == "-u" or argv[1] == "-U"):
        print("Usage : Name_of_sript First_argument Second_argument")
        print("Example : Demo.py Marvellous Practice.py")
        exit()

    if(argv[1] == "-h" or argv[1] == "-H"):
        print("These script is used to travel directory and perform operation")
        print("Example : Demo.py Marvellous Practice.py")
        exit()

    if(len(argv) != 2):
        print("Invalid number of arguments")
        exit()  
    
    else:
        StartT = time.time()
        DirectoryTravel(argv[1])
        EndT = time.time()

if __name__ == "__main__":
    main()