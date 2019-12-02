class Stack(object):
    def __init__(self):
        self.__items = []
        # self.__items = SingleLinkList()

    def push(self, item):
        self.__items.append(item)   # O(1)
        # self.__items.insert(0, item)  #O(n)

    def pop(self):
        return self.__items.pop()
        # self.__items.pop(0)

    def peek(self):
        return  self.__items[-1]
        # return  self.__items[len(self.__items)-1]

    def is_empty(self):
        return self.__items == []

    def size(self):
        return len(self.__items)