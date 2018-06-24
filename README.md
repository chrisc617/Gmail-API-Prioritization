# Gmail-API-Prioritization
06-24-2018
# API Setup
In order to get this application working, you first must need to install the google API client and have a gmail account. Instructions can be found [Google API Key](https://developers.google.com/gmail/api/quickstart/python). Below is a snippet of the instructions.

Step 1: Turn on the Gmail API
* Use this wizard to create or select a project in the Google Developers Console and automatically turn on the API. Click Continue, then * Go to credentials.
* On the Add credentials to your project page, click the Cancel button.
* At the top of the page, select the OAuth consent screen tab. Select an Email address, enter a Product name if not already set, and click the Save button.
* Select the Credentials tab, click the Create credentials button and select OAuth client ID.
* Select the application type Other, enter the name "Gmail API Quickstart", and click the Create button.
* Click OK to dismiss the resulting dialog.
* Click the file_download (Download JSON) button to the right of the client ID.
* Move this file to your working directory and rename it client_secret.json.

Step 2: Install the Google Client Library
* Run the following command to install the library using pip:

```sh
pip install --upgrade google-api-python-client
```
* See the library's installation page for the alternative installation options.



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
