import tiles

def movement():
    '''Determines where the charcter will move'''
    global x, y
    thinking = True
    warning = "You have reached the edge of the map!"
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
      except Exception as e:
        print(f"An error occured during movement: {e}")
      else:
        print("Movement completed successfully")
      finally:
        print("Movement finished")

def describe_setting(setting):
    '''Describes the setting of the block'''
    try:
     print(f"You are in the {setting}. {tiles.tile[setting]['Description']}")
    except Exception as e:
      print(f"An error occured while describing setting: {e}")
    else:
      print("Setting described successfully")
    finally: 
      print("Setting described completed")

# loop through the map and describe the setting when the character moves into a block
while True:
  try:
    setting = tiles.map[y][x]
    tiles.describe_setting(setting)
  except Exception as e:
    print(f"An error occured while playing: {e}")
    break
  else:
    print("Game continue successful")
  
    