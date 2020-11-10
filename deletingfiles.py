import os
import send2trash
for filename in os.listdir():
    if filename.endswith('.txt'):
        #os.unlink(filename) #dry run to print to make sure its deleting what you want
        print(filename)


