"""
    Automation 
"""

import os
from sys import *
import time

def DirectoryTravel(DirName,name):
    
    print("We are going to scan directory : ",DirName)

    flag = os.path.isabs(DirName)
    if flag == False:
        DirName = os.path.abspath(DirName)
    
    exist = os.path.isdir(DirName)
    
    if exist:
        for foldername, subfoldername, filename in os.walk(DirName):
            for fname in filename:
                if fname == name:
                    print("We are going to delete the file : ",fname)
                    os.remove(os.path.join(foldername,fname))
                    return
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
    

    if(len(argv) != 3):
        print("Invalid number of arguments")
        exit()  
    
    else:
        StartT = time.time()
        DirectoryTravel(argv[1],argv[2])
        EndT = time.time()
        print("Time required to execute the code is : ",EndT-StartT)


if __name__ == "__main__":
    main()