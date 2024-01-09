"""
    Automation2.py
"""

from sys import argv

def Addition(No1, No2):
    Ans = 0
    Ans = No1 + No2
    return Ans


def main():
    print("---------------Automation Script---------------")

    if (len(argv) == 2):
        if (argv[1] == "-u" or argv[1] == "-U"):
            print("Usage : Name_of_script First_Argument Second_Argument")
            print("Example : Demo.py 11 18")
            exit()
        elif(argv[1] == "-h" or argv[1] == "-H"):
            print("This script is used to additin of two numbers")
            exit()
        else:
            print("There is no such option to handle")
            exit()
    
    if (len(argv) != 3):
        print("Invalid number of arguments")
        exit()
    else:
        Ret = Addition(int(argv[1]),int(argv[2]))
        print("Addition is : %d"%Ret)





if __name__ == "__main__":
    main()