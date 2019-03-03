from sexting import state




def do_action(action, words):

    if action == "enter" and len(words)== 1:
        item = state.player.location.find_object(words[0])
        state.player.enter_door(item)

    elif action == 'look':
        state.player.look()

    elif action == "inventory":
        state.player.get_inventory()

    elif action == 'examine' and len(words) == 1:
        state.player.examine_object(words)

    elif action and len(words)== 1:
        item = state.player.location.find_object(words[0]) or state.player.inventory.find_object(words[0])
        if not item:
            print("Item does not exist")
            return
        action_valid = action in item.get_actions()

        method_exists = hasattr(item,action)

        if action_valid and method_exists:
            getattr(item,action)()
        else:
            print(item.bad_action(action))

    else:
        print("Boobs")





# look around the room
# examine an object
# doing an action


