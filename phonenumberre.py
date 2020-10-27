import re
#verbose more means white space and comments are ignored
re.compile(r'''
(\d\d\d-) |  #area code
(\(\d\d\d\) ) # or area code with parenthesis and no days
\d\d\d   #second 3 digits
-
\d\d\d\d   #last 4 digits
\sx\d{2,4}  #extension like x1234''', re.VERBOSE | re.DOTALL | re.IGNORECASE)