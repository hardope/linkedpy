from .node import Node

class List:
    __count = 0

    def __init__(self, *args):

        """Initialize list with optional iterable."""
        self.head = None
        for data in args:
            self.append(data)

    def count(self):

        """Return number of occurrences of value."""
        return self.__count

    def clear(self):

        """Remove all items from list."""
        self.head = None
        self.__count = 0

    def __len__(self):

        """Return number of items in list."""
        return self.__count

    def copy(self):

        """Return a shallow copy of the list."""
        new_list = List()
        node = self.head
        while node is not None:
            new_list.append(node.value)
            node = node.ref
        return new_list

    def to_list(self):

        """Return list as a normal list"""
        out = []
        node = self.head
        while node is not None:
            out.append(node.value)
            node = node.ref
        return out

    def extend(self, new_list):

        """Extend list by appending elements from the iterable."""
        
        self.head = self.__add__(new_list).head

    def remove(self, value):

        """Remove first occurrence of value."""
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

        """Return index of value in list"""
        
        return self.__getitem__(value)

    def min(self):

        """Return min value in list"""
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

        """Return max value in list"""
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

        """Append value to end of list."""
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
        
        """Insert value before index."""
        
        self.__setitem__(index, value)

    def pop(self, index=None):

        """Remove and return item at index (default last)."""
        if self.head == None:
            raise IndexError("Cannot remove Element from an empty list")

        if index < 0:
            index += len(self)

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

        """String representation of list"""
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
    
    def __repr__(self):

        """Representation of list"""

        return f"List({self.to_list()})"
    
    def __iter__(self):

        """Iterate over values in list"""

        current = self.head
        while current:
            yield current.value
            current = current.ref

    def __getitem__(self, index):

        """Get item at index"""
        if not isinstance(index, int):
            raise TypeError("Index must be an integer")
        
        # Handle negative indexing
        if index < 0:
            # Determine positive index equivalent for negative index
            index += len(self)

        current = self.head
        for _ in range(index):
            if current:
                current = current.ref
            else:
                raise IndexError("Index out of range")

        if current:
            return current.value
        else:
            raise IndexError("Index out of range")

    def __setitem__(self, index, value):

        """Set item at index"""
        if not isinstance(index, int):
            raise TypeError("Index must be an integer")
        
        # Handle negative indexing
        if index < 0:
            # Determine positive index equivalent for negative index
            index += len(self)

        current = self.head
        for _ in range(index):
            if current:
                current = current.ref
            else:
                raise IndexError("Index out of range")

        if current:
            current.value = value
        else:
            raise IndexError("Index out of range")
        
    def __delitem__(self, index):

        """Delete item at index"""

        if not isinstance(index, int):
            raise TypeError("Index must be an integer")
        
        # Handle negative indexing
        if index < 0:
            # Determine positive index equivalent for negative index
            index += len(self)

        if index == 0:
            self.head = self.head.ref
        else:
            current = self.head
            for _ in range(index - 1):
                if current:
                    current = current.ref
                else:
                    raise IndexError("Index out of range")

            if current:
                current.ref = current.ref.ref
            else:
                raise IndexError("Index out of range")
            
    def __add__(self, other):

        """Concatenation to allow for + operator"""

        if not isinstance(other, List):
            raise TypeError("Can only concatenate List to List")
        
        new_list = List()
        node = self.head
        while node:
            new_list.append(node.value)
            node = node.ref
        node = other.head
        while node:
            new_list.append(node.value)
            node = node.ref
        return new_list
    
    def __iadd__(self, other):

        """In-place concatenation to allow for += operator with normal lists on the right side"""

        if not isinstance(other, List):
            raise TypeError("Can only concatenate List to List")
        
        node = other.head
        while node:
            self.append(node.value)
            node = node.ref
        return self