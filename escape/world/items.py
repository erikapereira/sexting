class InventoryItem(object):
    actions = ["get", "drop"]

    def __str__(self):
        return self.name

    def __init__(self, name):
        self.name = name

    def get(self, player):
        if self not in player.inventory:
            player.location.remove_item(self)
            player.inventory.add_inventory_item(self)
            print(f"Item added to inventory: {self.name}")
        else:
            print("You already have this")

    def drop(self, player):
        if self in player.inventory:
            player.inventory.remove_inventory_item(self)
            player.location.add_item(self)
            print(f"You dropped the {self.name}")
        else:
            print("You cant do this")

    def get_actions(self):
        return self.actions

    def bad_action(self, action):
        return "You can't do this."


class RoomItem(object):
    pass

    # specific actions from somewhere else
    # cannot be added to inventory
    #


class Container(object):
    actions = ["open"]
    is_closed = True

    def __init__(self, name):
        self.name = name
        self.contains = []

    def __str__(self):
        return self.name

    def __contains__(self, item):
        return item in self.contains

    def get_actions(self):
        return self.actions

    def add_container_item(self, container_item):
        self.contains.append(container_item)

    def remove_container_item(self, container_item):
        self.contains.remove(container_item)

    def open(self, player):
        if self.is_closed:
            self.is_closed = False
            for item in self.contains:
                player.location.add_item(item)
                self.remove_container_item(item)
            print("You opened the box there is a key inside")
        else:
            print("The box is already open")

    def bad_action(self, action):
        return "You can't do this."


