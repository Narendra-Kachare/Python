"""
    File IO process in Python

"""
import os


def main():
    print("Demonstration of file IO")

    # Accept file name
    File_name = input("Enter file name : \n")

    # # Create file
    # if os.path.exists(File_name):
    #     print("File Already Exists")
    # else:
    #     fobj = open(File_name,"x")
    #     fobj.close()
    #     print("File create and successfully closed")


    # # Write into the file
    # if os.path.exists(File_name):
    #     fobj = open(File_name,"w")
    #     if fobj:
    #         Length = int(input("Enter the lines : \n"))
    #         print("Enter the Data that you want to store")
    #         for i in range(1,Length+1):
    #             Data = input("%d : "%i)
    #             fobj.write(Data)
    #             fobj.write("\n")
    #         fobj.close()
    #         print("Written data successfully and then file closed")
    #     else:
    #         print("Unable to open file")
    # else:
    #     print("File not Found")

    # Read file
    if os.path.exists(File_name):
        fobj = open(File_name,"r")
        if fobj:
            
            print(File_name+" File is : \n")
            Line1 = fobj.readlines()
            Line2 = fobj.readlines()

            print(Line1)
            print(Line2)
            fobj.close()
            print("Written data successfully and then file closed")
        else:
            print("Unable to open file")
    else:
        print("File not Found")

    # Read file
    if os.path.exists(File_name):
        fobj = open(File_name,"r")
        if fobj:
            
            print(File_name+" File is : \n")
            Line1 = fobj.readlines(2 )
            Line2 = fobj.readlines(10)

            print(Line1)
            print(Line2)
            fobj.close()
            print("Written data successfully and then file closed")
        else:
            print("Unable to open file")
    else:
        print("File not Found")
    
    

    # # Delete file
    # if os.path.exists(File_name):
    #     fobj = os.remove(File_name)
    #     print("File Successfully removed")
    # else:
    #     print("File not Found")


if __name__ == "__main__":
    main()