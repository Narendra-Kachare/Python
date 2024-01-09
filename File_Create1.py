"""
    File system in python

"""
import os

def main():
    print("Demonstration of File handling")

    
    # File Create (fd : File Directory)

    if os.path.exists('Marvellous.txt'):
        print("File Already Exist")
    else:
        fd = open("Marvellous.txt","x")
        print("File Successfully created")


if __name__ == "__main__":
    main()