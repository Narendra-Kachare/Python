"""
    Web Automation that extract emails from gmail
"""
################################################
# Python import modules
################################################
from selenium import webdriver
from urllib import request,error
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

################################################
# Global varibles
################################################
username = 'narendrakachare7@gmail.com'
password = 'Narendra15@'
url = "https://mail.google.com/mail/u/0/#label/Marvellous%2FPYTHON"

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
# Function Name : download_protected_pdf 
# Description : function download gmail pdf attachement
# Input : 
# Output : 
# Author : Narendra Mahadev Kachare
# Date : 02/12/2023
################################################

def download_protected_pdf(email, password, subject_keyword):
    # Create a new instance of the Chrome driver
    driver = webdriver.Chrome()

    try:
        s = Service(r"D:\API\chromedriver.exe")
        option = webdriver.ChromeOptions()
        option.add_experimental_option("debuggerAddress","localhost : 9222")

        driver = webdriver.Chrome(service=s,options=option)
        driver.get(url)
        driver.maximize_window()
        time.sleep(1)

        # # select username box and enter username
        # driver.find_element(By.ID,"identifierId").send_keys(username)

        # # select next button
        # driver.find_element(By.ID,"identifierNext").click()
        # time.sleep(2)
        # # select password box
        # email_password = driver.find_element(By.NAME,"Passwd")
        # email_password.click()
        # email_password.send_keys(password)
        


        # # select password next button
        # driver.find_element(By.ID,"passwordNext").click()
        # time.sleep(3)

        print("Logged in successfully")

        # # Search for emails with the specified subject
        # search_box = driver.find_element(By.NAME, "q")
        # search_box.send_keys(f"subject:{subject_keyword}")
        # search_box.send_keys(Keys.RETURN)

        # # Click on the first email (assumes the desired PDF is in the first email)
        # first_email = driver.find_element(By.CSS_SELECTOR, '.zA[role="link"]')
        # first_email.click()

        # Download the PDF attachment (modify the selector based on the actual HTML structure)
        download_button = driver.find_element(By.CSS_SELECTOR, '[download]')
        download_button.click()

        # Wait for the download to complete
        time.sleep(10)

    finally:
        # Close the browser window
        driver.quit()


################################################
# Function Name : main 
# Description : function where execution starts
# Input : 
# Output : 
# Author : Narendra Mahadev Kachare
# Date : 02/12/2023
################################################
def main():
    # open_gmail_in_browser()
    user = "narendrakachare7@gmail.com"
    password = "avboaxahzanvntxg    "
    sub = "Marvellous"

    # login_to_gmail(Email,password)

    download_protected_pdf(user,password,sub)





################################################
# Python Starter kit
################################################
if __name__ == "__main__":
    main()