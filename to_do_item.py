class ToDoItem():

    def __init__(self, name, description, is_done=False):
        self.name = name
        self.description = description
        self.is_done = is_done

    def __str__(self):
        return "Name: {}".format(self.name)
