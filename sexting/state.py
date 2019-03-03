
class Player(object):
    def __init__(self,location):
        self.is_alive = True
        self.is_trapped = True
        self.location = location
        self.inventory = Inventory()

    def dead(self):
        self.is_alive = False
        print('You died of dysentery')

    def set_location(self,new_location):
        self.location = new_location

    def enter_door(self,door):
        can_be_entered, reason = door.can_be_entered()

        if can_be_entered:
            if isinstance(door,EndDoor):
                self.is_trapped = False
                print("You escaped the room")

            else:
                self.set_location(door.destination)
                self.inventory.clear_inventory()
                print(f"You are in {self.location.name}.")
        else:
            print(reason)
            # this should say the door is locked?? delete redundant code from door class? Or call a function?

    def look(self):
        print(f" Location: {player.location.name} ")
        for item in player.location.contains:
            print(f"Room contains: ", item)

    def examine_object(self,words):
        item = player.location.find_object(words[0])
        if not item:
            print("Item does not exist")
            return
        print(f"You can do these actions: ", item.get_actions())

    def get_inventory(self):
        print("Inventory:")
        if len(player.inventory.inventory_items) > 0:
            for inventory_item in player.inventory.get_inventory():
                print(inventory_item.name)
        else:
            print("Emtpy")

            # drop item in inv





    # append/remove loication
    # enter door method.
    # which door is it and where does it go?
    # change players location


    # player actions



class Location(object):
    def __init__(self,name):
        self.name = name
        self.contains = []

    def __contains__(self, item):
        return item in self.contains

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

    def __init__(self,destination):
        self.destination = destination

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

    def can_be_entered(self):
        return True, None

    def get_actions(self):
        return self.actions

    def bad_action(self,action):
        return "You can't do this."


class LockedDoor(Door):
    is_locked = True

    def __init__(self,destination,key):
        super().__init__(destination)
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

    def can_be_entered(self):
        if self.is_locked:
            return False, "The door is locked"
        else:
            return True, None

class EndDoor(LockedDoor):
    pass


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

    def clear_inventory(self):
        self.inventory_items = []

    def find_object(self,inventory_item):
        for item in self.inventory_items:
            if inventory_item.lower() == str(item).lower():
                return item
        return None



class InventoryItem(object):
    actions = ['get', 'drop']

    def __str__(self):
        return self.name

    def __init__(self,name):
        self.name = name

    def get(self):
        if self not in player.inventory:
            player.location.remove_item(self)
            player.inventory.add_inventory_item(self)
            print(f"Item added to inventory: {self.name}")
        else:
            print("You already have this")

    def drop(self):
        if self in player.inventory:
            player.inventory.remove_inventory_item(self)
            player.location.add_item(self)
            print(f"You dropped the {self.name}")
        else:
            print("You cant do this")

    def get_actions(self):
        return self.actions

    def bad_action(self,action):
        return "You can't do this."


room_one = Location(name='Room 1')
room_two = Location(name='Room 2')



player = Player(location=room_one)



room_one_key = InventoryItem('key')
room_two_key = InventoryItem('key')


room_one_door = LockedDoor(room_two,room_one_key)
room_one.add_item(room_one_door)
room_one.add_item(room_one_key)

room_two_door = EndDoor(None,room_two_key)
room_two.add_item(room_two_door)
room_two.add_item(room_two_key)

