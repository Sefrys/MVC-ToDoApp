from to_do_item import *


def add_item_to_list(to_do_list):
    to_do_list.append(ToDoItem.add_new_item(ToDoItem))


def display_list(to_do_list):
    if len(to_do_list) == 0:
        print("No entries to display.")
    else:
        item_index = 0
        for item in to_do_list:
            print(item_index, item)
            item_index += 1


def display_item_details(to_do_list):
    item_index = int(input("Choose item index to view details: "))
    print("Description: " + to_do_list[item_index].description)
    print("Task finished:", to_do_list[item_index].is_done)


def modify_item_attirbutes(to_do_list):
    item_index = int(input("Choose item index to modify: "))
    name = ToDoItem.item_name()
    description = ToDoItem.item_description()
    is_done = mark_progress_status()
    to_do_list[item_index].modify_item_attirbutes(name, description, is_done)


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


def delete_item(to_do_list):
    item_index = int(input("Choose index of item to delete: "))
    to_do_list.pop(item_index)
