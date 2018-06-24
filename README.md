# Gmail-API-Prioritization
06-24-2018
# API Setup
In order to get this application working, you first must need to install the google API client and have a gmail account. Instructions can be found [Google API Key](https://developers.google.com/gmail/api/quickstart/python)



# Requirements
Install package dependencies using one of the following commands, depending on how you have installed Python and how you are managing packages:

```sh
# Pipenv on Mac or Windows:
pipenv install -r requirements.txt

# Homebrew-installed Python 3.x on Mac OS:
pip3 install -r requirements.txt

# All others:
pip install -r requirements.txt
```

# Folder
As the same with the instructions from the Google Developers site, your client_secret.json file and credentials.json file should be in the same directory as the python code.

# Gmail 
In order for the application to function properly, you must have emails under your 'STARRED' label and 'UNREAD' in your 'INBOX'. If your most important emails are stored under a separate label, update variable **important_ids**, which can be found in line 25, to the label of your choice.

Messages will be pulled from your unread inbox. If you have no unread messages, then the code will not pull anything.
