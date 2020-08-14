# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.backpack = []

    def __str__(self):
        return f'{self.name}, you are now at {self.current_room}. You have {self.backpack}'

    def get_item(self, item):
        self.backpack.append(item)

    def drop_item(self, item):
        self.backpack.remove(item)
