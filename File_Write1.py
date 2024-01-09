"""

    File system in python

"""

import os

def main():
    print("Demonstration of file handling")

    # Accept file name
    File_name = input("Enter File name : \n")

    # Create file
    if os.path.exists(File_name):
        print("File Already Exists\n")
    else:
        fobj = open(File_name,"x")
        print(File_name+" Succcessfully Created")
        fobj.close()
        print("File suucessfully Closed\n")
    
    # Open File
    if os.path.exists(File_name):
        fobj = open(File_name,"r")
        if fobj:
            print(File_name+" Successfully opened")
            fobj.close()
            print("File Successfully closed\n")
        else:
            print("File unable to opened\n")
    else:
        print("File Does not exists\n")
    
    # File Write1 using "w" 
    if os.path.exists(File_name):
        fobj = open(File_name,"w")
        if fobj:
            print("File successfully opened")
            Data = input("Enter the data that you want to write : \n")
            fobj.write(Data)
            fobj.close()
            print("File Successfully closed\n")
        else:
            print("File unable to open\n")
    else:
        print("File does not exist\n")

            





    # # Delete File
    # if os.path.exists(File_name):
    #     fobj = os.remove(File_name)
    #     print(File_name+" file successfully removed")
    # else:
    #     print("File Does Not Exists")


if __name__ == "__main__":
    main()