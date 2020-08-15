# Implement a class to hold room information. This should have name and
# description attributes.
from item import Item


class Room:
    def __init__(self, name, description, items=[]):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.items = items

    def __str__(self):
        return f"{self.name}. {self.description}. "

    def check_room(self):
        for key, value in enumerate(self.items, 1):
            print(key, value)

        # if len(self.items) > 0:
        # output = []
        # for item in self.items:
        #     output.append(item)
        #     # output += f'\n {item}'

        # else:
        #     print("There are no items in this room")

        # if len(self.items) > 0:
        #     output = "\n You see the following items in the room: "
        #     for item in self.items:
        #         output += f'\n {item.name} : {item.description}.'

    # def __repr__(self):
    #     return f'{self.name}, {self.description}'

    def on_take(self, items):

        self.items.remove(items)

    def on_drop(self, items):
        self.items.append(items)
