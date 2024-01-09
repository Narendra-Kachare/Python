"""
    Automation script that convert extension of image file 

"""
################################################
# Python import modules
################################################
import os
from sys import argv
import time
from PIL import Image


################################################
# Function Name : ExtensionConvertor 
# Description : function converts extension of file (webp to pdf)
# Input : name,extension,RenameE
# Output : 
# Author : Narendra Mahadev Kachare
# Date : 05/12/2023
################################################
def ExtensionConvertor(name,extension,RenameE = argv[2]):
    if extension == "."+RenameE:
        print("File extension is already in your choice format")
        pass
    else:

        img = Image.open(name+extension).convert("RGB")
        img.save(name+"."+RenameE,RenameE)

        # After that remove existing file
        os.remove(name+extension)

################################################
# Function Name : DirectoryTravel
# Description : function travel directory files
# Input : DirName
# Output : 
# Author : Narendra Mahadev Kachare
# Date : 05/12/2023
################################################
def DirectoryTravel_R(DirName):
    
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
                    ExtensionConvertor(name,extension)
                except FileExistsError as fobj:
                    print("Error : ",fobj)
                except Exception as E:
                    print("Error : ",E)
    else:
        print("Directory is not Found")
        
    print("Files extensions are sucessfully Renamed")

################################################
# Function Name : main 
# Description : function where execution starts
# Input : 
# Output : 
# Author : Narendra Mahadev Kachare
# Date : 05/12/2023
################################################
def main():
    print("------------------Automation Script------------------")
    
  
    if(argv[1] == "-u" or argv[1] == "-U"):
        print("Usage : Name_of_script <Destination_file_path_dir> <Rename_Extensiton_Formatname>")
        print("Example : Demo.py Practice.py png")
        exit()
    
    if(argv[1] == "-h" or argv[1] == "-H"):
        print("These Script changes image file extension format")
        exit()

    if(len(argv) != 3):
        print("Invalid number of arguments")
        exit()

    StartT = time.time()
    DirectoryTravel_R(argv[1])
    EndT = time.time()
    print("Total time required to run the sript is : ",EndT-StartT)
    
################################################
# Starter kit
################################################
if __name__ == "__main__":
    main()





