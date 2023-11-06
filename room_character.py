#Create a character

class Character():
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None

#Decribe this character

    def describe(self):
        print(f"/!\ /!\ /!\ ❗️ {self.name} is here ❗️ /!\ /!\ /!\ \n")
        print(self.description)

#Set what this character will say when talked to 

    def set_conversation(self, conversation):
        self.conversation = conversation

#Talk to this character

    def talk(self):
        if self.conversation is not None:
            print(f"[{self.name} says]: {self.conversation}")
        else: 
            print(f"{self.name} doesn't want to talk to you.")

#Fight with this character

    def fight(self, combat_item):
        combat_item = combat_item
        print(self.name + " doesn't want to fight you")
        return True
    
#Subclass
    
class Enemy(Character):
    def __init__(self, char_name, char_description, char_weakness):
        super().__init__(char_name, char_description)
        self.char_weakness = char_weakness
    
    def set_weakness(self, item_weakness):
        self.weakness = item_weakness
    
    def get_weakness(self):
        return self.weakness
    
    def drop_item(self, item):
        print(f"A {item} has dropped from his pocket!")
    
    def fight(self, combat_item): #Overrides the method used in Character
        if combat_item == self.weakness:
            print(f"☞ You fend {self.name} off, using {combat_item}." )
            return True
        else: 
            print("\n")
            print(f"☞ {self.name} crushes you, puny adventurer!")
            return False
            
        
##########

class Friend(Character):
    def __init__(self, char_name, char_description):
         super().__init__(char_name, char_description)
         self.gift_item = "shield"

    def set_gift(self, gift_item):
         self.gift_item = gift_item
    
    def get_gift(self, gift_item):
        return gift_item
        
    def give_item(self):
        print(f"☞ Brave mortal, let me give you this {self.gift_item}." )
         

##########