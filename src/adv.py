from room import Room
from player import Player


# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance,",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer,", """Dim light filters in from the south. Dusty
                    passages run north and east."""),

    'overlook': Room("Grand Overlook,", """A steep cliff appears before you, falling
                    into the darkness. Ahead to the north, a light flickers in
                    the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage,", """The narrow passage bends here from west
                    to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber,", """You've found the long-lost treasure
                    chamber! Sadly, it has already been completely emptied by
                    earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']  # ! can only go N
room['foyer'].s_to = room['outside']  # ! can go n, s, e
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']  # ! overlook can go s
room['narrow'].w_to = room['foyer']  # ! narrow can go w,n
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']  # !can only go s


#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player_name = input('Please enter your name: ')
player = Player(player_name, room['outside'])
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
while True:

    print(f'{player} You are in {player.current_room.name} {player.current_room.description} !')
    player_input = input(
        f'Please choose which direction you would like to go: [s] for south, [n] for north, [e] for east, [w] for west, or choose [q] to quit game: ')

    if player_input == 'q':
        print("Thank you for playing")
        break
    if player_input in {'n', 's', 'e', 'w'}:
        if hasattr(player.current_room, f'{player_input}_to'):
            player.current_room = getattr(
                player.current_room, f'{player_input}_to')
            print(f' You are now in {player.current_room}')
    else:
        print("You cannot go in that direction, please choose another direction")

        #
        # If the user enters a cardinal direction, attempt to move to the room there.
        # Print an error message if the movement isn't allowed.
        #
        # If the user enters "q", quit the game.
