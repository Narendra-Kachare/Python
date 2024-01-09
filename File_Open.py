"""
    File system in python

"""
import os

def main():
    print("Demonstration of file handling")

    # Accept File name
    File_name = input("Enter File name : ")

    # Create file
    if os.path.exists(File_name):
        print("File ALready Exists")
    else:
        fd = open(File_name,"x")
        print("File successfully created")
        fd.close()
        print("File closed successfully\n")

    # Open File
    if os.path.exists(File_name):
        
        fd = open(File_name,"r")
        if fd:
            print(File_name,"Opened Successfully")
            fd.close()
            print("File closed successfully\n")
        else:
            print("Unable to open file\n")

    else:
        print("File not found")

    # Delete File 
    if os.path.exists(File_name):
        fd = os.remove(File_name)
        print(File_name,"Deleted Successfully\n")
    else:
        print("File does not exists\n")
    




if __name__ == "__main__":
    main()