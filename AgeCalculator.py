"""
    Age Calculator
"""

import datetime as dt

def main():
    print("Demonstration of Age Calculator")
    Name = input("Enter your name : \n")

    ArrM = [31,28,31,30,31,30,31,31,30,31,30,31]

    B_D = int(input("Enter your Birth date : "))
    B_M = int(input("Enter your Birth Month : "))
    B_Y = int(input("Enter your Birth Year : "))
    
    Present = dt.date.today()
    P_D = Present.day
    P_M = Present.month
    P_Y = Present.year

    if B_D > P_D:
        P_D = P_D + ArrM[B_M - 1]
        P_M = P_M - 1
    
    if B_M > P_M:
        P_M = P_M + 12
        P_Y = P_Y - 1
        
    R_D = P_D - B_D
    R_M = P_M - B_M
    R_Y = P_Y - B_Y

    print("Welcome",Name,"\nYour Age will be :",R_Y,"years,",R_M,"months,",R_D,"days")

if __name__ == "__main__":
    main()