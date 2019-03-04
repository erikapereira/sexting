from sexting import actions
from sexting.levels import player


def welcome_message():
    print("Welcome to Erika's escape room adventure")


def main():
    welcome_message()

    print("Enter action")

    while player.is_trapped and player.is_alive:
        command = input("> ").strip()
        # added strip
        commands = command.split(" ")

        actions.do_action(player, commands[0], commands[1:])

        # need to change to include commad being more than two words eg 'pick up' instead of 'get'

        # black . in terminal to format code!
        # pip install black - installs on current project
