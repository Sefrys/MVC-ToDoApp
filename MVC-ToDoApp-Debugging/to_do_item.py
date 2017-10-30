from logme import *


class ToDoItem():

    def __init__(self, name, description, is_done=False):
        self.name = name
        self.description = description
        self.is_done = is_done

    @logme
    def item_name():
        setting_name = True
        while setting_name:
            name = input("Name: ")
            if len(name) > 20:
                print("Name exceeed maximum characters (20)\n")
                continue
            return name

    @logme
    def item_description():
        setting_description = True
        while setting_description:
            description = input("Description: ")
            if len(description) > 150:
                print("Description exceeds maximum characters (150)\n")
                continue
            return description

    @logme
    def add_new_item(self):
        name = self.item_name()
        description = self.item_description()
        new_item = ToDoItem(name, description)
        return new_item

    @logme
    def modify_item_attirbutes(self, name, description, is_done):
        self.name = name
        self.description = description
        self.is_done = is_done

    @logme
    def __str__(self):
        return "Name: {}".format(self.name)
