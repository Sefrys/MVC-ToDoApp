import os
import sys
from to_do_list import *


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
        os.system("clear")
        print(menu_choices)
        menu_choice = input("Select an option: ")
        if menu_choice == "1":
            print("Add new item: \n")
            add_item_to_list(to_do_list)
        elif menu_choice == "2":
            display_list(to_do_list)
        elif menu_choice == "3":
            display_item_details(to_do_list)
        elif menu_choice == "4":
            modify_item(to_do_list)
        elif menu_choice == "5":
            delete_item(to_do_list)
        elif menu_choice == "6":
            sys.exit()
        else:
            print("Wrong input!")


if __name__ == "__main__":
    main()
