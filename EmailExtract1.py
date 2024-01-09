"""
    Web Automation that extract emails from gmail
"""

imap_server = "imap.gmail.com"
email_addr = "______@gmail.com"
pwd = "______"




################################################
# Python import mmodules
################################################
import imaplib
import email
from urllib import request
from urllib import error
import base64
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
# Function Name : MailExtract 
# Description : function extract mail information
# Input : 
# Output : 
# Author : Narendra Mahadev Kachare
# Date : 1/12/2023
################################################
def MailExtract():
    print("Inside Mail Reader")
    Connection = is_connected()
    if Connection == True:
        print("Internet Connection is ON")
        
        imap = imaplib.IMAP4_SSL(imap_server,993)
        imap.login(email_addr,pwd)

        imap.select("Marvellous/PYTHON")

        _,num = imap.search(None, "ALL")

        separator = "-"*100
        
        # These will display list of mail contents and labels
        print(imap.list())
        
        
        for num in num[0].split():
            try:
                _,data = imap.fetch(num,"(RFC822)")

                raw_msg = data[0][1].decode("utf-8")
                message = email.message_from_string(raw_msg)
                for each in message:
                    print(each)
                
                # print(f"Message Number : {num}")
                # print(f"From : {message.get('From')}")
                print(f"Subject : {message.get('Subject')}")
                # print(f"To : {message.get('To')}")
                # print(f"BCC : {message.get('BCC')}")
                # print(f"Date : {message.get('Date')}")
                print(f"get_all : {message.get('ARC-Message-Signature')}")
            except imaplib.IMAP4.error as aobj:
                print("Error : ",aobj)
            
            # for part in message.walk():
            #     if part.get_content_type() == "text/plain":
            #         print(part.as_string())
            print(separator)
    
        imap.close()

    else:
        print("Internet connection is OFF")
        exit()



################################################
# Function Name : main 
# Description : function where execution starts
# Input : 
# Output : 
# Author : Narendra Mahadev Kachare
# Date : 30/11/2023
################################################
def main():
    print("Automation Script")
    print("Web Automation to fetch mails")

    MailExtract()


################################################
# Starter kit
################################################
if __name__ == "__main__":
    main()
