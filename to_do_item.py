class ToDoItem():

    def __init__(self, name, description, is_done=False):
        self.name = name
        self.description = description
        self.is_done = is_done

    def item_name():
        setting_name = True
        while setting_name:
            name = input("Name: ")
            if len(name) > 20:
                print("Name exceeed maximum characters (20)")
                continue
            return name

    def item_description():
        setting_description = True
        while setting_description:
            description = input("Description: ")
            if len(description) > 150:
                print("Description exceeds maximum characters (150)")
                continue
            return description

    def add_new_item(self):
        name = self.item_name()
        description = self.item_description()
        new_item = ToDoItem(name, description)
        return new_item

    def modify_item_attirbutes(self, name, description, is_done):
        self.name = name
        self.description = description
        self.is_done = is_done

    def __str__(self):
        return "Name: {}".format(self.name)
