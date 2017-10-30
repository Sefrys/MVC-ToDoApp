from to_do_item import *
from main import clear
from logme import *


@logme
def add_item_to_list(to_do_list):
    to_do_list.append(ToDoItem.add_new_item(ToDoItem))


@logme
def display_list(to_do_list):
    if len(to_do_list) == 0:
        print("No entries to display.")
    else:
        item_index = 0
        for item in to_do_list:
            print("ID: {} - {}".format(item_index, item))
            item_index += 1


@logme
def display_item_details(to_do_list):
    list_length = len(to_do_list) - 1

    displaying_list_items = True
    while displaying_list_items:
        display_list(to_do_list)
        entry_selection = input("\nChoose item ID to view details or Q to exit to menu: ").upper()
        # clear()
        if entry_selection == "Q":
            break
        if all(x.isdigit() for x in entry_selection) and entry_selection is not "":
            entry_selection = int(entry_selection)
            # clear()
            if entry_selection < len(to_do_list):
                print("Description: {} \nTask finished: {}".format(to_do_list[entry_selection].description,
                                                                   to_do_list[entry_selection].is_done))
        else:
            print("Index doesn't exist. Choose one from between 0 and {}\n".format(list_length))


@logme
def modify_item_attirbutes(to_do_list):
    list_length = len(to_do_list) - 1

    modifying_list_item = True
    while modifying_list_item:
        display_list(to_do_list)
        entry_selection = input("\nChoose item ID to modify or Q to exit to menu: ").upper()
        # clear()
        if entry_selection == "Q":
            break
        if all(x.isdigit() for x in entry_selection) and entry_selection is not "":
            entry_selection = int(entry_selection)
            if entry_selection < len(to_do_list):
                name = ToDoItem.item_name()
                description = ToDoItem.item_description()
                is_done = mark_progress_status()
                to_do_list[entry_selection].modify_item_attirbutes(name, description, is_done)
                # clear()
        else:
            print("Index doesn't exist. Choose one from between 0 and {}\n".format(list_length))


@logme
def delete_item(to_do_list):
    list_length = len(to_do_list) - 1

    deleting_list_item = True
    while deleting_list_item:
        display_list(to_do_list)
        entry_selection = input("\nChoose item ID to delete or Q to exit to menu: ").upper()
        # clear()
        if entry_selection == "Q":
            break
        if all(x.isdigit() for x in entry_selection) and entry_selection is not "":
            entry_selection = int(entry_selection)
            if entry_selection < len(to_do_list):
                to_do_list.pop(entry_selection)
                # clear()
        else:
            print("Index doesn't exist. Choose one from between 0 and {}\n".format(list_length))


def mark_progress_status():
    marking_status = True
    while marking_status:
        status = input("Is task finished? Y/N: ").upper()
        if status == "Y":
            return True
        elif status == "N":
            return False
        else:
            print("Invalid input, choose Y/N")
            continue
