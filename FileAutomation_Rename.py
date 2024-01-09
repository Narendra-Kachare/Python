"""
    Rename() Files script

"""
import os
from sys import argv
import time


def DirectoryTravel_R(DirName):
    
    folderpath = ""
    
    flag = os.path.isabs(DirName)

    if flag == False:
        DirName = os.path.abspath(DirName)
    
    exist = os.path.isdir(DirName)

    if exist == True:
        for foldername, subfoldername, filename in os.walk(DirName):
            folderpath = foldername
            print(folderpath)
            i = 0
            for fname in filename:
                fname = os.path.join(foldername,fname)
                i = str(i)
                try:
                    os.rename(fname,str(os.path.join(folderpath,"PyResume"+i+".jpeg")))
                except FileExistsError as fobj:
                    print("Error : ",fobj)
                i = int(i)
                i+=1
    else:
        print("Directory is not Found")
        
    print("Files are sucessfully Renamed")


def main():
    print("------------------Automation Script------------------")
    
    if len(argv) == 2:
        if(argv[1] == "-u" or argv[1] == "-U"):
            print("Usage : Name_of_script <Source_File> <Destination_file>")
            print("Example : Demo.py Practice.py 1.py")
            exit()
        
        elif(argv[1] == "-h" or argv[1] == "-H"):
            print("These Script is used to renamed Directory file in numeric order")
            exit()
        else:
            StartT = time.time()
            DirectoryTravel_R(argv[1])
            EndT = time.time()
            print("Total time required to run the sript is : ",EndT-StartT)

    if(len(argv) != 2):
        print("Invalid number of arguments")
        exit()

    
    
    


if __name__ == "__main__":
    main()





