class HouseItem:

    def __init__(self, name, area):

        self.name = name
        self.area = area

    def __str__(self):

        return "[%s] is %.2f" % (self.name, self.area)

class House:

    def __init__(self, house_type, area):

        self.house_type = house_type
        self.area = area


        self.free_area = area

        # furniture name
        self.item_list = []

    def __str__(self):

        return ("House Type：%s\nTotal Square Meter：%.2f[Free Area:%.2f]\nFurniture：%s"
                % (self.house_type, self.area,
                   self.free_area, self.item_list))

    def add_item(self, item):

        print("We need to add %s" % item)
        # furniture size
        if item.area > self.free_area:
            print("The size of %s is too big, we can not add it" % item.name)

            return

        # 2. add the furniture name in the list
        self.item_list.append(item.name)

        # 3. caculate the free space
        self.free_area -= item.area


# 1. create furniture
bed = HouseItem("Mattress", 40)
closet = HouseItem("Closet", 5)
table = HouseItem("Dinning Table", 20)

print(bed)
print(closet)
print(table)

# 2. create the house
my_home = House("2 bedroom", 80)

my_home.add_item(bed)
my_home.add_item(closet)
my_home.add_item(table)

print(my_home)
