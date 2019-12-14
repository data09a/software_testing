class HouseItem:

    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return "[%s] takes a space of %.2f" % (self.name, self.area)


bed = HouseItem("mattress", 4)
chest = HouseItem("closet", 2)
table = HouseItem("dinning table", 1.5)

print(bed)
print(chest)
print(table)
