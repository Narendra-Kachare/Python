"""

    File system in python

"""
import os

def main():
    print("Demonstration of file IO\n")

    # Accept the file
    print("Enter file name : ")
    File_name = input()

    # Create the file
    if os.path.exists(File_name):
        print("File Already Exists\n")
    else:
        fobj = open(File_name,"x")
        fobj.close()
        print("\nFile created successfully and then closed\n")


    # Open the file
    if os.path.exists(File_name):
        fobj = open(File_name,"r")
        if fobj:
            fobj.close()
            print("File opened successfully and then closed\n")
        else:
            print("File unable to open\n")
    else:
        print("File not exists\n")
    
    # Write the file "w"
    if os.path.exists(File_name):
        fobj = open(File_name,"w")
        if fobj:
            Data = input("Enter the data that you want to store : \n")
            print(type(Data))
            fobj.write(Data.capitalize())
            fobj.close()
            print("Writing Data complete, File successfully closed")
        else:
            print("File unable to open\n")
    else:
        print("File not exists\n")

    
    # write the file "a"
    if os.path.exists(File_name):
        fobj = open(File_name,"a")
        if fobj:
            Data = input("Enter the data that you want to append od add : \n")
            fobj.write(Data)
            fobj.close()
            print("Writing data complete, File successfully closed")
        else:
            print("File unable to open")
    else:
        print("File not found")
            

    
    # Delete the file
    if os.path.exists(File_name):
        fobj = os.remove(File_name)
        print("\nFile Removed successfully\n")
    else:
        print("File not found\n")
    

    




if __name__ == "__main__":
    main()