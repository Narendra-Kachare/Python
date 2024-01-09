"""
    Automation3.py
"""
from sys import argv
import os


def DirctoryTravel(DirName):
    print("We are going to scan the directory : ",DirName)

    for foldername, subfoldername, filename in os.walk(DirName):
        for fname in filename:
            print(fname)
    


def main():
    print("------------Automation Script------------")

    print("Automation Script name is : ",argv[0])

    if (len(argv) != 2):
        if (argv[1] == "-u" or argv[1] == "-U"):
            print("Usage : Name_of_Script First_Argument")
            print("Example : Demo.py 11 21")
            exit()
        elif(argv[1] == "-h" or argv[1] == "-H"):
            print("These script is used for file Automation")
            exit()
        else:
            print("These is no option to handle")
    
    if(len(argv) != 2):
        print("Invalid number of arguments")
        exit()
    else:
        DirctoryTravel(argv[1])



if __name__ == "__main__":
    main()