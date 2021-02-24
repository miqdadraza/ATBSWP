import pprint #pretty print module

message="It was a bright cold dat in April, and the clocks were striking thirteen."
count={} # "r":12 if r appears 12 times

for character in message.upper(): # will call uppercase to whole string
    count.setdefault(character,0) # if a key doesnt exist for a particular letter, set it to zero. 
    count[character] = count[character] + 1

pprint.pprint(count)

text=pprint.pformat(count)
print("This is a test of the pprint format module function")
print(text)



#basically what this program does is that it first starts off with a sting and an empty dictionary. The for loop then assigns the character as a key inside the dictionary. At the beginning, the first time it sees the key, it will asign it a zero value, and then every time it sees the character, it will increase it by 1.