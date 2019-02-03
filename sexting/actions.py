from sexting import state, world_state


def get_actions():
    return ['look','walk']

def do_action(action, arguments):
    if action == 'look':
        print('Looks around room. There is a door')

    elif action == 'walk':
        print('walking')

    elif action == 'open' and arguments and arguments[0] == 'door':
        world_state.open_door()

    elif action == 'close' and arguments and arguments[0] == 'door':
        world_state.close_door()

    elif action == 'enter' and arguments and arguments[0] == 'door':
        state.complete_game()

    else:
        state.player_dead(reason='mumbling')


