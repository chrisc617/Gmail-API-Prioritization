"""
Shows basic usage of the Gmail API.

Lists the user's Gmail labels.
"""
from __future__ import print_function
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
from datetime import datetime, timedelta

# Setup the Gmail API
SCOPES = 'https://www.googleapis.com/auth/gmail.readonly'
store = file.Storage('credentials.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
    creds = tools.run_flow(flow, store)
service = build('gmail', 'v1', http=creds.authorize(Http()))

#Labels we are interested in
label_ids=['INBOX', 'UNREAD']
# Call the Gmail API

#Will retrieve all unread email messages from the inbox
def initial_list_of_messages():
    response = service.users().messages().list(userId='me', labelIds=label_ids).execute()

    list_of_message_ids = response.get('messages')
    return list_of_message_ids

#Used to get the time the message was sent
def get_msg_time(message_id):
    message = service.users().messages().get(userId='me', id=message_id).execute()
    msg_date=message['payload']['headers'][1]['value']
    msg_date=msg_date.split(';')
    msg_date=(msg_date[1].strip()).replace(",","")
    msg_date=datetime.strptime(msg_date,'%a %d %b %Y %H:%M:%S -0700 (PDT)')
    return msg_date

#Does a check on the time to determine if the message has been received within the last three days
def list_recent_messages():
    list_of_recent_message_ids=[]
    today = datetime.today()
    margin = timedelta(days = 3)
    for id in initial_list_of_messages():
        if today-margin <=get_msg_time(id['id']): #double check please
            list_of_recent_message_ids.append(id['id'])
        else:
            pass
    return list_of_recent_message_ids

list_recent_messages()
