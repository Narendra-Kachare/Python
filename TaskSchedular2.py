"""

    Task Scheduling

"""
import datetime as dt
import time
import schedule


def Schedule_Hour():
    print("Schedular schedules after a hour....")
    print("Current time is : ",dt.datetime.now())

def Schedule_Minute():
    print("Schedular schedules after a hour....")
    print("Current time is : ",dt.datetime.now())

def Schedule_Seconds():
    print("Schedular schedules after a hour....")
    print("Current time is : ",dt.datetime.now())

def Schedule_Saturday():
    print("Schedular schedules after a hour....")
    print("Current time is : ",dt.datetime.now())

def main():
    print("Demonstration of fileIO")

    schedule.every().hour.do(Schedule_Hour)
    schedule.every().minutes.do(Schedule_Minute)
    schedule.every(5).seconds.do(Schedule_Seconds)
    schedule.every().saturday.do(Schedule_Saturday)

    while True:
        schedule.run_pending()
        time.sleep(1)



if __name__ == "__main__":
    main()
