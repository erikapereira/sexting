from sexting import state
from sexting import actions


def welcome_message():
    print ("Welcome to Erika's sexting adventure")



def main():
    welcome_message()

    print('Enter action')

    while state.player.is_trapped and state.player.is_alive:
        command=input('> ')
        commands = command.split(' ')

        actions.do_action(commands[0], commands[1:])


