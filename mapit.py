import webbrowser, sys, pyperclip

sys.argv # ['mapit.py', '870', 'Valencia', 'St.']

#Check if command line arguments were passed

# basically if the system argument exists, do the first part. Otherwise get it from the clipboard
if len(sys.argv) > 1:
    # ['mapit.py', '870', 'Valencia', 'St.'] -> '870 Valencia St.'
    address = ' '.join(sys.argv[1:]) #this slice equals ['870', 'Valencia', 'St.']
else:
    address = pyperclip.paste()

#https://www.google.com/maps/place/<ADDRESS>

webbrowser.open('https://www.google.com/maps/place/' + address)

