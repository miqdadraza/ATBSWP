#this program was made with help of stackoverflow: https://stackoverflow.com/questions/60658830/automate-the-boring-stuff-coin-flip-streaks


"""
Coin Flip Streaks
For this exercise, we’ll try doing an experiment. If you flip a coin 100 times and write down an “H” for each heads and “T” for each tails, you’ll create a list that looks like “T T T T H H H H T T.” If you ask a human to make up 100 random coin flips, you’ll probably end up with alternating head-tail results like “H T H T H H T H T T,” which looks random (to humans), but isn’t mathematically random. A human will almost never write down a streak of six heads or six tails in a row, even though it is highly likely to happen in truly random coin flips. Humans are predictably bad at being random.

Write a program to find out how often a streak of six heads or a streak of six tails comes up in a randomly generated list of heads and tails. Your program breaks up the experiment into two parts: the first part generates a list of randomly selected 'heads' and 'tails' values, and the second part checks if there is a streak in it. Put all of this code in a loop that repeats the experiment 10,000 times so we can find out what percentage of the coin flips contains a streak of six heads or tails in a row. As a hint, the function call random.randint(0, 1) will return a 0 value 50% of the time and a 1 value the other 50% of the time.

You can start with the following template:

import random
numberOfStreaks = 0
for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.

    # Code that checks if there is a streak of 6 heads or tails in a row.
print('Chance of streak: %s%%' % (numberOfStreaks / 100))

Of course, this is only an estimate, but 10,000 is a decent sample size. Some knowledge of mathematics could give you the exact answer and save you the trouble of writing a program, but programmers are notoriously bad at math.

"""

import random

number_of_streaks_of_6 = 0
H_or_T = []
repetition = 0

for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.    
    for i in range (100): #will create a 100 value list of randoms (0 or 1 represent H or T)
        H_or_T.append(random.randint(0,1))
        #print(H_or_T)

    # Code that checks if there is a streak of 6 heads or tails in a row.
    for j in range(len(H_or_T)):
        if H_or_T[j] == H_or_T[j-1]:
            repetition+=1

        if repetition == 6:
            number_of_streaks_of_6 +=1
    H_or_T = [] #need to reset list of program will crash (or keep going forever until 10000 times). Reset because once number of streaks of 6 and repetition are filled, it's no longer needed

print('Chance of streak: %s%%' % (number_of_streaks_of_6 / 100))


#print(H_or_T)

"""Another solution from user on stackoverflow:"""
import random
numStreaks = 0
test = 0
flip = []

#running the experiment 10000 times

for exp in range(10000):
    for i in range(100): #list of 100 random heads/tails

        if random.randint(0,1) == 0:
            flip.append('H')
        else:
            flip.append('T')

    for j in range(100): #checking for streaks of 6 heads/tails

        if flip[j:j+6] == ['H','H','H','H','H','H']:
            numStreaks += 1
        elif flip[j:j+6] == ['T','T','T','T','T','T']:
            numStreaks += 1
        else:
            test += 1 #just to test the prog
            continue
print (test)
chance = numStreaks / 10000
print("chance of streaks of 6: %s %%" % chance )