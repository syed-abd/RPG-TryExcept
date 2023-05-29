##############################################################################
# Title: Class of the Elite
# Assignment: RPG-Try/Except                                                               
# Class: Computer Science 30                                                            
# Date:  May 15th, 2023                                                               
# Coders Name: Abullah Hashmi                                                      
# Version: 001   
##############################################################################
''' This code allows character to access the inventory with items in it 
kkko
okloo'''

import tiles
from inventory import *

def movement():
    '''Determines where the charcter will move'''
    global x, y
    thinking = True
    while thinking:
      try:
        # ask the user where to move next
        direction = input("Where do you want to go? (north, south, west, east) ")
        # update the character's position based on the user's input
        
        if direction == "north":
          if y != 0:
            y -= 1
            thinking = False
          else:
            print(warning)
        elif direction == "south":
          if y != 3:
            y += 1
            thinking = False
          else:
            print(warning) 
        elif direction == "west":
          if y != 0:
            x -= 1
            thinking = False
          else:
            print(warning)
        elif direction == "east":
           if y != 4:
             x += 1
             thinking = False
           else:
            print(warning)
        else:
          print("Invalid")
      finally:
        print("Continuing")

# define the starting position of the character
x, y = 0, 0
  
# create two inventories using nested dictionaries
objects = {
    "pencil": {"description": "A sharp tip for combat", "location": "classroom"},
    "potion": {"description": "A potion that restores health", "location": [None, None]},
    "book": {"description": "A book filled with ancient knowledge", "location": [None, None]}, 
    "key": {"description": "A key that unlocks a mysterious door", "location": [None, None]}
}

def search():
    for obj in objects:
        if objects[obj]["location"] == tiles.map[x][y]:
            print(f"You have found {obj}!")
            print(f"{objects[obj]['description']}")
            inventory.take_item(obj)

try:
# ask the user where to move next
  mainMenu = input("What do you want to do? (walk, inventory, drop item)")
  
    # update the character's position based on the user's input
  if mainMenu == "walk":
        movement()
        search()
  elif mainMenu == "inventory":
        access_inventory()
  elif mainMenu == "drop item":
        drop_item()
  else:
        print("Invalid")
finally:
        print("Existing")
