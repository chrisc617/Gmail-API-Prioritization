# Project Planning

## Problem Statement

I will be trying to solve the issue of prioritizing emails that are deemed to be higher priority. Some people get up to hundreds of emails a day and it makes it hard to determine which are important before even reading them. The goal of this project will be to help the user determine which unread emails are of the highest priority.

The primary user of this application will be myself, and anyone with a gmail account (I will start with gmail and perhaps move onto other email hosts at a later time). The user will need to help manage their unread email message inbox. The program will be able to identify which emails are considered high importance. The desired functionality is that the application will output unread emails in order of their importance. Importance will be scored based on the number of keywords it touches upon from your 'starred' label...Key words will be determined by frequency of apparence, and more frequent key words will be considered more important. It is difficult to manage your own inbox. There are a ton of rules one can apply to map emails to certain folders, but it can often get confusing to track your emails if you start to input too many rules. The application will be able to use smarter rules to organize your important emails and also learn to better identify what is high priority for you at a specific time.
Provide a description of the problem your project is trying to solve, including statements of user needs and descriptions of "as-is" and "to-be" processes.

**Process as is:**
1. User opens email (after long meeting or beginning of day)
2. User sifts through all emails to catch-up (Can take anywhere from 15 minutes-hours depending on how many emails received)
3. User then plans day

**Process to be**
1. User opens email (after long meeting or beginning of day)
2. User runs application (All it takes is the run time of the application)
3. User can take care of most important emails by simply running down the list

## Information Requirements

Identify the application's information inputs and information outputs.

If you get stuck, think about the following questions:

What information inputs does the system require in order to achieve its desired functionality? Where do these inputs come from? What is the data format of these inputs?
What information outputs does the system produce in the process of achieving its desired functionality? What will be the data format of these outputs?

### Information Inputs

Inputs it will require is an email address and password. Another input may also be to label certain items as high priorities (ex. the name of a project your are working on). An ideal state would be for the user to star emails that they have deemed important in the past; therefore, the application will pick up on that pattern and immediately know that it is important. My hesitation with this method is that there are so many reasons why someone would star an email, thus making it unrealiable as an indicator of priority.



### Information Outputs

The output will be snippets of your email that is sorted from the highest priority to the lowest priority.

## Technology Requirements

### APIs and Web Service Requirements

I just need access to my gmail to get this working.

### Python Package Requirements

The application will require pytest for testing.

It may also require the imaplib module to connect to the email server, NLTK to interpret the email, and time to identify which emails are more time relevant.
### Hardware Requirements

I will only need my laptop for hardware.
