from sexting import state
from sexting import actions


def welcome_message():
    print ("Welcome to Erika's sexting adventure")

    list_actions()


def main():
    welcome_message()

    print('Enter action')

    while state.player.is_trapped and state.player.is_alive:
        command=input('> ')
        commands = command.split(' ')

        actions.do_action(commands[0], commands[1:])


def list_actions():
    print('Your available actions are ')
    print(actions.get_actions())