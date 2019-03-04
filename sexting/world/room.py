class Location(object):
    def __init__(self, name):
        self.name = name
        self.contains = []

    def __contains__(self, item):
        return item in self.contains

    def add_item(self, item):
        self.contains.append(item)

    def remove_item(self, item):
        self.contains.remove(item)

    def find_object(self, item_name):
        for item in self.contains:
            if item_name.lower() == str(item).lower():
                return item
        return None


class Door(object):
    actions = ["open", "close", "enter"]
    is_closed = True

    def __init__(self, destination):
        self.destination = destination

    def __str__(self):
        return "door"

    def open(self, player):
        if self.is_closed:
            print("The door opened")
            self.is_closed = False

        else:
            print("The door is already open")

    def close(self,player):
        if self.is_closed:
            print("The door is already closed")

        else:
            print("You closed the door")
            self.is_closed = True

    def can_be_entered(self):
        return True, None

    def get_actions(self):
        return self.actions

    def bad_action(self, action):
        return "You can't do this."


class TrapDoor(Door):
    def __str__(self):
        return "trapdoor"

    def enter(self,player):
        player.enter_door()


class LockedDoor(Door):
    is_locked = True

    def __init__(self, destination, key):
        super().__init__(destination)
        self.key = key

    def open(self, player):
        if self.is_locked:
            print("The door is locked")

        else:
            super().open(player)

    def unlock(self, player):

        if self.is_locked and self.key in player.inventory:
            self.is_locked = False
            print("You unlocked the door")

        elif not self.is_locked and self.key in player.inventory:
            print("Door is already unlocked")

        else:
            print("You don't have a key")

    def lock(self, player):
        if self.is_locked and self.key in player.inventory:
            print("Door is already locked")

        elif not self.is_locked and self.key in player.inventory:
            self.is_locked = True
            self.is_closed = True
            print("You locked the door")

        else:
            print("You don't have a key")

    def get_actions(self):
        return super().get_actions() + ["unlock", "lock"]

    def can_be_entered(self):
        if self.is_locked:
            return False, "The door is locked"
        else:
            return True, None


class EndDoor(LockedDoor):
    pass