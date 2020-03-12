# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self,name,current_room,gear = None):
        self.name = name
        self.current_room = current_room
        self.gear = [gear]
    def travel(self, direction):
        next_room = getattr(self.current_room, f"{direction}_to")
        if next_room is not None:
            self.current_room = next_room
            print(self.current_room)
        else:
            print("You cannot move in that direction")
    def take_item(self,item):
        self.gear = self.gear + self.current_room.item
        print(f"You aquire the {item}")
        self.current_room.item = []
    def drop_item(self,item):
        self.current_room.item = self.gear + self.current_room.item
        print(f"You drop {self.gear}")
        self.gear = []