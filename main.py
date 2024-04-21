import script_functions
from script_functions import choose_menu_option

def main():
    check_switch = 0
    print("Welcome to the Habit Reward Pairing Program.")
    print("Please choose from one of the options below by typing the associated number and pressing Enter.")

    while check_switch == 0:
        menu_option = script_functions.choose_menu_option()
        try:
            menu_option = int(menu_option)
            check_switch = 1

        except:
            print("Please type the associated number with the option of your choosing idiot")

        if check_switch == 1 and (menu_option < 1 or menu_option > 3):
            print("Please type the associated number with the option of your choosing")
            check_switch = 0

    print("Horrah!")


main()
        
