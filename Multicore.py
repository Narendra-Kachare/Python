import multiprocessing


def main():
    print("Demonstration of single core CPU")
    print("Number of core count un your cpu are : ",multiprocessing.cpu_count())


if __name__ == "__main__":
    main()