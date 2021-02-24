#this does not work but this is just for an example

import imapclient
conn = imapclient.IMAPClient('imap.gmail.com', ssl=True) 

conn.login('miqdad@bhurani.net', 'password')
#will get output saying success

conn.select_folder('INBOX', readonly=True)
#will return a whole bunch of stuff
UIDs = conn.search(['SINCE 20-Aug-2015']) #imap syntax for date. search keys in textbook

#calling UIDs will return a list of unique IDs, which are the IDs to the emails

rawMessage = conn.fetch([47474], ['BIDY[]', 'FLAGS']) #complicated syntax

import pyzmail

message = pyzmail.PyzMessage.factory(rawMessage[47474][b'BODY[]'])

message.get_subject() #will get the subject

message.get_address('from') #will get the from address

message.get_address('to')

message.get_address('bcc')

message.text_part #member variable will give if there is a text part
message.html_part == None #may evaluate to true or false

message.text_part.get_payload().decode('UTF-8') #will give the text part of the message


conn.list_folders() #will show tuple of all folders

conn.select_folder('INBOX', readonly=False) #will allow us to modify the folder

UIDS = conn.search([ON 24-Aug-2015])
#calling UIDs will show list

conn.delete_messages(UIDs) #will delete all