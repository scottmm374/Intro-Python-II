# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, current_room, backpack=[]):
        self.name = name
        self.current_room = current_room
        self.backpack = backpack

    def __str__(self):
        return f'{self.name}, you are now at {self.current_room}.'

    def on_take(self, item):
        print(f'You have picked up the {item}')
        self.backpack.append(item)

    def on_drop(self, item):
        print(f'You have dropped the {item}')
        self.backpack.remove(item)

    def check_backpack(self):
        for key, value in enumerate(self.backpack, 1):
            print(key, value)
        # if len(self.backpack) > 0:
        #     output = (f' You have the following items in your backpack: ')
        #     for item in self.backpack:
        #         output += f'\n {item}'
        #         print(output)
        # else:
        #     print("Your backpack is empty")
