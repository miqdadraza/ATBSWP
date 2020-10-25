""" def isPhoneNumber(text):
    if len(text) != 12:
        return False #not phone number size
    for i in range(0,3):
        if not text[i].isdecimal():
            return False #no area code
    if text[3] != '-':
        return False
    for i in range(4,7):
        if not text[i].isdecimal():
            return False #no first 3 digits
    if text[7] != '-':
        return False # missing second dash
    for i in range(8,12):
        if not text[i].isdecimal():
            return False #missing last 4 digits
    return True

message= "Call me at 415-555-1011 tomorrow, or at 415-555-9999 for my office line"

foundNumber=False
for i in range(len(message)):
    chunk = message[i:i+12] #will start with i=0, so it will go from 0:12, next will be 1:13, etc
    if isPhoneNumber(chunk):
        print('Phone number found: ' + chunk)
        foundNumber = True
if not foundNumber:
    print("Could not find any phone number")

print(isPhoneNumber('hello')) """

# All of this could be simplified by this:

import re

message= 'Call me at 415-555-1011 tomorrow, or at 415-555-9999 for my office line'

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') #looking for that pattern, the r is a raw string because we are using the backslash. regex use a lot of backslashes. \d is digit. the re.compile creates a regex object
mo = phoneNumRegex.search(message) #for single matching object (mo) occurence. regex data type has a search method
print(mo.group()) # match objects have method called group which will tell you the actual text.
#specify patter, search string, print

no = phoneNumRegex.findall(message) #findall returns a list of all messages available
print(no)


