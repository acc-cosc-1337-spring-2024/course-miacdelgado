import sets

# Creates menu
print('Homework 7 Menu\n'
      '1-Students who took prog1 and prog2\n'
      '2-Students who took prog2 only\n'
      '3-Students who took prog1 not prog2\n'
      '4-Students who took prog2 not prog1\n'
      '5-Exit\n')

# Creates the two sets to be compared
prog1 = set(['Student1', 'Student2', 'Student3'])
prog2 = set(['Student3', 'Student4', 'Student5'])

# Prompts the user for one of the menu item selects
menu_select = int(input('Select one of the above options: '))

while menu_select != 1 and menu_select != 2 and menu_select != 3 and menu_select != 4 and menu_select != 5:
    menu_select = int(input('That choice is not valid, please choose a menu option: '))

while menu_select == 1 or menu_select == 2 or menu_select == 3 or menu_select == 4 or menu_select == 5:
    if menu_select == 1:
        print('The students that took both prog1 and prog2 are: ')
        print(sets.get_students_who_took_prog1_and_prog2(prog1, prog2))

        menu_cont = input('Would you like to choose another option from the menu ( y or n )? ')

        if menu_cont == 'n' or menu_cont == 'N':
            print('Goodbye')
            menu_select = 'exit'

        else:
            print('Homework 7 Menu\n'
                  '1-Students who took prog1 and prog2\n'
                  '2-Students who took prog2 only\n'
                  '3-Students who took prog1 not prog2\n'
                  '4-Students who took prog2 not prog1\n'
                  '5-Exit\n')
                
            menu_select = int(input('Select one of the above options: '))

            while menu_select != 1 and menu_select != 2 and menu_select != 3 and menu_select != 4 and menu_select != 5:
                menu_select = int(input('That choice is not valid, please choose a menu option: '))

            if menu_select == 5:
                print("Goodbye")
                menu_select = 'exit'

    if menu_select == 2:
        print('The students that took either prog1 or prog2 are: ')
        print(sets.get_students_who_took_prog1_or_prog2(prog1, prog2))

        menu_cont = input('Would you like to choose another option from the menu ( y or n )? ')

        if menu_cont == 'n' or menu_cont == 'N':
            print('Goodbye')
            menu_select = 'exit'

        else:
            print('Homework 7 Menu\n'
                  '1-Students who took prog1 and prog2\n'
                  '2-Students who took prog2 only\n'
                  '3-Students who took prog1 not prog2\n'
                  '4-Students who took prog2 not prog1\n'
                  '5-Exit\n')
                
            menu_select = int(input('Select one of the above options: '))

            while menu_select != 1 and menu_select != 2 and menu_select != 3 and menu_select != 4 and menu_select != 5:
                menu_select = int(input('That choice is not valid, please choose a menu option: '))

            if menu_select == 5:
                print("Goodbye")
                menu_select = 'exit'

    if menu_select == 3:
        print('The students that only took prog1 are: ')
        print(sets.get_students_who_took_prog1_not_prog_2(prog1, prog2))

        menu_cont = input('Would you like to choose another option from the menu ( y or n )? ')

        if menu_cont == 'n' or menu_cont == 'N':
            print('Goodbye')
            menu_select = 'exit'

        else:
            print('Homework 7 Menu\n'
                  '1-Students who took prog1 and prog2\n'
                  '2-Students who took prog2 only\n'
                  '3-Students who took prog1 not prog2\n'
                  '4-Students who took prog2 not prog1\n'
                  '5-Exit\n')
                
            menu_select = int(input('Select one of the above options: '))

            while menu_select != 1 and menu_select != 2 and menu_select != 3 and menu_select != 4 and menu_select != 5:
                menu_select = int(input('That choice is not valid, please choose a menu option: '))

            if menu_select == 5:
                print("Goodbye")
                menu_select = 'exit'

    if menu_select == 4:
        print('The students that only took prog2 are: ')
        print(sets.get_students_who_took_prog2_not_prog_1(prog1, prog2))

        menu_cont = input('Would you like to choose another option from the menu ( y or n )? ')

        if menu_cont == 'n' or menu_cont == 'N':
            print('Goodbye')
            menu_select = 'exit'

        else:
            print('Homework 7 Menu\n'
                  '1-Students who took prog1 and prog2\n'
                  '2-Students who took prog2 only\n'
                  '3-Students who took prog1 not prog2\n'
                  '4-Students who took prog2 not prog1\n'
                  '5-Exit\n')
                
            menu_select = int(input('Select one of the above options: '))

            while menu_select != 1 and menu_select != 2 and menu_select != 3 and menu_select != 4 and menu_select != 5:
                menu_select = int(input('That choice is not valid, please choose a menu option: '))

            if menu_select == 5:
                print("Goodbye")
                menu_select = 'exit'

    elif menu_select == 5:
        menu_exit = input("Are you sure you would like to exit the program: ")
        if menu_exit == 'Y' or menu_exit == 'y':
            print("Goodbye")
            menu_select = 'exit'
        else:
            print('Homework 7 Menu\n'
                  '1-Students who took prog1 and prog2\n'
                  '2-Students who took prog2 only\n'
                  '3-Students who took prog1 not prog2\n'
                  '4-Students who took prog2 not prog1\n'
                  '5-Exit\n')
            
            menu_select = int(input('Select one of the above options: '))

            while menu_select != 1 and menu_select != 2 and menu_select != 3 and menu_select != 4 and menu_select != 5:
                menu_select = int(input('That choice is not valid, please choose a menu option: '))

            if menu_select == 5:
                print("Goodbye")