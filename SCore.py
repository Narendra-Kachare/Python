import time
import multiprocessing

def fun(no):
    sum = 0
    for i in range(1000):
        sum = sum + (no*no)
        print(sum)
    return sum

def main():
    print("Demonstration of singlecore CPU")
    
    StartTime = time.time()
    Result = []
    P1 = multiprocessing.Pool()


    for no in range(1000):
        Result.append(fun(no))
    EndTime = time.time()
    print("Time required to execute the program is : ",EndTime - StartTime)

if __name__ == "__main__":
    main()