"""
    File IO process in Python

"""
import os


def main():
    print("Demonstration of file IO")

    # Accept file name
    File_name = input("Enter file name : \n")

    # Create file
    if os.path.exists(File_name):
        print("File Already Exists")
    else:
        fobj = open(File_name,"x")
        fobj.close()
        print("File create and successfully closed")


    # Write into the file
    if os.path.exists(File_name):
        fobj = open(File_name,"w")
        Value = int(input("Enter the lines : \n"))
        print("Enter the Data that you want to store")
        for i in range(Value):
            Data = input("%d : "%i)
            fobj.write(Data)
        fobj.close()
        print("Written data successfully and then file closed")

    else:
        print("File create and successfully closed")

    
    

    # Delete file
    if os.path.exists(File_name):
        fobj = os.remove(File_name)
        print("File Successfully removed")
    else:
        print("File not Found")


if __name__ == "__main__":
    main()