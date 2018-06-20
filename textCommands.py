# Sherzah Tahir
# Purpose: A script that reads the emails sent as text messages from the phone,
# and then updates the calander and excel spreadsheet based on the commands.

import imaplib, email

# The username and password for the gmail account. This can be uploaded from a seprate file, or hard coded into
# the python code. 
gmail_username = ''
gmail_password = ''

# This is to code to connect to the gmail API, using the secured IMAP4_SSL
mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login(gmail_username, gmail_password)
mail.list()

# The folder being searched for. You can create a new folder in your gmail account or use 'INBOX' for inbox.
# The correct spelling of the folder is important. 
mail.select('python')

#-----------------------------------------------------#
# This function takes a list of integers, and prints  #
# the emails respective to those integers. 1 being    #
# the first email, and so forth.                      #
#-----------------------------------------------------#
def print_message_to_file(email_list):
        for i in range(0, (len(email_list))):
                result_email, data_email = mail.fetch(str(email_list[i]), 'RFC822')
                raw_email = email.message_from_string(data_email[0][1])
                stir = get_body(raw_email)
                print type(stir)
                print stir

#-----------------------------------------------------#
# This function takes a raw input of the email, and   #
# pulls just the body of the email, excluding the     #
# headers                                             #
#-----------------------------------------------------#
def get_body(msg):
        if msg.is_multipart():
                return get_body(msg.get_payload(0))
        else:
                return msg.get_payload(None, True)

#-----------------------------------------------------#
# This function checks if condition 1 or 2 is send    #
#-----------------------------------------------------#
#def which_condition(text):



# This searches for all unread messages in our selected folder. 
result_email, data_email = mail.search(None, '(UNSEEN)')

# This takes the string of data that correlates to the unread emails, and splits it into an actual list of ints
unread_email_list = data_email[0].split()

# This function takes the list of emails, and prints the contents to a file. 
print_message_to_file(unread_email_list)
