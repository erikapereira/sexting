
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

    def find_object(self,item_name):
        for item in self.contains:
            if item_name.lower() == str(item).lower():
                return item
        return None


class Door(object):
    actions = ['open',"close",'enter']
    is_closed = True

    def __str__(self):
        return 'door'

    def open(self):
        if self.is_closed:
            print('the door opened')
            self.is_closed = False

        else:
            print('the door is already open')

    def close(self):
        if self.is_closed:
            print('the door is already closed')

        else:
            print('you closed the door')
            self.is_closed = True

    def enter(self):
        if not self.is_closed:
            print('Well done you escaped the room!')
            player.is_trapped = False

        else:
            print('the door is not open')

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
            print('the door is locked')

        else:
            super().open()

    def unlock(self):

        if self.key in player.inventory:
            self.is_locked = False
            print("You unlocked the door")

        else:
            print("You don't have a key")


    def get_actions(self):
        return super().get_actions() + ['unlock']




class Inventory(object):
    def __init__(self):
        self.inventory_items = []

    def __contains__(self, item):
        return item in self.inventory_items

    def add_inventory_item (self, inventory_item):
        self.inventory_items.append(inventory_item)




class InventoryItem(object):
    actions = ['get']

    def __str__(self):
        return self.name

    def __init__(self,name):
        self.name = name

    def get(self):
        player.inventory.add_inventory_item(self)

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