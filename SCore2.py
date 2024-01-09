import time
import multiprocessing

def Fun(no):
    sum = 0
    for i in range(100000):
        sum = sum + (no*no)
        print(sum)
    return sum



def main():
    print("Demonstration of Map function in multiprocessing")

    StartTime = time.time()
    P = multiprocessing.Pool()

    Result = []
    Result = P.map(Fun,range(10000))
    P.close()
    P.join()

    EndTime = time.time()
    print("Time required to run application : ",EndTime-StartTime)

if __name__ == "__main__": 
    main()