class Node:
    def __init__(self, value):
        self.value = value
        self.ref = None


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

    def pop(self, index=None):
        if self.head == None:
            raise IndexError("Cannot remove Elemenet from an empty list")

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
