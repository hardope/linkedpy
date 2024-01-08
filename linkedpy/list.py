from .node import Node

class List:
    __count = 0

    def __init__(self, initial=[]):
        self.head = None
        if initial != []:
            for value in initial:
                self.append(value)

    def count(self):
        return self.__count

    def clear(self):
        self.head = None
        self.__count = 0

    def __len__(self):
        return self.__count

    def copy(self):
        new_list = List()
        node = self.head
        while node is not None:
            new_list.append(node.value)
            node = node.ref
        return new_list

    def to_list(self):
        out = []
        node = self.head
        while node is not None:
            out.append(node.value)
            node = node.ref
        return out

    def extend(self, values=[]):
        if values == []:
            raise ValueError("Cannot extend empty list")
        for value in values:
            self.append(value)

    def remove(self, value):
        rem = False
        if self.head == None:
            raise ValueError("Cannot remove Element from an empty list")
        if value == self.head.value:
            self.head = self.head.ref
            rem = True
        else:
            node = self.head
            while node.ref is not None:
                if value == node.ref.value:
                    node.ref = node.ref.ref
                    rem = True
                else:
                    node = node.ref
        if rem:
            self.__count -= 1
        else:
            raise ValueError(f"{value} not in list")

    def index(self, value):
        if self.head == None:
            raise ValueError("Cannot find Element in an empty list")
        if value == self.head.value:
            return 0
        else:
            node = self.head
            i = 0
            while node is not None:
                if value == node.value:
                    return i
                else:
                    i += 1
                node = node.ref
            raise ValueError(f"{value} not in list")

    def min(self):
        if self.head == None:
            raise ValueError("Empty list")
        if self.head.ref == None:
            return self.head.value
        else:
            minimum = self.head.value
            node = self.head.ref
            while node.ref is not None:
                if minimum > node.ref.value:
                    minimum = node.ref.value
                node = node.ref

        return minimum

    def max(self):
        if self.head == None:
            raise ValueError("Empty list")
        if self.head.ref == None:
            return self.head.value
        else:
            maximum = self.head.value
            node = self.head.ref
            while node.ref is not None:
                if maximum < node.ref.value:
                    maximum = node.ref.value
                node = node.ref

        return maximum

    def append(self, value):
        new_node = Node(value)

        if self.head == None:
            self.head = new_node
        else:
            node = self.head
            while node.ref is not None:
                node = node.ref

            node.ref = new_node
        self.__count += 1

    def insert(self, index, value):
        if index == 0:
            new_node = Node(value)
            new_node.ref = self.head
            self.head = new_node

        elif index > self.__count - 1:
            raise IndexError("Index out of range")
        else:
            new_node = Node(value)

            if self.head == None:
                self.head = new_node
            else:
                node = self.head
                i = 0
                while node.ref is not None:
                    if i + 1 == index:
                        break
                    else:
                        node = node.ref
                    i += 1
                new_node.ref = node.ref
                node.ref = new_node
        self.__count += 1

    def pop(self, index=None):
        if self.head == None:
            raise IndexError("Cannot remove Element from an empty list")

        if index == None:
            if self.head.ref == None:
                out = self.head.value
                self.head = None
            else:
                node = self.head
                while node.ref.ref is not None:
                    node = node.ref
                out = node.ref.value
                node.ref = None
        elif index == 0:
            node = self.head
            out = node.value
            self.head = node.ref
        else:
            if index > self.__count - 1:
                raise IndexError("Index out of range")
            node = self.head
            i = 0
            while node.ref is not None:
                if i + 1 == index:
                    break
                else:
                    node = node.ref
                i += 1
            out = node.ref.value
            node.ref = node.ref.ref

        self.__count -= 1

        return out

    def __str__(self):
        if self.head == None:
            return "[]"
        else:
            node = self.head
            data = "["
            a = 0
            while node is not None:
                if isinstance(node.value, str):
                    if a == self.__count - 1:
                        data += f'"{node.value}"'
                    else:
                        data += f'"{node.value}", '
                else:
                    if a == self.__count - 1:
                        data += f"{node.value}"
                    else:
                        data += f"{node.value}, "
                node = node.ref
                a += 1
            data += "]"

        return data