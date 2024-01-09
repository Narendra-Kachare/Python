"""
    Rename() Files script

"""
import os
from sys import argv
import time



def DirectoryTravel_R(DirName,Extension):
    
    flag = os.path.isabs(DirName)

    if flag == False:
        DirName = os.path.abspath(DirName)
    
    exist = os.path.isdir(DirName)

    if exist == True:
        for foldername, subfoldername, filename in os.walk(DirName):
            for fname in filename:
                fname = os.path.join(foldername,fname)
                print(fname)
                try:
                    name,extension = os.path.splitext(fname)
                    fchangename = name+Extension
                    os.rename(fname,fchangename)
                except FileExistsError as fobj:
                    print("Error : ",fobj)
                except Exception as E:
                    print("Error : ",E)
    else:
        print("Directory is not Found")
        
    print("Files extensions are sucessfully Renamed")


def main():
    print("------------------Automation Script------------------")
    
    if len(argv) == 2:
        if(argv[1] == "-u" or argv[1] == "-U"):
            print("Usage : Name_of_script <Destination_file_path_dir> <extension>")
            print("Example : Demo.py Practice.py 1.py")
            exit()
        
        elif(argv[1] == "-h" or argv[1] == "-H"):
            print("These Script is used to renamed Directory file in numeric order")
            exit()

    if(len(argv) != 3):
        print("Invalid number of arguments")
        exit()
    
    StartT = time.time()
    DirectoryTravel_R(argv[1],argv[2])
    EndT = time.time()
    print("Total time required to run the sript is : ",EndT-StartT)

    
    
    


if __name__ == "__main__":
    main()





