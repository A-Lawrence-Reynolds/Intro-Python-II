# from room import Room
# from player import Player
# # Declare all the rooms

# room = {
#     'outside':  Room("Outside Cave Entrance",
#                      "North of you, the cave mount beckons"),

#     'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
# passages run north and east."""),

#     'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
# into the darkness. Ahead to the north, a light flickers in
# the distance, but there is no way across the chasm."""),

#     'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
# to north. The smell of gold permeates the air."""),

#     'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
# chamber! Sadly, it has already been completely emptied by
# earlier adventurers. The only exit is to the south."""),
# }


# # Link rooms together

# room['outside'].n_to = room['foyer']
# room['foyer'].s_to = room['outside']
# room['foyer'].n_to = room['overlook']
# room['foyer'].e_to = room['narrow']
# room['overlook'].s_to = room['foyer']
# room['narrow'].w_to = room['foyer']
# room['narrow'].n_to = room['treasure']
# room['treasure'].s_to = room['narrow']

# #
# # Main
# #

# # Make a new player object that is currently in the 'outside' room.
# Player_one = Player('Vitruvius', 'outside')
# # Write a loop that:
# #
# while True:
#     current_room = Player_one.current_room
#     print(room[current_room])
#     user_input = input(
#         "Select a move(Moves to take are N,S,E,W or press Q to Quit)")
# # OUTSIDE path
# if Player_one.current_room == 'outside':
#         if user_input == "N":
#             Player_one.current_room = 'foyer'
#         elif user_input == "q":
#             break
#         elif user_input != "N":
#             print("Foward only")
#     elif Player_one.current_room == 'foyer':
#         if user_input == "S":
#             Player_one.current_room = 'outside'
#         elif user_input == "N":
#             Player_one.current_room = 'overlook'
#         elif user_input == "E":
#             Player_one.current_room = 'narrow'
#         elif user_input == "q":
#             break
#         elif user_input != "N" or "S" or "E":
#             print("Not a path")
#     elif Player_one.current_room == 'overlook':
#         if user_input == "S":
#             Player_one.current_room = 'foyer'
#         elif user_input == "q":
#             break
#         elif user_input != "S":
#             print("Not a path")
#     elif Player_one.current_room == 'narrow':
#         if user_input == "W":
#             Player_one.current_room = 'foyer'
#         elif user_input == "N":
#             Player_one.current_room = 'treasure'
#         elif user_input == "q":
#             break
#         elif user_input != "W" or "N":
#             print("Not a path")
#     elif Player_one.current_room == 'treasure':
#         if user_input == "S":
#             Player_one.current_room = 'narrow'
#         elif user_input == "q":
#             break
#         elif user_input != "S":
#             print("Not a path")


# # * Prints the current room name
# # * Prints the current description (the textwrap module might be useful here).
# # * Waits for user input and decides what to do.
# #
# # If the user enters a cardinal direction, attempt to move to the room there.
# # Print an error message if the movement isn't allowed.
# #
# # If the user enters "q", quit the game.
from room import Room
from player import Player
import random
# Declare all the rooms

potential = ["knife","chestplate","gold","skull"]
pick = random.choice(potential)
pick2 = random.choice(potential)
pick3 = random.choice(potential)
pick4 = random.choice(potential)
room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",f'loot: {pick}'),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""",f'loot: {pick2}'),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",f'{pick3}'),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",f'{pick4}'),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""","Treasure!"),
}



# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
Player_one = Player("Joshua",'outside')
# print(Player_one.current_room)
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


while True:
    curr_room = Player_one.current_room
    print(room[curr_room])
    user_input = input("What do you wish to do?(Move via N,S,W,E, or q)")
    # # OUTSIDE paths
    if Player_one.current_room == 'outside':
        if user_input == "N":
            Player_one.current_room = 'foyer'
        elif user_input == "q":
            break
        elif user_input != "N":
            print("Foward only")
    elif Player_one.current_room == 'foyer':
        if user_input == "S":
            Player_one.current_room = 'outside'
        elif user_input == "N":
            Player_one.current_room = 'overlook'
        elif user_input == "E":
            Player_one.current_room = 'narrow'
        elif user_input == "q":
            break
        elif user_input != "N" or "S" or "E":
            print("Not a path")
    elif Player_one.current_room == 'overlook':
        if user_input == "S":
            Player_one.current_room = 'foyer'
        elif user_input == "q":
            break
        elif user_input != "S":
            print("Not a path")
    elif Player_one.current_room == 'narrow':
        if user_input == "W":
            Player_one.current_room = 'foyer'
        elif user_input == "N":
            Player_one.current_room = 'treasure'
        elif user_input == "q":
            break
        elif user_input != "W" or "N":
            print("Not a path")
    elif Player_one.current_room == 'treasure':
        if user_input == "S":
            Player_one.current_room = 'narrow'
        elif user_input == "q":
            break
        elif user_input != "S":
            print("Not a path")
    
    
    
    
