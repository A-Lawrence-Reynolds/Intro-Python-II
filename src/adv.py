from room import Room
from player import Player
from item import Item
import random
# Declare all the rooms

potential= [Item("gun","BOOOM!!!!"),
 Item('armor','protect yourself from harm'), 
 Item("Rusty sword","a sword that is a little rusty but will keep you alive in a pinch"),
 Item("Sword","just a normal sword"),
 Item("Gold sword!","this is the best sword"),
 Item("Boots","to keep your feet happy"),
 Item("Axe","to chop wood or defeat a attacker "),
 Item("Helmet","keeping you head in a safe"),
  ]
room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons."),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),

    'cliffside': Room("Edge of large cliff", """You have walked away from the cave and find yourself 
    on the edge of a menacing cliff. The only way to get away from the cliff if to find your way back
     to the cave."""),

     'dinning room': Room("A grand dinning hall fit for a king!", """you have entered 
    a wonderful place to eat but any food was eaten long ago, better luck in a different room...."""),
}

# room[0].item.append(random.choice(potential))

for k,v in room.items():
    v.item=(random.sample(potential,2))


# Link rooms together

room['outside'].n_to = room['foyer']
room['outside'].s_to = room['cliffside']
room['cliffside'].n_to = room['outside']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['foyer'].w_to = room['dinning room']
room['dinning room'].e_to = room['foyer']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
Player_one = Player("Vitruvius", room['outside'],)
# print(Player_one.gear)
# print(Player_one.current_room.item)
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.


print(Player_one.current_room)
while True:
    print("N,S,W,E for movement. I for inventory. Q to quit.")
    cmd = input("-> ").lower()
     #case 2 take and drop
    action = cmd.split(' ')
    if len(action)== 1:
        if cmd in ["n", "s", "e", "w"]:
            # Move to that room
            Player_one.travel(cmd)
        
        elif cmd in ["i"]:
            # import pdb; pdb.set_trace()
            print(f"current inventory: {[n.name for n in Player_one.gear]}")
        elif cmd == "q":
            print("Goodbye!")
            exit()
        else:
            print("I did not understand that command.")
    elif len(action)== 2:
        print("first word",action[0]) 
        # take or drop if its = one or other 
        if action[0] == "take":
            Player_one.take_item(action[1])
    elif len(action)== 2:
        print("first word",action[0]) 
        # take or drop if its = one or other 
        if action[0] == "drop":
            Player_one.drop_item(action[1])
             
    # case 1 der i and q
