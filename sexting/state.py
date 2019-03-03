
class Player(object):
    def __init__(self,location):
        self.is_alive = True
        self.is_trapped = True
        self.location = location
        self.inventory = Inventory()

    def dead(self):
        self.is_alive = False
        print('You died of dysentery')



class Location(object):
    def __init__(self,name):
        self.name = name
        self.contains = []

    def add_item(self,item):
        self.contains.append(item)

    def remove_item(self,item):
        self.contains.remove(item)

    # remove item so when you pick up a key its not there anymore!

    def find_object(self,item_name):
        for item in self.contains:
            if item_name.lower() == str(item).lower():
                return item
        return None

    # need to add/remove item from location/inventory once picked up


class Door(object):
    actions = ['open',"close",'enter']
    is_closed = True

    def __str__(self):
        return 'door'

    def open(self):
        if self.is_closed:
            print('The door opened')
            self.is_closed = False

        else:
            print('The door is already open')

    def close(self):
        if self.is_closed:
            print('The door is already closed')

        else:
            print('You closed the door')
            self.is_closed = True

    def enter(self):
        if not self.is_closed:
            print('Well done you escaped the room!')
            player.is_trapped = False

        else:
            print('The door is not open')

    def get_actions(self):
        return self.actions

    def bad_action(self,action):
        return "You can't do this."


class LockedDoor(Door):
    is_locked = True

    def __init__(self,key):
        self.key = key

    def open(self):
        if self.is_locked:
            print('The door is locked')

        else:
            super().open()

    def unlock(self):

        if self.is_locked and self.key in player.inventory:
            self.is_locked = False
            print("You unlocked the door")

        elif not self.is_locked and self.key in player.inventory:
            print("Door is already unlocked")

        else:
            print("You don't have a key")

    def lock(self):
        if self.is_locked and self.key in player.inventory:
            print("Door is already locked")

        elif not self.is_locked and self.key in player.inventory:
            self.is_locked = True
            self.is_closed = True
            print("You locked the door")

        else:
            print("You don't have a key")

    def get_actions(self):
        return super().get_actions() + ['unlock','lock']




class Inventory(object):
    def __init__(self):
        self.inventory_items = []

    def __contains__(self, item):
        return item in self.inventory_items

    def get_inventory(self):
        return self.inventory_items

    def add_inventory_item (self, inventory_item):
        self.inventory_items.append(inventory_item)

    def remove_inventory_item (self, inventory_item):
        self.inventory_items.remove(inventory_item)




class InventoryItem(object):
    actions = ['get', 'drop']

    def __str__(self):
        return self.name

    def __init__(self,name):
        self.name = name

    def get(self):
            player.location.remove_item(self)
            player.inventory.add_inventory_item(self)
            print(f"Item added to inventory: {self.name}")

    def drop(self):
            player.location.add_item(self)
            player.inventory.remove_inventory_item(self)
            print(f"You dropped {self.name}")

        # why does GET work but not DROP?!
        # because removing something from Inventory not currently supported in actions.


    def get_actions(self):
        return self.actions

    def bad_action(self,action):
        return "You can't do this."


lounge = Location(name='lounge')

player = Player(location=lounge)



lounge_key = InventoryItem('key')


lounge_door = LockedDoor(lounge_key)
lounge.add_item(lounge_door)
lounge.add_item(lounge_key)