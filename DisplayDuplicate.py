"""
    Display directory files and their checksums
"""
################################################
# Python import packages
################################################
import os
from sys import *
import time
import hashlib

################################################
# Function Name : hashfile 
# Description : hashfile function will generate checksum of given files
# Input : fname
# Output : hexadigit function i.e hasher.hexdigest()
# Author : Narendra Mahadev Kachare
# Date : 3/11/2023
################################################
def hashfile(fname,blocksize = 1024):
    afile = open(fname,"rb")
    buf = afile.read(blocksize)
    hasher = hashlib.md5()
    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(blocksize)
    return hasher.hexdigest()

################################################
# Function Name : DisplayDuplicate 
# Description : These function will return duplicate files
# Input : DirName
# Output : Dups(Dictionary)
# Author : Narendra Mahadev Kachare
# Date : 3/11/2023
################################################
def DisplayDuplicate(DirName):
    flag = os.path.isabs(DirName)
    if flag == False:
        DirName = os.path.abspath(DirName)
    exist = os.path.isdir(DirName)

    dups = {}
    if exist:
        for foldername, subfoldername, filename in os.walk(DirName):
            for fname in filename:
                fname = os.path.join(foldername,fname)
                file_hash = hashfile(fname)
                if file_hash in dups:
                    dups[file_hash].append(fname)
                else:
                    dups[file_hash] = [fname]
        return dups
    else:
        print("folder does not exists")
    
################################################
# Function Name : PrintDuplicate 
# Description : print duplicate files 
# Input : Dict1
# Output : compare checksums and print duplicate files
# Author : Narendra Mahadev Kachare
# Date : 4/11/2023
################################################
def PrintDuplicate(Dict1):
    Duplicate = []
    for files in Dict1.values():
        if len(files) > 1:
           Duplicate.append(files)
    if len(Duplicate) == 0:
        print("No Duplicate files are found")
    else:
        print("Out of ",len(Dict1),"files ",len(Duplicate)," files are Duplicate")
    print(Duplicate)
    
################################################
# Function Name : main
# Description : main function from where execution starts
# Input : 
# Output : 
# Author : Narendra Mahadev Kachare
# Date : 3/11/2023
################################################

def main():
    print("---------------Automation Script---------------")

    if(len(argv) == 2):
        if(argv[1] == "-u" or argv[1] == "-U"):
            print("Usage : Name_of_script <Absolute_Directory_Path>")
            print("Example : Demo.py Marvellous")
            exit()

        elif(argv[1] == "-h" or argv[1] == "-H"):
            print("These script is used to display duplicate files")
            exit()
        else:
            Arr = {}
            StartT = time.time()
            Arr = DisplayDuplicate(argv[1])
            PrintDuplicate(Arr)
            EndT = time.time()
    
    if(len(argv) != 2):
        print("Invalid number of arguments")
        exit()

################################################
# Starter
################################################

if __name__ == "__main__":
    main()