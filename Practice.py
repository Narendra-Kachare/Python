"""
    Web Automation that login gmail 
"""
################################################
# Import python modules
################################################
from selenium import webdriver
from urllib import request,error
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

################################################
# Global varibles
################################################
username = 'narendrakachare7@gmail.com'
password = 'Narendra15@'
url = "https://accounts.google.com/v3/signin/identifier?authuser=0&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ec=GAlAFw&hl=en-GB&service=mail&flowName=GlifWebSignIn&flowEntry=AddSession&dsh=S1762397050%3A1701608774469280&theme=glif"

################################################
# Function Name : is_connected
# Description : function create schedule log file list each second
# Input : foldername
# Output : listprocess
# Author : Narendra Mahadev Kachare
# Date : 24/11/2023
################################################
def is_connected():
    try:
        request.urlopen("https://www.youtube.com/",timeout=1)
        return True
    except error.URLError() as aobj:
        return False
################################################
# Function Name : login_to_gmail 
# Description : function login gmail account
# Input : 
# Output : 
# Author : Narendra Mahadev Kachare
# Date : 03/12/2023
################################################


################################################
# Function Name : login_to_gmail 
# Description : function login gmail account
# Input : 
# Output : 
# Author : Narendra Mahadev Kachare
# Date : 03/12/2023
################################################
def login_to_gmail():

    s = Service(r"D:\API\chromedriver.exe")
    option = webdriver.ChromeOptions()
    option.add_experimental_option("debuggerAddress","localhost : 9222")

    driver = webdriver.Chrome(service=s,options=option)
    driver.get(url)
    driver.maximize_window()
    time.sleep(1)

    # select username box and enter username
    driver.find_element(By.ID,"identifierId").send_keys(username)

    # select next button
    driver.find_element(By.ID,"identifierNext").click()
    time.sleep(2)
    # select password box
    email_password = driver.find_element(By.NAME,"Passwd")
    email_password.click()
    email_password.send_keys(password)
    


    # select password next button
    driver.find_element(By.ID,"passwordNext").click()
    time.sleep(3)

    print("Logged in successfully")

    # Proceed further
    driver.find_element(By.CLASS_NAME,"J-Ke n0").click()
    time.sleep(1)




################################################
# Function Name : main 
# Description : function where execution starts
# Input : 
# Output : 
# Author : Narendra Mahadev Kachare
# Date : 03/12/2023
################################################
def main():
    print("Automation script by Narendra Kachare")
    Connection = is_connected()
    if Connection == True:
        print("Internet is ON proceed further")
        login_to_gmail()
    else:
        print("No any internet connectivity")
        exit()


################################################
# Starter kit
################################################
if __name__ == "__main__":
    main()