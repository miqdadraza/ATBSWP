"""
Sandwich Maker
Write a program that asks users for their sandwich preferences. The program should use PyInputPlus to ensure that they enter valid input, such as:
Using inputMenu() for a bread type: wheat, white, or sourdough.
Using inputMenu() for a protein type: chicken, turkey, ham, or tofu.
Using inputYesNo() to ask if they want cheese.
If so, using inputMenu() to ask for a cheese type: cheddar, Swiss, or mozzarella.
Using inputYesNo() to ask if they want mayo, mustard, lettuce, or tomato.
Using inputInt() to ask how many sandwiches they want. Make sure this number is 1 or more.
Come up with prices for each of these options, and have your program display a total cost after the user enters their selection.
"""

import pyinputplus as pyip
import numpy as np

#choices of bread
bread = {'wheat': 5,
          'white': 3,
          'sourdough': 3.5}
bread_input = list(bread.keys()) #for the input menu

#choices of protein
protein = {'chicken': 2,
            'turkey': 3,
            'ham': 2.5,
            'tofu': 1}
protein_input = list(protein.keys()) #for the input menu

#choices of cheese
cheese = {'cheddar': 1,
            'swiss': 2,
            'mozzarella': 2.5}
cheese_input = list(cheese.keys()) # for the input menu

#choices of condiments
condiments = {'mayo': 0.5,
                'mustard': 0.5,
                'lettuce': 0,
                'tomato': 0}

all_items = {}
all_items.update(**bread,**protein,**cheese,**condiments) #making a dictionary of all the items and their prices.

customer_choices = [] #empty list for all the customer choices

print("Welcome to the Umbrella Subs and Clubs Shop")

customer_bread = pyip.inputMenu(choices=bread_input, prompt="What kind of bread would you like?\n")
customer_choices.append(customer_bread) #adding bread to the list of customer choices

customer_protein = pyip.inputMenu(choices=protein_input, prompt="What kind of protein would you like?\n")
customer_choices.append(customer_protein) #adding protein to the list of customer choices


customer_cheese_yesno = pyip.inputYesNo(prompt="Would you like cheese?") #asking for cheese
if customer_cheese_yesno == 'yes': #will only execute if cheese is added
    customer_cheese = pyip.inputMenu(cheese_input, prompt="What kind of cheese would you like?")
    customer_choices.append(customer_cheese) #adding cheese to the order list


customer_condiments = [] #empty condiments list
mayochoice = pyip.inputYesNo(prompt="Would you like mayo?")
if mayochoice == 'yes':
     customer_condiments.append("mayo")

mustardchoice = pyip.inputYesNo(prompt="Would you like mustard?")
if mustardchoice == 'yes':
     customer_condiments.append("mustard")

lettucechoice = pyip.inputYesNo(prompt="Would you like lettuce?")
if lettucechoice == 'yes':
     customer_condiments.append("lettuce")

tomatochoice = pyip.inputYesNo(prompt="Would you like tomato?")
if tomatochoice == 'yes':
     customer_condiments.append("tomato")

final_customer_choices = customer_choices + customer_condiments #final choices, addition of condiments into original list
#print(final_customer_choices)

print("Your choice of sandwich today is:") #will show everything ordered
for i in final_customer_choices:
    print (i)

sum = 0 #initializing float for the total cost
for j in final_customer_choices:
    sum += all_items[j]

quantity = pyip.inputInt(prompt="How many of these sandwiches would you like?", min=1) #asking for quantity, minimum 1

sum *= quantity #total sum with multiplication into quantity

print("Your total for the " + str(quantity) + " sandwich order is: $" + str(np.round(sum,2))) #final stuff #rounding not working, need to check