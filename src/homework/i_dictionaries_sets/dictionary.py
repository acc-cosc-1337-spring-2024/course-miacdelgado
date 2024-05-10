# This creates an empty dictonary to save our inventory
inventory = {}

# Adds or edits an item in our dictionary
def add_inventory(widget_name, quantity):
    if widget_name in inventory:
        inventory[widget_name] += quantity

        print('Item updated')
        return inventory
    else:
        inventory[widget_name] = quantity

        print('Item added')
        return inventory

# Deletes an item from our dictionary
def del_inventory(widget_name):
    if widget_name in inventory:
        del(inventory[widget_name])

        print('Record deleted')
        return inventory
    
    else:
        print('Item not found')
        return inventory


