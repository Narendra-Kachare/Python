"""
    Automation 
"""

import os
from sys import *
import time

def DirectoryTravel(DirName,name):
    separator = "-" * 100
    print("The name of the script is : ",argv[0])

    flag = os.path.isabs(DirName)

    if flag == False:
        DirName = os.path.abspath(DirName)  
    
    exist = os.path.isdir(DirName)
    if (exist == True):
        for foldername, subfoldername, filename in os.walk(DirName):
            for fname in filename:
                if (fname == name):
                    print("File is present in the directory with name : ",fname)
        
    else:
        print("Directory not exists")



def main():
    print("---------------Automation Script---------------")

    if len(argv) != 3:
        print("Invalid number of arguments")
        exit()
    
    if(argv[1] == "-u" or argv[1] == "-U"):
        print("Usage : Name_of_script First_argument Second_argument")
        print("Example : Demo.py Marvellous Practice.py")
        exit()

    if(argv[1] == "-h" or argv[1] == "-H"):
        print("These script is used to travel the directory and check whether file is present or not")
        exit()
    
    else:
        StartT = time.time()
        DirectoryTravel(argv[1],argv[2])
        EndT = time.time()

        print("Time required to execute the script is : ",(EndT - StartT))
    



if __name__ == "__main__":
    main()