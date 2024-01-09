"""
    File Automation 1
"""

import os
from sys import argv
import time


def DirectoryTravel(DirName):
    print("We are going to scan the directory : ",DirName)

    for foldername, subfoldername, filename in os.walk(DirName):
        print("Current Directory name is : ",foldername)

        for subname in subfoldername:
            print("Subfolder name is : ",subname)
        for fname in filename:
            print("->",fname,end="\t")  
        print()

def main():
    print("------------Automation Script------------")

    if(len(argv) == 2):
        if(argv[1] == "-h" or argv[1] == "-H"):
            print("These script is used to directory travel")
            exit()
        elif(argv[1] == "-u" or argv[1] == "-U"):
            print("Usage : Name_of_script <Dir_name>")
            print("Example : Demo.py Marvellous")
            exit()
        else:
            Starttime = time.time()
            DirectoryTravel(argv[1])    # Loop madhe janar
            Endtime = time.time()
            print("Total time required to execute the code is : %d sec"%(int(Endtime-Starttime)))
            exit()
    if(len(argv) != 2):
        print("Invalid number of arguments")
        exit()

if __name__ == "__main__":
    main()



