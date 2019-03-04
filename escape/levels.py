from escape.player import Player
from escape.world.room import Location, TrapDoor, EndDoor, LockedDoor
from escape.world.items import InventoryItem, Container


# add locations
room_one = Location(name="Room 1")
room_two = Location(name="Room 2")

player = Player(location=room_one)

room_one_key = InventoryItem("key")
room_two_key = InventoryItem("key")
room_two_box = Container("box")

# room one stuff
room_one_door = LockedDoor(room_two, room_one_key)
room_one.add_item(room_one_door)
room_one.add_item(room_one_key)

# room two stuff
room_two_door = EndDoor(None, room_two_key)
room_two_trapdoor = TrapDoor(None)
room_two.add_item(room_two_door)
room_two.add_item(room_two_trapdoor)
room_two_box.add_container_item(room_two_key)

room_two.add_item(room_two_box)
