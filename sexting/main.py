from sexting import state
from sexting import actions


def welcome_message():
    print ("Welcome to Erika's sexting adventure")
    print('You are in the ' + state.current_room.title())

    if state.is_alive:
        print('Congrats! You are alive')

    list_actions()


def main():
    welcome_message()

    print('Enter action')

    while state.is_alive and not state.escaped:
        command=input('> ')
        commands = command.split(' ')

        actions.do_action(commands[0], commands[1:])


def list_actions():
    print('Your available actions are ')
    print(actions.get_actions())
