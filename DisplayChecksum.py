"""
    Display directory files and their checksums

"""
################################################
# Python import packages
################################################

import os 
from sys import argv
import time
import hashlib

################################################
# Function Name : hashfile
# Description : Generate chechsum or hashcode by reading files
# Input : DirName
# Output : generate checksum by using function hasher.hexdigest()
# Author : Narendra Mahadev Kachare
# Date : 30/10/2023
################################################

def hashfile(path, blocksize = 1024):
    afile = open(path,"rb")
    buf = afile.read(blocksize)
    hasher = hashlib.md5()
    while(len(buf) > 0):
        hasher.update(buf)
        buf = afile.read(blocksize)
    afile.close()
    return hasher.hexdigest()

################################################
# Function Name : DisplayChecksum 
# Description : Display checksum of specified folder files
# Input : DirName
# Output : 
# Author : Narendra Mahadev Kachare
# Date : 30/10/2023
################################################
def DisplayChecksum(DirName):
    print("We are going to scan directory with name : ",DirName)
    
    flag = os.path.isabs(DirName)
    if flag == False:
        DirName = os.path.abspath(DirName)
    
    exist = os.path.isdir(DirName)
    if exist == True:
        for foldername , subfoldername, filename in os.walk(DirName):
            print("Current foldername is : ",foldername)
            for fname in filename:
                fname = os.path.join(foldername,fname)
                hash_file = hashfile(fname)
                print(fname,":",hash_file,end="\n")
    else:
        print("Directory does not exists")



################################################
# Function Name : main 
# Description : main function from where execution starts
# Input : 
# Output : 
# Author : Narendra Mahadev Kachare
# Date : 30/10/2023
################################################

def main():
    print("---------------Automation Script---------------")
    print("Application name is : ",argv[0])
    if (len(argv) == 2):
        if (argv[1] == "-u" or argv[1] == "-U"):
            print("Usage : Name_of_Script First_argument")
            print("Example : Demo.py Marvellous")
            exit()
        elif(argv[1] == "-h" or argv[1] == "-H"):
            print("These script is display file names and its checksums")
            exit()
        else:
            StartT = time.time()
            DisplayChecksum(argv[1])
            EndT = time.time()
            print("Time required to execute the code is : ",EndT-StartT)
    else:
        print("Invalid number of arguments")
        exit()
    
if __name__ == "__main__":
    main()