class Item():
 def __init__(self, name):
  self.name = name

 def get_name(self):
     return self.name
  
 def get_description(self):
     return self.description
  
 def set_name(self, item_name):
     self.name = item_name

 def set_description(self, description):
     self.description = description

 def describe_item(self):
   print(self.description)


class Potions(Item):
   def __init__(self, name):
    super().__init__(name)
    self.color_one = None
    self.color_two = None


   def describe(self, color_one, color_two):
      print(f"☞ You can see two {self.name} on the table.")
      print(f"Choose {color_one} or {color_two}.")

class Cheese(Item):
   def __init__(self, name):
    super().__init__(name)

   def describe(self):
      print("\n")
      print(f"You can see a {self.name} lying on the floor.")
      print(f"What will you do? ☞ EAT IT or ☞ TAKE IT?")






