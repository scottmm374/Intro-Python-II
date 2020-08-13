from room import Room
from item import Item
from player import Player


# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance,",
                     "North of you, the cave mount beckons", 'hammer'),

    'foyer':    Room("Foyer,", """Dim light filters in from the south. Dusty
                    passages run north and east.""", 'saw'),

    'overlook': Room("Grand Overlook,", """A steep cliff appears before you, falling
                    into the darkness. Ahead to the north, a light flickers in
                    the distance, but there is no way across the chasm.""", 'water'),

    'narrow':   Room("Narrow Passage,", """The narrow passage bends here from west
                    to north. The smell of gold permeates the air.""", 'snackbar'),

    'treasure': Room("Treasure Chamber,", """You've found the long-lost treasure
                    chamber! Sadly, it has already been completely emptied by
                    earlier adventurers. The only exit is to the south.""", 'medical'),
}

items = {
    'hammer': Item("hammer", "Break things"),
    'saw': Item("Hand saw", "For sawing things"),
    'water':  Item("Bottled Water", "Keep yourself hydrated"),
    'snackbar':  Item("snickers", "Keep yourself fed"),
    'medical':  Item("First Aid kit", "Stay healthy"),
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
player = Player(player_name, room['outside'], [items['snackbar']])
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
while True:
    try:
        print(player)

        player_input = input(
            f'Please choose which direction you would like to go: [s] for south, [n] for north, [e] for east, [w] for west. type[t] to take an item, or [d] to drop and item. or choose[q] to quit game: ').lower()

        if player_input == 'q':
            print("Thank you for playing")
            break

        if player_input == "t":
            player_take = input(f'Which item do you want to take?').lower()
            if items[player_take] in player.current_room.item:
                player.current_room.on_take(items[player_take])
                player.get_item(items[player_take])
            else:
                print(f'Item does not exist')

        if player_input == 's' or player_input == 'n' or player_input == 'e' or player_input == 'w':
            if getattr(player.current_room, f'{player_input}_to') is not None:
                player.current_room = getattr(
                    player.current_room, f'{player_input}_to')
            else:
                print("That direction is blocked, please choose another direction")

    except ValueError:
        print('Error')

    # If the user enters a cardinal direction, attempt to move to the room there.
    # Print an error message if the movement isn't allowed.

    # If the user enters "q", quit the game.
