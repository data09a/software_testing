class Tool(object):

    count = 0

    @classmethod
    def show_tool_count(cls):

        print("Quantity: %d" % cls.count)

    def __init__(self, name):
        self.name = name

        Tool.count += 1


tool1 = Tool("Knife")
tool2 = Tool("Hammer")

Tool.show_tool_count()