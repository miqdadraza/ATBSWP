"""
def spam():
    eggs = 31337

spam()
# print(eggs) #this program errors out because this is calling a global scope. the eggs variable is in a local scope and is destroyed as soon as the spam function returns
"""

"""
def newspam(): #showing local scopes cannot use variables in other local scopes
    eggs = 99
    bacon()
    print(eggs)


def bacon():
    ham=101
    eggs=0

newspam() #prints 99 because once the bacon function call in newspam is returned, local variable eggs=0 is destroyed
"""

"""
#global variables can be read from local scope
def newnewspam():
    print(neweggs)

neweggs=42
newnewspam()
print(neweggs) #both give the same value because the newnewspam is reading from the global scope
"""

"""
#local and global variables with the same name
def spam():
    eggs = "spam local"
    print(eggs) #will print the spam local

def bacon():
    eggs="bacon local"
    print(eggs) #will print bacon local
    spam() #eggs in here is destroyed as soon as function returns
    print(eggs) #will still print bacon local

eggs="global"

bacon()
print(eggs)
"""



"""adding global variable in local scope (function)

def spam():
    global eggs
    eggs="spam"

eggs="global"
spam() #when this function is called, the eggs in the function becomes a global variable because of the global eggs line
print(eggs)
"""




