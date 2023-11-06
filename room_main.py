from room_classes import Room
from room_character import Enemy, Friend
from room_item import Cheese, Potions 

#Variables so I don't have to write those lines everytime
which_direction = "\n ☞ Which direction would you like to go? North? ↑ South? ↓ East? → West? ←"
nothing = "\n....There's nothing in here. You should try to go somewhere else.\n"

#Create (=instantiate) rooms and their attributes
kitchen = Room("KITCHEN 🥣")
kitchen.set_description("it's a dank and dirty room, buzzing with flies.")

ballroom = Room("BALLROOM 💃")
ballroom.set_description("you feel like a princess.")

dining_hall = Room("DINING HALL 🥂")
dining_hall.set_description("it makes you hungry...")

study = Room("STUDY 📙") 
study.set_description("a dusty room with a messy desk")

#Create items and their attributes
cheese = Cheese("piece of CHEESE 🧀")
kitchen.set_item(cheese)

potions = Potions("POTIONS 🧪")
dining_hall.set_item(potions)
color_one = "🔵 BLUE"
color_two = "🔴 RED"
       
#Links the rooms
kitchen.link_room(dining_hall, "south") # This links the kitchen to the dining hall
dining_hall.link_room(kitchen, "north") # Go to the empty dictionary on room_classes
dining_hall.link_room(ballroom, "west")
ballroom.link_room(dining_hall, "east")
ballroom.link_room(study, "west")

############################ CREATE CHARACTERS ##########################################
#Creates Dave
dave = Enemy("🧟 DAVE 🧟", "A smelly zombie...", "cheese")
dining_hall.set_character(dave) #Dave is in the dining hall
dave.set_conversation("My name is Dave, I'd like to eat your brains! 🧠")
dave.set_weakness("cheese")

#Creates Catrina 
catrina = Friend("💀 CATRINA 💀", "A spooky skeleton")

ballroom.set_character(catrina) #Catrina is in the ballroom

catrina.set_conversation("Hi, I'm Catrina, do not be afraid. 🙂")
catrina.set_gift("SHIELD 🛡") 

#Creates Franky
franky = Enemy("🧛‍ FRANKY 🧛‍", "A vampire, he hasn't seen the sun in a while...", "shield")

study.set_character(franky)

franky.set_conversation("Hi! Let me drink you blood! 🩸")
franky.set_weakness("shield")


############################ functions to make code easier to read ##########################################

# Dave scenario

def zombie_scenario():
 print("\n--> WATCH OUT! He bites! What will fight with?")
 fight_with = input("\n> ").lower().strip()
 win_or_lose = dave.fight(fight_with)

 if win_or_lose == False:
  print("\n")
  print("☞ Game over.")
  exit()
 elif win_or_lose == True:
  print("You're glad to have gotten rid of that CHEESE 🧀...")
  print("\n")

# Potions scenario

def potions_scenario():
 user_choice = (input("\n> "))
        
 if user_choice == "red":
    print("☞ You died. GAME OVER")
    exit()
        
 else:
  print("You have chosen the 🔵 BLUE potion.")
  print("☞ It tastes bitter...Your appearance has changed. Enemies will now be nice to you for a while. 🙂")
  print(nothing)

# Franky scenario

def vamp_scenario():
  print("\n--> WATCH OUT! He bites! You need to protect yourself! What will you use?")

  fight_with = input("\n> ").lower().strip()
  win_or_lose = franky.fight(fight_with)

  if win_or_lose == False:
    print("\n")
    print("☞ Game over.")
    exit()
  elif win_or_lose == True:
    print("Frankie is knocked out.\n")
    franky.drop_item("KEY 🔑")
    print("\n")
    print("--------------------------------------------")
    print("| You took the KEY 🔑 and got away safely   |")
    print("--------------------------------------------")
    print("\n THE END")
    exit()


############################################################ GAME STARTS ###############################################################

current_room = kitchen
inhabitant = current_room.get_character() #places the character in the room


print("\n+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+**+*+**+*+*+*+*+* ✣ __ ✣ 👻 WELCOME FOOLISH MORTAL TO THE HAUNTED MANSION 👻 ✣ __ ✣ ++**+*+*+*+*+*+*+*+*+*+*+*+*+**+*+*+*+*+*+**+*+*+*+*+*+*+*")



while True:
    print("\n")
    
    inhabitant = current_room.get_character()

    #### Cheese


    if inhabitant is None: 
       current_room.get_details()
       kitchen.set_item(cheese)
       cheese.describe()
       command = input("\n> ").lower().strip()
       if command == "eat it":
         print("You died. Game over. 💀")
         exit()
       elif command == "take it":
        print('☞ You put the CHEESE 🧀 in your satchel.')
        kitchen.remove_item()
        print(nothing)
        current_room.direction_help()
        print(which_direction)          
        command = input("\n> ").lower().strip()
        current_room = current_room.move(command)
       else:
         print("☞ Please choose between the two options.")


      #### Dave


    if inhabitant is dave: 
        current_room.get_details()
        print("\n")
        inhabitant.describe()
        inhabitant.talk()
        zombie_scenario()
        current_room.remove_character()


      #### Potions

        
        dining_hall.set_item(potions)  ## Find the potions in the Dining Hall
        potions.describe(color_one, color_two)
        potions_scenario()
        current_room.direction_help()
        
    
        print(which_direction)  ## Choose which direction to go
        command = input("\n> ").lower().strip()
        current_room = current_room.move(command)
        current_room.direction_help()
        inhabitant = current_room.get_character()


      #### Catrina
         
           
        if inhabitant is catrina:
         current_room.get_details()
         print("\n")
         inhabitant.describe()
         inhabitant.talk()
         print("\n")
         print("☞ What would like to do? CHANGE ROOM or TALK?")
         command = input("> ").lower().strip()

        if command == "change room":
         current_room.direction_help()
         print(which_direction)
         command = input("\n> ").lower().strip()
         current_room = current_room.move(command)
         current_room.get_details()
       
        elif command == "talk":
         inhabitant.give_item()
         inhabitant = None
         print("She left...")
         print("\n")
         print("☞ Your appearence changed back to normal.")
         print(nothing)
         current_room.direction_help()

        else:
         print("☞ Please choose between the two options.")
         exit()
     
        if inhabitant is None:
         print(which_direction)          
         command = input("\n> ").lower().strip()
         current_room = current_room.move(command)


        #### Franky
         
    if inhabitant is franky:
         current_room.get_details()
         print("\n")
         inhabitant.describe()
         inhabitant.talk()
         vamp_scenario()
         










