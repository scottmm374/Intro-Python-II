#!/usr/bin/env python3

from room import Room
from item import Item
from player import Player

# Declaring Items

hammer = Item("hammer", "Break things")
saw = Item("Hand saw", "For sawing things")
water = Item("Bottled Water", "Keep yourself hydrated")
snacks = Item("snickers", "Keep yourself fed")
medical = Item("First Aid kit", "Stay healthy")
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance,",
                     "North of you, the cave mount beckons", [hammer, saw]),

    'foyer':    Room("Foyer,", """Dim light filters in from the south. Dusty
                    passages run north and east.""", [saw]),

    'overlook': Room("Grand Overlook,", """A steep cliff appears before you, falling
                    into the darkness. Ahead to the north, a light flickers in
                    the distance, but there is no way across the chasm.""", [water]),

    'narrow':   Room("Narrow Passage,", """The narrow passage bends here from west
                    to north. The smell of gold permeates the air.""", [snacks]),

    'treasure': Room("Treasure Chamber,", """You've found the long-lost treasure
                    chamber! Sadly, it has already been completely emptied by
                    earlier adventurers. The only exit is to the south.""", [medical]),
}


# room['foyer'].items = [items['hammer']]
# room['overlook'].items = [items['water']]
# room['narrow'].items = [items['medical']]
# room['treasure'].items = [items['saw']]
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
player_name = input('Please enter your name: ')
player = Player(player_name, room['outside'])
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
while True:
    try:
        print(player)

        player_input = input(
            f'Please choose a direction: n, s, e, w or q to quit: ').lower()
        if player_input == 'q':
            print("Thank you for playing")
            break

        print(f'The following items are in the room: ')
        current_items = player.current_room.check_room()

        command = input(f'Pick up item?  yes or no: ').lower()

        if player_input == "yes":
            if player.current_room.items in player.current_room.items:
                player.on_take(player.current_room.items)

                # print(f'You picked up {player.current_room.item}')
            else:
                print(f'Choose an action')

        if player_input == 's' or player_input == 'n' or player_input == 'e' or player_input == 'w':
            if getattr(player.current_room, f'{player_input}_to') is not None:
                player.current_room = getattr(
                    player.current_room, f'{player_input}_to')
            else:
                print("That direction is blocked, please choose another direction")

    except ValueError:
        print('Error')
