# Implement a class to hold room information. This should have name and
# description attributes.
from iten import Item


class Room:
    def __init__(self, name, description, items):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.items = items

    def __str__(self):
        item_string = " "
        for item in self.item:
            item_string += str(item)
        if item_string == ""
        item_string = "None"
        return f"{self.name}. {self.description}. \nItems: {item_string}"

    def on_take(self, item):
        self.item.remove(item)

    def on_drop(self, item):
        self.item.append(item)
