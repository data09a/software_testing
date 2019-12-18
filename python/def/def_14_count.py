class Tool(object):

    count = 0

    def __init__(self, name):
        self.name = name

        Tool.count += 1


tool1 = Tool("Knife")
tool2 = Tool("Hammer")
tool3 = Tool("bucket")

tool3.count = 99

print("the amount is %d" % tool3.count)
print("===> %d" % Tool.count)
