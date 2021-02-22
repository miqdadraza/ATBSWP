#!/usr/bin/env python3

import re, pyperclip
                                # Create a regex for phone numbers #

phoneRegex = re.compile(r'''(
                                  # 415-555-0000, 444-0000, (415) 555-0000, 555-0000 ext 12345, ext. 12345, x12345

((\d\d\d) | (\(\d\d\d\)))?        # area code (optional) (paranthesis denote groups. so it could be 444 OR (444). This whole group is in paranthesis with a ? meaning all of this is optional, can appear 0 or 1 time)
(\s | -)?                         # first seperator, all in paranthesis meaning a group, ? meaning can appear 0 or 1 time
\d\d\d                            # first 3 digits
-                                 # seperator
\d\d\d\d                          # last 4 digits
(((ext(\.)?\s) | x)               # extension word part (optional). could be ext. or ext with a space
(\d{2,5}))?                       # extension number part. the whole extension group is optional
)''', re.VERBOSE)                  #verbose lets you do triple quoted string

# re.compile(r'((\d\d\d) | (\(\d\d\d\)))(\s | -)?\d\d\d-\d\d\d\d(((ext(\.)?\s) | x)(\d{2,5}))?') without verbose mode
#-----------------------------------------------------------------------------------------------------------------------#

#Create a regex for email addresses #
emailRegex = re.compile('''
#some.+_thing@some.+_thing.comedunetgov

[a-zA-Z0-9_.+]+                   # name part, range is all letters and numbers and + and period. the plus at the end means 1 or more of those characters
@                                 # @ symbol
[a-zA-Z0-9_.+]+                   # domain name part
''', re.VERBOSE)


# Get text off clipboard
text = pyperclip.paste()

#Extract email and phone numbers from this text
extractedPhone = phoneRegex.findall(text) #will return list of tuples, one string for each groups. Way to solve is to cover everything in a group. this way, the first string will be the full phone number, followed by bs
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNumber in extractedPhone: #this for loop will append the 0th index of extractedPhone to a new list
    allPhoneNumbers.append(phoneNumber[0])

# Copy extracted email/phone to the clipboard
results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail) #join takes a list of strings like allphonenumbers and joins together in one single string. new line characted in between all phone numbers

pyperclip.copy(results)