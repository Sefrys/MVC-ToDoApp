from to_do_item import *


def add_item_to_list(to_do_list):
    to_do_list.append(ToDoItem.add_new_item(ToDoItem))


def display_list(to_do_list):
    item_index = 0
    for item in to_do_list:
        print(item_index, item)
        item_index += 1


def display_item_details(to_do_list):
    item_index = int(input("Choose item index to view details: "))
    print("Description: " + to_do_list[item_index].description)
    print("Task finished:", to_do_list[item_index].is_done)
