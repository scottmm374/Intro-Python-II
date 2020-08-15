class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f'{self.name}: {self.description}'


# hammer = Item("hammer", "Break things")
# saw = Item("Hand saw", "For sawing things")
# water = Item("Bottled Water", "Keep yourself hydrated")
# snacks = Item("snickers", "Keep yourself fed")
# medical = Item("First Aid kit", "Stay healthy")
