from sexting import state


def get_actions():
    return ['look','walk']

def do_action(action, arguments):
    if action == 'look':
        print(f'Looks around {state.player.location.name}. There is a door.')

    elif action == 'walk':
        print('walking')

    elif action == 'open' and arguments and arguments[0] == 'door':
       state.lounge_door.open()

    elif action == 'close' and arguments and arguments[0] == 'door':
        state.lounge_door.close()

    elif action == 'enter' and arguments and arguments[0] == 'door':
        state.lounge_door.enter()

    else:
        state.player.dead()


