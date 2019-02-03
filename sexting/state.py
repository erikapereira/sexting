from sexting import world_state

is_alive = True
escaped = False

current_room = 'lounge'


def player_dead(reason):
    global is_alive
    print (f'You died because {reason}')
    is_alive = False


def complete_game():
    global escaped
    if not world_state.door_closed:
        print('well done! you escaped the room')
        escaped = True

    else:
        print('the door is still closed')

