name='bob'
age=3000
if name=='alice':
    print('hi alice')
elif age<12:
    print('you are not alice, kiddo')
elif age>2000:
    print('unlike you, alice is not an undead, importal vampire')
elif age>100:
   print('you are not alice, grannie')

print('enter a name.')
name=input()
if name: #basically if name is truthy (if name exists)
    print('thank you for entering a name')
else:
    print('enter a valid name.')

#alternate way of doing above
print('enter a name.')
name=input()
if name != "": #if name is not equal to empty string
    print('thank you for entering a name')
else:
    print('enter a valid name.')