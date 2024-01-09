"""
    Web Automation that extract emails from gmail
"""
################################################
# Python import modules
################################################
import webbrowser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
################################################
# Function Name : open_gmail_in_browser 
# Description : function opens gmail in browser
# Input : 
# Output : 
# Author : Narendra Mahadev Kachare
# Date : 02/12/2023
################################################
def open_gmail_in_browser():
    # URL for Gmail
    gmail_url = "https://mail.google.com/"

    # Open Gmail in the default web browser
    webbrowser.open(gmail_url)


################################################
# Function Name : login_to_gmail 
# Description : function logins gmail in browser
# Input : 
# Output : 
# Author : Narendra Mahadev Kachare
# Date : 02/12/2023
################################################
def login_to_gmail(email, password):
    # Create a new instance of the Chrome driver
    driver = webdriver.Chrome()

    try:
        # Open Gmail login page
        driver.get("https://mail.google.com/")

        # Find the email input field and enter your email
        email_input = driver.find_element(By.NAME, "identifier")
        email_input.send_keys(email)

        # Click the "Next" button
        next_button = driver.find_element(By.ID, "identifierNext")
        next_button.click()

        # Wait for a while to load the next page
        time.sleep(2)

        # Find the password input field and enter your password
        password_input = driver.find_element(By.NAME, "password")
        password_input.send_keys(password)

    #     # Click the "Next" button
    #     next_button = driver.find_element(By.ID, "passwordNext")
    #     next_button.click()

    #     # Wait for a while to complete the login
    #     time.sleep(5)

    finally:
        # Close the browser window
        driver.quit()

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
        # Open Gmail login page
        driver.get("https://mail.google.com/")

        # Find the email input field and enter your email
        email_input = driver.find_element(By.NAME, "identifier")
        email_input.send_keys(email)

        # Click the "Next" button
        next_button = driver.find_element(By.ID, "identifierNext")
        next_button.click()

        # Wait for a while to load the next page
        time.sleep(2)

        # Find the password input field and enter your password
        password_input = driver.find_element(By.CSS_SELECTOR, 'input[name="password"]')
        password_input.send_keys(password)

        # Click the "Next" button
        next_button = driver.find_element(By.ID, "passwordNext")
        next_button.click()

        # Wait for a while to complete the login
        time.sleep(5)

        # Search for emails with the specified subject
        search_box = driver.find_element(By.NAME, "q")
        search_box.send_keys(f"subject:{subject_keyword}")
        search_box.send_keys(Keys.RETURN)

        # Click on the first email (assumes the desired PDF is in the first email)
        first_email = driver.find_element(By.CSS_SELECTOR, '.zA[role="link"]')
        first_email.click()

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
    Email = "narendrakachare7@gmail.com"
    password = "avboaxahzanvntxg"
    Subject = "Marvellous"

    # login_to_gmail(Email,password)

    download_protected_pdf(Email,password, Subject)





################################################
# Python Starter kit
################################################
if __name__ == "__main__":
    main()