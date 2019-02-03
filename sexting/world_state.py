




door_closed = True

def open_door():
    global door_closed

    if door_closed:
        print('You opened the door')
        door_closed = False

    else:
        print('The door is already open')

def close_door():
    global door_closed

    if door_closed:
        print('The door is already closed')

    else:
        print('You closed the door')
        door_closed = True


