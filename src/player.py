# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self,name,current_room):
        self.name = name
        self.current_room = current_room
        self.gear = []
    def travel(self, direction):
        next_room = getattr(self.current_room, f"{direction}_to")
        if next_room is not None:
            self.current_room = next_room
            print(self.current_room)
        else:
            print("You cannot move in that direction")
    def take_item(self,item):
        room_items = [item for item in self.current_room.item]
        str_items = [str(item) for item in self.current_room.item]
    # the item being pass into take_item() is a string 
    # this string need to match to a name of an item in room_items
        if item in str_items:
            # import pdb; pdb.set_trace()
            item_index = str_items.index(item)
            item_object = room_items.pop(item_index)
            print(item_object,type(item_object))
            self.gear.append(item_object)
            self.current_room.item.remove(item_object)
        else:
            print('no item here boss')
  
        print(f"You aquired the {item}")
        print('after item pick up. gear list', [n.name for n in self.gear])
    def drop_item(self,item):
        # self.current_room.item = self.gear + self.current_room.item
        # print(f"You drop {self.gear}")
        # self.gear = []
        room_items = [item for item in self.current_room.item]
        str_items = [str(item) for item in self.current_room.item]

        if item in str_items:
            item_index = str_items.index(item)
            item_object = room_items.append(item_index)
            print(item_object,type(item_object))
            self.gear.pop(item_object)
            
        """
        take item check for item in the room.
        if item self.gear.append item object to pick item
        player.current_room.remove(item)
        else return print('err message')
        """
        """
        drop item check for item in gear if true remove player.gear.remove 
        player.current_room.append item 
        else return print('err message)  
        """  # all the items in room items are OBJECTS 
        
    # each object has self.name which i can use to match my current string
    # OR! if i call an object inside room_items it will return it's name string because of __str__ name
    # each item OBJECT in room_items has an index 
    # we can match the given string to an item OBJECT and we can determine the index of this item OBJECT inside room_items
    # when we append , we can  take item OBJECT from room_items and put it in self.gear.append(room_items[INDEX OF MATCHED OBJECT]) 
      