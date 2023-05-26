# add empty list for inventory
inventory = []

# define a function to access the inventory
def access_inventory():
  try:
    if not inventory:
        print("Your inventory is empty.")
    else:
        print("Your inventory contains:")
        for item in inventory:
            print(f"- {item}")
  except Exception as e:
    print(f"Something went wrong while accessing the inventory: {e} ")
  else: 
    print("Inventory successfully accessed")
  finally:
    print("Inventory access completed")

# define a function to add an item to the inventory
def take_item(object):
    global inventory
    answer = input(f"Do you want to keep the {object}? (yes, no)")
    if answer == "yes":
        inventory.append(object)
        print(f"You have taken the {object}.")
    elif answer == "no":
        print(f"You did not take the {object}")
    else:
        print("Invalid choice")
        take_item(object)

# define a function to remove an item from the inventory
def drop_item():
    global inventory
    if not inventory:
        print("Your inventory is empty.")
    else:
        print("Which item do you want to drop?")
        for item in inventory:
            print(item)
        item_choice = input()
        if item_choice not in inventory:
            print("Invalid item.")
        else:
            inventory.remove(item_choice)
            print(f"You have dropped the {item_choice}.")