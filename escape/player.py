class Player(object):
    def __init__(self, location):
        self.is_alive = True
        self.is_trapped = True
        self.location = location
        self.inventory = Inventory()

    def dead(self):
        self.is_alive = False
        print("You died of dysentery")

    def set_location(self, new_location):
        self.location = new_location

    def enter_door(self, door):
        can_be_entered, reason = door.can_be_entered()

        if can_be_entered:
            from escape.world.room import TrapDoor, EndDoor

            if isinstance(door, EndDoor):
                self.is_trapped = False
                print("You escaped the room")

            elif isinstance(door, TrapDoor):
                self.is_alive = False
                print("You fell to your death")

            else:
                self.set_location(door.destination)
                self.inventory.clear_inventory()
                print(f"You are in {self.location.name}.")
        else:
            print(reason)

    def look(self):
        print(f" Location: {self.location.name} ")
        for item in self.location.contains:
            print(f"Room contains: ", item)

    def examine_object(self, words):
        item = self.location.find_object(words[0]) or self.inventory.find_object(
            words[0]
        )
        if not item:
            print("Item does not exist")
            return
        print(f"You can do these actions: ", item.get_actions())

    def get_inventory(self):
        print("Inventory:")
        if len(self.inventory.inventory_items) > 0:
            for inventory_item in self.inventory.get_inventory():
                print(inventory_item.name)
        else:
            print("Emtpy")

            # drop item in inv


class Inventory(object):
    def __init__(self):
        self.inventory_items = []

    def __contains__(self, item):
        return item in self.inventory_items

    def get_inventory(self):
        return self.inventory_items

    def add_inventory_item(self, inventory_item):
        self.inventory_items.append(inventory_item)

    def remove_inventory_item(self, inventory_item):
        self.inventory_items.remove(inventory_item)

    def clear_inventory(self):
        self.inventory_items = []

    def find_object(self, inventory_item):
        for item in self.inventory_items:
            if inventory_item.lower() == str(item).lower():
                return item
        return None
