"""
   Pyautogui is automation that automates and controls all automations
"""
################################################
# Python import modules
################################################
import pyautogui
import time

################################################
# Function Name : Autogui 
# Description : function use for pointing and select
# Input : 
# Output : 
# Author : Narendra Mahadev Kachare
# Date : 02/12/2023
################################################
def AutoGUI():
    print("Inside PyAutoGUI")

    # Identify mouse corordinate
    M_Pos = pyautogui.position()
    print(M_Pos)
    
    # move mouse location
    time.sleep(2)
    pyautogui.moveTo(2600,736,1)
    pyautogui

################################################
# Function Name : main 
# Description : function where execution starts
# Input : 
# Output : 
# Author : Narendra Mahadev Kachare
# Date : 02/12/2023
################################################
def main():
    print("AutoGUI Automation Script")
    AutoGUI()


################################################
# Starter kit
################################################
if __name__ == "__main__":
    main()