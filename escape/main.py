from escape import actions
from escape.levels import player


def welcome_message():
    print("You've received an invitation to Baron Von Cheesesticks kinky dungeon party. You've arrived at the house on the address, but where's the party?")


def main():
    welcome_message()
    print("Try typing 'look' to begin")

    while player.is_trapped and player.is_alive:
        command = input("> ").strip()
        # added strip
        commands = command.split(" ")

        actions.do_action(player, commands[0], commands[1:])


        # black . in terminal to format code!
        # pip install black - installs on current project
