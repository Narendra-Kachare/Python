"""
    File Automation 1
"""

import os
from sys import argv


def DirectoryTravel(DirName):
    print("We are going to scan the directory : ",DirName)

    for foldername, subfoldername, filename in os.walk(DirName):
        
        for fname in filename:
            print(fname)

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
            DirectoryTravel(argv[1])    # Loop madhe janar
            exit()
    if(len(argv) != 2):
        print("Invalid number of arguments")
        exit()

        




if __name__ == "__main__":
    main()



