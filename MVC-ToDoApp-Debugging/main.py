import os
import sys
import time
from to_do_list import *


def clear():
    """Clear the display"""
    os.system("cls" if os.name == "nt" else "clear")


def main():
    menu_choices = """
    (1) Create an item
    (2) Display item list
    (3) Display item details
    (4) Modify item details
    (5) Delete item from list
    (6) Exit program\n
    """

    to_do_list = []
    in_menu = True
    while in_menu:
        print(menu_choices)
        menu_choice = input("Select an option: ")
        if menu_choice == "1":
            # clear()
            print("Add new item: \n")
            add_item_to_list(to_do_list)
            # clear()
        elif menu_choice == "2":
            # clear()
            display_list(to_do_list)
        elif menu_choice == "3":
            # clear()
            display_item_details(to_do_list)
        elif menu_choice == "4":
            # clear()
            modify_item_attirbutes(to_do_list)
        elif menu_choice == "5":
            # clear()
            delete_item(to_do_list)
        elif menu_choice == "6":
            sys.exit()
        else:
            # clear()
            print("Wrong input!")


if __name__ == "__main__":
    main()
