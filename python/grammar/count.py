class Tool(object):

    count = 0

    def __init__(self, name):
        self.name = name


        Tool.count += 1


#  create objects for tools
tool1 = Tool("hammer")
tool2 = Tool("bucket")
tool3 = Tool("screwdriver")
tool4 = Tool("saw")


print(Tool.count)
