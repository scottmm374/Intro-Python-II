# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room


class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room

    def __str__(self):
        return f'{self.name}, you are now at {self.current_room}'

    # def move(self, direction):
    #     if getattr(self.room, f'{direction}_to') is not None:
    #         self.room = getattr(self.room, f'{direction}_to')
    #     else:
    #         print("That direction is blocked, please choose another direction")
