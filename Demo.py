"""
    Display directory files and their checksums
"""
import os
flag = False
File = input()
try:
    logfile = open(File,"x")
    logfile.close()
    print("File successfully created")
    flag = True

except FileExistsError:
    os.remove(File)
    print("File successfully removes")

if flag == True:
    logfile = open(File,"w")
    Data = input()
    logfile.write(Data)
    logfile.close()
    logfile = open(File,"r")
    print(logfile.read())
    logfile.close()
