# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, current_room, backpack):
        self.name = name
        self.current_room = current_room
        self.backpack = backpack

    def __str__(self):
        backpack_contents = " "
        for item in self.backpack:
            backpack_contents += str(item)
        if backpack_contents == " ":
            backpack_contents = "None"
        return f'{self.name}, you are now at {self.current_room}. \n Your backpack contains: {backpack_contents}'

    def get_item(self, item):
        self.backpack.append(item)

    def drop_item(self, item):
        self.backpack.remove(item)
