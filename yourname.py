name = ""
while name != "your name":
    print("please type your name.")
    name=input() #will keep going until name is "your name"
print("Thank you")


#break statement
name=""
while True:
    print("please enter your name")
    name=input()
    if name=="your name":
        break
print("thanks")