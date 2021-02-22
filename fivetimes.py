print("my name is")
for i in range(5):
    print("Jimmy Five Times "+ str(i+1))

total=0
for num in range(101):
    total=total+num #when for loop is executed, starts with 0 all the way up to 100, not including 101
print(total)


"""
below is another way of doing fivetimes, using a while loop
"""

print("My name is")
w = 0
while w<5:
    print("jimmy 5 times"+str(w))
    w=w+1

p = range(10) #checking what range is
print(p)

"""trying out the range function for diff numbers"""

print("my name is")
for q in range(5,18):
    print("Jimmy Five Times "+ str(q)) #evaluates from 5 to 18, not including 18

#three argument range function
print("my name is")
for h in range(5,18,3):
    print("Jimmy Five Times "+ str(h)) #evaluates from 5 to 18, not including 18
#third argument in range is step value

"""with a negative step, it counts down"""
print("my name is")
for o in range(5,-34,-3):
    if o == -25:
        continue #when o is equal to -25, will go back to the for loop
    print("Jimmy Five Times "+ str(o)) #evaluates from 5 to 18, not including 18
    
#third argument in range is step value


"""break in for loops"""
print("my name is")
for u in range(5,-34,-3):
    if u == -25:
        break #when o is equal to -25, will stop the for loop
    print("Jimmy Five Times "+ str(u)) #evaluates from 5 to 18, not including 18
