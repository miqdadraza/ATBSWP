spam = 0
while spam < 5:
    spam = spam+1
    if spam==3:
        continue #if the condition above is true, it will immediately jump back to the while step, does not evaluate further for this condition
    print("spam is "+str(spam))
