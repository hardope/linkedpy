# linkedpy

`linkedpy` is a simple linked list implementation in Python, providing a custom `List` class with various methods for managing linked list operations.

## Features

- **Basic Operations:**
  - `append(value)`: Add a value to the end of the list.
  - `insert(index, value)`: Insert a value before the specified index.
  - `remove(value)`: Remove the first occurrence of a value.
  - `pop(index=None)`: Remove and return an item at a specified index (default is the last item).
  - `clear()`: Remove all items from the list.

- **Access and Indexing:**
  - `__getitem__(index)`: Get the item at a specific index.
  - `__setitem__(index, value)`: Set the item at a specific index.
  - `__delitem__(index)`: Delete the item at a specific index.

- **Information and Iteration:**
  - `count()`: Return the number of items in the list.
  - `__len__()`: Return the number of items in the list.
  - `to_list()`: Return the list as a normal Python list.
  - `__repr__()`: Return a string representation of the list.
  - `__iter__()`: Iterate over values in the list.

- **Concatenation:**
  - `__add__(other)`: Concatenate two lists using the `+` operator.
  - `__iadd__(other)`: In-place concatenation using the `+=` operator.

- **Statistical Operations:**
  - `min()`: Return the minimum value in the list.
  - `max()`: Return the maximum value in the list.

## Usage

```python
from linkedpy import List

# Create a new list
my_list = List(1, 2, 3)

# Append values
my_list.append(4)
my_list.append(5)

# Access elements
print(my_list[2])  # Output: 3

# Remove element
my_list.remove(2)

# Iterate over the list
for item in my_list:
    print(item)

# Concatenate lists
new_list = my_list + List(6, 7, 8)

# In-place concatenation
my_list += List(9, 10)
