"""
    Automation1.py
"""

from sys import argv



def main():
    print("----------Automation Script-----------")

    if(len(argv) == 2):         # flag 
        if(argv[1] == "-u" or argv[1] == "-U"):
            print("Usage : Name_of_Script First_Argument Second_Argument")
            print("Example : Demo.py 11 10")
            exit()
        
        elif(argv[1] == "-h" or argv[1] == "-H"):   
            print("Automation script used to perform addition of two numbers")
            exit()
        
        else:
            print("There is no option to handle")
            exit()
    if(len(argv) != 3):
        print("Invalid number of arguments")
        exit()


if __name__ == "__main__":
    main()