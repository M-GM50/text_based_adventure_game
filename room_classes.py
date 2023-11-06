# Text based adventure game 

class Room():
    def __init__(self, room_name):
        self.name = room_name
        self.description = None
        self.linked_rooms = {} 
        self.character = None
        self.item = None #I added this

    def get_description(self):
        return self.description
    
    def set_description(self, description):
        self.description = description

    def get_name(self):
        return self.name
    
    def set_name(self, room_name):
        self.room_name = room_name

    def set_character(self, new_character):
        self.character = new_character

    def get_character(self):
        return self.character
    
    def remove_character(self): 
        self.character = None
    
    def remove_item(self): 
        self.item = None

    def set_item(self, new_item): # I ADDED THIS
        self.item = new_item

    def decribe(self):
        print(self.description)

    def link_room(self, room_to_link, direction):
        self.linked_rooms[direction] = room_to_link

    def get_details(self):
        print(f"You have arrived in the {self.name}:")
        print(self.description)

    def direction_help(self): ###I split get_details
        print("-------------------------------------------------------------------------")
        print("According to your map: ")
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            print(f"the {room.get_name()} is {direction}.")
        print("-------------------------------------------------------------------------")

    def move(self, direction):
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print("You can't go that way")
            return self
