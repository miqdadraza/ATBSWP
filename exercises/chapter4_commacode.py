"""
Comma Code
Say you have a list value like this:

spam = ['apples', 'bananas', 'tofu', 'cats']

Write a function that takes a list value as an argument and returns a string with all the items separated by a comma and a space, with and inserted before the last item. For example, passing the previous spam list to the function would return 'apples, bananas, tofu, and cats'. But your function should be able to work with any list value passed to it. Be sure to test the case where an empty list [] is passed to your function.

"""

def joinlist(mylist):
    returnstring = ""
    for value in range(len(mylist)-1):
        returnstring = returnstring + mylist[value] + ", "
    returnstring = returnstring + "and " + mylist[-1]

    return returnstring


inputlist = input("Enter a list of seperated by a space:\n")
convert_to_list = inputlist.split() #this will make the user's input into a list (since it's seperated by space)

try:
    print(joinlist(convert_to_list))
except:
    print("Please input a valid list seperated by spaces.")