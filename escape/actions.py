def do_action(player, action, words):

    if action == "enter" and len(words) == 1:
        item = player.location.find_object(words[0])
        player.enter_door(item)

    elif action == "help":
        player.help()

    elif action == "look":
        player.look()

    elif action == "inventory":
        player.get_inventory()

    elif action == "help":
        player.help()

    elif action == "examine" and len(words) == 1:
        player.examine_object(words)

    elif action and len(words) == 1:
        item = player.location.find_object(words[0]) or player.inventory.find_object(
            words[0]
 )
        if not item:
            print("Item does not exist")
            return
        action_valid = action in item.get_actions()

        method_exists = hasattr(item, action)

        if action_valid and method_exists:
            getattr(item, action)(player)
        else:
            print(item.bad_action(action))

    else:
        print("Boobs")










# look around the room
# examine an object
# doing an action
