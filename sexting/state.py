
class Player(object):
    def __init__(self,location):
        self.is_alive = True
        self.is_trapped = True
        self.location = location

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




lounge = Location(name='lounge')

player = Player(location=lounge)

lounge_door = Door()
lounge.add_item(lounge_door)

