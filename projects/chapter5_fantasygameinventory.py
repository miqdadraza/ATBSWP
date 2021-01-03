"""

Fantasy Game Inventory
You are creating a fantasy video game. The data structure to model the player’s inventory will be a dictionary where the keys are string values describing the item in the inventory and the value is an integer value detailing how many of that item the player has. For example, the dictionary value {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12} means the player has 1 rope, 6 torches, 42 gold coins, and so on.

Write a function named displayInventory() that would take any possible “inventory” and display it like the following:

Inventory:
12 arrow
42 gold coin
1 rope
6 torch
1 dagger
Total number of items: 62

Hint: You can use a for loop to loop through all the keys in a dictionary.

# inventory.py
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        # FILL THIS PART IN
    print("Total number of items: " + str(item_total))

displayInventory(stuff)

"""

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
    item_total = 0
    for item, quantity in inventory.items(): #iterate over key and value
        print(str(quantity) + " " + item)
        item_total += quantity
    print("Total number of items: " + str(item_total))

#displayInventory(stuff)

"""
List to Dictionary Function for Fantasy Game Inventory
Imagine that a vanquished dragon’s loot is represented as a list of strings like this:

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

Write a function named addToInventory(inventory, addedItems), where the inventory parameter is a dictionary representing the player’s inventory (like in the previous project) and the addedItems parameter is a list like dragonLoot. The addToInventory() function should return a dictionary that represents the updated inventory. Note that the addedItems list can contain multiples of the same item. Your code could look something like this:

def addToInventory(inventory, addedItems):
    # your code goes here

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
"""

def addToInventory(inventory, addedItems):
    for item in addedItems:
        inventory.setdefault(item,0) #setdefault method checks to see if key exists in dict. If it exists, it will return the value of the key. If it does not exist, it will create one and value will be whatever provided. Here it is 0
        inventory[item] +=1 #above line will set it to zero, this line will add one
    return inventory


inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)