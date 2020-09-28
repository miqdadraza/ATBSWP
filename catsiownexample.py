print("How many cats do you have?")
numCats=input()
try:
    if int(numCats) >=4:
        print("That is a lot of cats")
    else:
        print("I guess that is okay!")
except:
    print("type an integer pls")