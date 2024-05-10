import dictionary

# Creates menu
print('Homework 6 Menu\n'
      '1-Add or Update an Item\n'
      '2-Delete Item\n'
      '3-Exit\n')

# Prompts the user for one of the menu item selects
menu_select = int(input('Select one of the above options: '))

while menu_select != 1 and menu_select != 2 and menu_select != 3:
    menu_select = int(input('That choice is not valid, please choose a menu option: '))

while menu_select == 1 or menu_select == 2 or menu_select == 3:
    if menu_select == 1:
        print('Here is the current inventory: ', dictionary.inventory,
               '\nYou would like to either add or edit an inventory item.')
        option = input('Would you like to add an item ( y or n )? ')

        if option == 'y' or option == 'Y':
            item = input('What is the item name? ')
            amount = int(input('How much inventory is there? '))

            dictionary.add_inventory(item, amount)

            print('Here is the updated inventory: ', dictionary.inventory)
        
        else:
            print("You'll be editing an existing item then.")
            item = input('What is the item that you will be editing? ')
            amount = int(input('How much inventory is there? '))

            dictionary.add_inventory(item, amount)

            print('Here is the updated inventory: ' , dictionary.inventory)

        menu_cont = input('Would you like to choose another option from the menu ( y or n )? ')

        if menu_cont == 'n' or menu_cont == 'N':
            print('Goodbye')
            menu_select = 'exit'

        else:
            print('What else would you like to do?\n'
                  '1-Add or Update an Item\n'
                  '2-Delete Item\n'
                  '3-Exit\n')
                
            menu_select = int(input('Select one of the above options: '))

            while menu_select != 1 and menu_select != 2 and menu_select != 3:
                menu_select = int(input('That choice is not valid, please choose a menu option: '))

            if menu_select == 3:
                print("Goodbye")
                menu_select = 'exit'

    if menu_select == 2:
        print('Here is the current inventory: ', dictionary.inventory,
              '\nOkay, you would like to delete an item from the inventory.')
        
        item = input('What is the item that you will be deleting? ')

        dictionary.del_inventory(item)

        print('Here is the updated inventory: ' , dictionary.inventory)

        menu_cont = input('Would you like to choose another option from the menu ( y or n )? ')

        if menu_cont == 'n' or menu_cont == 'N':
            print('Goodbye')
            menu_select = 'exit'

        else:
            print('What else would you like to do?\n'
                  '1-Add or Update an Item\n'
                  '2-Delete Item\n'
                  '3-Exit\n')
                
            menu_select = int(input('Select one of the above options: '))

            while menu_select != 1 and menu_select != 2 and menu_select != 3:
                menu_select = int(input('That choice is not valid, please choose a menu option: '))

            if menu_select == 3:
                print("Goodbye")
                menu_select = 'exit'

    elif menu_select == 3:
        menu_exit = input("Are you sure you would like to exit the program: ")
        if menu_exit == 'Y' or menu_exit == 'y':
            print("Goodbye")
            menu_select = 'exit'
        else:
            print('What else would you like to do?\n'
                  '1-Add or Update an Item\n'
                  '2-Delete Item\n'
                  '3-Exit\n')
            
            menu_select = int(input('Select one of the above options: '))

            while menu_select != 1 and menu_select != 2 and menu_select != 3:
                menu_select = int(input('That choice is not valid, please choose a menu option: '))

            if menu_select == 3:
                print("Goodbye")