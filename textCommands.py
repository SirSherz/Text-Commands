# Sherzah Tahir
# Purpose: A script that reads the emails sent as text messages from the phone,
# and then updates the calander and excel spreadsheet based on the commands.

import imaplib, email, oauth2client, httplib2, os, datetime
import dateutil.parser as parser

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from os import path

SCOPES = 'https://www.googleapis.com/auth/calendar'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Text-Command'

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
# This function checks if the credential are correct. #
#-----------------------------------------------------#
def get_credentials():
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,'text-command-cred.json')

    store = oauth2client.file.Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials

#-----------------------------------------------------#
# This function creates an event in the google        #
# calander.                                           #
#-----------------------------------------------------#
def create_event(event_list):
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('calendar', 'v3', http=http)

    event = {
      'summary': event_list[1] + ' ' + event_list[2],
      'location': '',
      'description': 'Lawn Care',
      'start': {
        'dateTime': event_list[4],
        'timeZone': 'America/New_York',
      },
      'end': {
        'dateTime': event_list[5],
        'timeZone': 'America/New_York',
      },
      'reminders': {
        'useDefault': False,
        'overrides': [
          {'method': 'email', 'minutes': 48 * 60},
          {'method': 'popup', 'minutes': 4 * 60},
        ],
      },
    }

    event = service.events().insert(calendarId='primary', body=event).execute()
    print ('Event created: %s' % (event.get('htmlLink')))

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
                
#-----------------------------------------------------#
# This function takes a list of integers, and uses    #
# the emails respective to those integers. 1 being    #
# the first email, and so forth. Then sends the msg   #
# and date to the respective function for further     #
# processing.                                         #
#-----------------------------------------------------#               
def get_email_date(email_list):
        for i in range(0, (len(email_list))):
                result_email, data_email = mail.fetch(str(email_list[i]), 'RFC822')
                raw_email = email.message_from_string(data_email[0][1])
                stir = get_body(raw_email)
                date_text = raw_email['Date']
                date = parser.parse(date_text)
                date = date.isoformat()
                yourdate = parser.parse(date)
                which_condition(stir, yourdate)

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
# This function checks if condition 1 or 2 is send.   #
#-----------------------------------------------------#
def which_condition(text, date):
        if(text[0] == '1'):
                condition_1(text, date)
        else:
                condition_2(text)

#-----------------------------------------------------#
# If the command is 1 then 4 fields are required from #
# text message.                                       #
#-----------------------------------------------------#
def condition_1(text, date):
        cmd, first_name, last_name, num_days = text.split()
        event_list = [cmd, first_name, last_name, num_days]
        newdate = date - datetime.timedelta(hours=4)
        newdate = newdate + datetime.timedelta(days=int(num_days))
        enddate =  newdate + datetime.timedelta(hours=1)
        enddate = enddate.isoformat()
        newdate = newdate.isoformat()
        event_list.append(newdate)
        event_list.append(enddate)
        create_event(event_list)

#-----------------------------------------------------#
# If the command is 2 then 5 fields are required from #
# text message.                                       #
#-----------------------------------------------------#
def condition_2(text):
        cmd, first_name, last_name, stir, num_dollars = text.split()
        event_list = [cmd, first_name, last_name, stir, num_dollars]
        print  event_list

# This searches for all unread messages in our selected folder. 
result_email, data_email = mail.search(None, '(UNSEEN)')

# This takes the string of data that correlates to the unread emails, and splits it into an actual list of ints
unread_email_list = data_email[0].split()

# This function takes the list of emails, and prints the contents to a file. 
get_email_date(unread_email_list)
