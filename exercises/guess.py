# This is a number guessing game

import random

print("Hello, what is your name?")
name = input()

print("Well " + str(name) + ", I am thinking of a number between 1 and 20!")
secretnumber = random.randint(1,20) #generate a random number between 1 and 20, including 1 and 20

print("DEBUG: Secret number is "+ str(secretnumber) + ".") #for debugging purposes

for guessesTaken in range(1,23): #will continue looping 22 times
    print("Take a guess!")
    guess = int(input())

    if guess < secretnumber:
        print("Your guess was too low")
    elif guess > secretnumber:
        print("Your guess is too high")
    else:
        break #loop will end if all 6 iterations are complete, or if the number was guessed

if guess == secretnumber:
    print("That is right. The number I was guessing was " + str(secretnumber) + "! You guessed it in "+ str(guessesTaken) + " tries.")
else:
    print("You took "+ str(guessesTaken) + " guesses. The number I was thinking of was " + str(secretnumber) + "!")