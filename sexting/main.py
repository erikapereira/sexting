from sexting import state
from sexting import actions


def welcome_message():
    print ("Welcome to Erika's escape room adventure")



def main():
    welcome_message()

    print('Enter action')

    while state.player.is_trapped and state.player.is_alive:
        command=input('> ').strip()
        # added strip
        commands = command.split(' ')

        actions.do_action(commands[0], commands[1:])

        # need to change to include commad being more than two words eg 'pick up' instead of 'get'


