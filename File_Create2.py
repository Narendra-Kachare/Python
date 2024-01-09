"""
    File system in python

"""
import os

def main():
    print("Demonstration of File handling")

    # Accept input from user
    File_name = input()
    
    # File Create (fd : File Directory)

    if os.path.exists(File_name):
        print("File Already Exist")
    else:
        fd = open(File_name,"x")
        print("File Successfully created")

    # Delete File

    


if __name__ == "__main__":
    main()