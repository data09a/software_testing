class HouseItem:

    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return "[%s] takes a space of %.2f" % (self.name, self.area)


class House:

    def __init__(self, house_type, area):
        self.house_type = house_type
        self.area = area

        # free area
        self.free_area = area

        # house item name list
        self.item_list = []

    def __str__(self):
        return ("Style: %s\nTotal space: %.2f[Free space: %.2f]\nHouse item: %s"
                % (self.house_type, self.area,
                   self.free_area, self.item_list))

    def add_item(self, item):
        print("Add %s" % item)


# 1. create furniture
bed = HouseItem("mattress", 4)
closet = HouseItem("closet", 2)
table = HouseItem("dinning table", 1.5)

print(bed)
print(closet)
print(table)

# 2. create house object
my_home = House("2 bedroom", 60)

my_home.add_item(bed)
my_home.add_item(closet)
my_home.add_item(table)

print(my_home)