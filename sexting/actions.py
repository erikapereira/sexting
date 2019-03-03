from sexting import state


# glabal ations: look, walk, exit, examine, inventory etc

def do_action(action, words):
    if action == 'look':
        print(f" Location: {state.player.location.name} ")
        #room contains
        for item in state.player.location.contains:
            print(f"Room contains: ",item)

    elif action == "inventory":
        print("Inventory:")
        if len(state.player.inventory.inventory_items) > 0:
            for inventory_item in state.player.inventory.get_inventory():
                print(inventory_item.name)
        else:
            print("Emtpy")

# drop item in inv

    elif action == 'examine' and len(words) == 1:
        item = state.player.location.find_object(words[0])
        if not item:
            print("Item does not exist")
            return
        print(f"You can do these actions: ",item.get_actions())

        # add examine to object class?//global actions?


    elif action and len(words)== 1:
        item = state.player.location.find_object(words[0])
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


