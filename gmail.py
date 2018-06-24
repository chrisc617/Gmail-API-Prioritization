
from __future__ import print_function
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
from datetime import datetime, timedelta
import base64
import email
from nltk.tokenize import RegexpTokenizer,word_tokenize
from nltk.corpus import stopwords
from collections import Counter
from nltk.util import ngrams



# Setup the Gmail API
SCOPES = 'https://www.googleapis.com/auth/gmail.readonly'
store = file.Storage('credentials.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
    creds = tools.run_flow(flow, store)
service = build('gmail', 'v1', http=creds.authorize(Http()))

#Labels we are interested in
label_ids=['UNREAD','INBOX']
important_ids=['STARRED']
# Call the Gmail API

#Will retrieve all unread email messages from the inbox. You have to select which labels you want to select from
def initial_list_of_messages(a):
    response = service.users().messages().list(userId='me', labelIds=a).execute()
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

#Does a check on the time to determine if the message has been received within the last three days. This function will drive what initial list you choose from
def list_recent_messages(a):
    list_of_recent_message_ids=[]
    today = datetime.today()
    margin = timedelta(days = 3)
    for id in initial_list_of_messages(a):
        if today-margin <=get_msg_time(id['id']): #double check please
            list_of_recent_message_ids.append(id['id'])
        else:
            pass
    print(list_of_recent_message_ids)
    return list_of_recent_message_ids

def retrieve_contents_of_message(message_id):
        message = service.users().messages().get(userId='me', id=message_id).execute()
        msg_content={}
        headers=message['payload']['headers']

        for i in headers:
            if i['name'] == 'Subject':
                msg_content['Subject'] = i['value']
            elif i['name'] == 'Date':
                msg_content['Date'] = i['value']
            elif i['name'] == 'From':
                msg_content['From'] = i['value']
            else:
                pass
        msg_content['Snippet']=message['snippet']
        info= f'''
        ---------------------------------------------------------------------------------------------------------------
        Date: {msg_content['Date']}
        From: {msg_content['From']}
        Subject: {msg_content['Subject']}
        Snippet: {msg_content['Snippet']}
        --------------------------------------------------------------------------------------------------------------- '''
        print(info)
#Used to parse the message to get the body. Will only be used for NLTK purposes. Referenced https://stackoverflow.com/questions/34514629/new-python-gmail-api-only-retrieve-messages-from-yesterday
def message_converter(message_id):
        message = service.users().messages().get(userId='me', id=message_id,format='raw').execute()
        msg_str = str(base64.urlsafe_b64decode(message['raw'].encode('ASCII')),'UTF-8')
        mime_msg = email.message_from_string(msg_str)
        if mime_msg.is_multipart():
            for payload in mime_msg.get_payload():
                try:
                    if payload.get_content_type() == 'text/plain': #referenced Stackoverflow so that I could parse through and only receive text back https://stackoverflow.com/questions/1463074/how-can-i-get-an-email-messages-text-content-using-python
                        print(payload.get_payload())
                        return (payload.get_payload())
                except:
                    pass

bucket_of_words=[]
#This function was written to append each word into my final list that is not a stop word. NLTK documentation was reviewed.
def word_tokenizer(input,wordbucket=bucket_of_words):
    try:
        tokenizer = RegexpTokenizer(r'\w+')
        stop_words=set(stopwords.words('english'))
        stop_words.update(['html','com','https','unsubscribe','http','subject','www','email','click','us','org','image','inline'])
        wordlist=tokenizer.tokenize(input)
        wordlist=[w.lower() for w in wordlist]
        keywords=[w for w in wordlist if w not in stop_words and len(w)>2]
        for i in keywords:
            wordbucket.append(i)
    except:
        pass

#This script will return the five most common words from our messages. most common 10 is just an arbitrary number
def most_common_words():
    for message in initial_list_of_messages(important_ids):
        word_tokenizer(message_converter(message['id']))
    print(Counter(bucket_of_words).most_common(10))
    return (Counter(bucket_of_words).most_common(10))

# important_words=most_common_words()
# msg_importance={}
# for messages in list_recent_messages(label_ids):
#     count=0
#     bucket_of_all_words=[]
#     word_tokenizer(message_converter(messages),bucket_of_all_words)
#     for i in important_words:
#         if i[0] in bucket_of_all_words:
#             count +=int(i[1])
#     msg_importance[messages]=count
# print(msg_importance)
#



# for i in most_common_words():
#     print(i[0])
message_converter('1642ea686349277d')
