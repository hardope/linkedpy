from .node import Node

class Set:
    def __init__(self, *args):
        """Initialize set with optional values."""
        self.head = None
        self.__count = 0
        for item in args:
            self.add(item)

    def __len__(self):
        """Return the number of items in the set."""
        return self.__count

    def __contains__(self, item):
        """Return True if item is in the set, False otherwise."""
        current = self.head
        while current:
            if current.value == item:
                return True
            current = current.ref
        return False

    def add(self, value):
        """Add an element to the set, if it is not already present."""
        if value not in self:
            new_node = Node(value)
            new_node.ref = self.head
            self.head = new_node
            self.__count += 1

    def remove(self, value):
        """Remove an element from the set. Raise KeyError if not present."""
        if self.head is None:
            raise KeyError("remove(): " + str(value) + " not in set")
        if self.head.value == value:
            self.head = self.head.ref
            self.__count -= 1
            return

        current = self.head
        while current.ref:
            if current.ref.value == value:
                current.ref = current.ref.ref
                self.__count -= 1
                return
            current = current.ref
        raise KeyError("remove(): " + str(value) + " not in set")

    def clear(self):
        """Remove all items from the set."""
        self.head = None
        self.__count = 0

    def copy(self):
        """Return a shallow copy of the set."""
        return Set(*self)

    def __iter__(self):
        """Iterate over the elements in the set."""
        current = self.head
        while current:
            yield current.value
            current = current.ref

    def __str__(self):
        """String representation of the set."""
        return "{" + ", ".join(repr(item) for item in self) + "}"

    def __repr__(self):
        """Official string representation of the set."""
        return f"Set({list(self)})"

    def union(self, other):
        """Return a new set with elements from the set and all others."""
        new_set = self.copy()
        for item in other:
            new_set.add(item)
        return new_set

    def intersection(self, other):
        """Return a new set with elements common to the set and other."""
        new_set = Set()
        for item in self:
            if item in other:
                new_set.add(item)
        return new_set

    def difference(self, other):
        """Return a new set with elements in the set that are not in the other."""
        new_set = Set()
        for item in self:
            if item not in other:
                new_set.add(item)
        return new_set

    def issubset(self, other):
        """Report whether another set contains this set."""
        for item in self:
            if item not in other:
                return False
        return True

    def issuperset(self, other):
        """Report whether this set contains another set."""
        for item in other:
            if item not in self:
                return False
        return True
