class Node(object):

    def __init__(self, item):
        self.item = item
        self.next = None


class SingleLinkList(object):

    def __init__(self, node=None):
        self.__head = node

    def is_empty(self):
        return self.__head is None

    def length(self):
        cur = self.__head
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        cur = self.__head
        while cur is not None:
            print(cur.item, end=" ")
            cur = cur.next
        print("")

    def add(self, item):
        node = Node(item)
        node.next = self.__head
        self.__head = node

    def append(self, item):
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next is not None:
                cur = cur.next
            cur.next = node

    def insert(self, pos, item):
        if pos <= 0:
            self.add(item)
        elif pos >= self.length():
            self.append(item)
        else:
            cur = self.__head
            count = 0
            while count < (pos - 1):
                count += 1
                cur = cur.next
            node = Node(item)
            node.next = cur.next
            cur.next = node

    def remove(self, item):
        cur = self.__head
        pre = None
        while cur is not None:
            if cur.item == item:

                if cur == self.__head:
                    self.__head = cur.next
                else:
                    pre.next = cur.next
                return
            pre = cur
            cur = cur.next

    def search(self, item):
        cur = self.__head
        while cur is not None:
            if cur.item == item:
                return True
            cur = cur.next
        return False




