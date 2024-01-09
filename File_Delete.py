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
        print(File_name," Successfully created")
        fd.close()  # File close to overcome permission error difficulties
        print("File Successfully closed")


    

    # Delete File
    if os.path.exists(File_name):
        fd = os.remove(File_name)
        print(File_name,"File Deleted Successfully")
    else:
        print("File Not Found")

    

    


if __name__ == "__main__":
    main()