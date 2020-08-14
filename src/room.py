# Implement a class to hold room information. This should have name and
# description attributes.
from item import Item


class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.item = []

    def __str__(self):
        return f"{self.name}. {self.description}. "

    def on_take(self, item):
        self.item.remove(item)

    def on_drop(self, item):
        self.item.append(item)
