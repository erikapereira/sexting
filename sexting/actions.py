from sexting import state




def do_action(action, words):
    if action == 'look':
        print(f" Location: {state.player.location.name} ")
        for item in state.player.location.contains:
            print(f"Room contains: ",item)

    elif action == 'examine' and len(words) == 1:
        item = state.player.location.find_object(words[0])
        print(f"You can do these actions: ",item.get_actions())

    elif action and len(words)== 1:
        item = state.player.location.find_object(words[0])
        action_valid = action in item.get_actions()


        method_exists = hasattr(item,action)

        if action_valid and method_exists:
            getattr(item,action)()
        else:
            print("arse")

    else:
        print("Boobs")





# look around the room
# examine an object
# doing an action


