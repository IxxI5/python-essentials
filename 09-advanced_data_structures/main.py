# Advanced Data Structures Example

# List Comprehensions: It is a way to create new lists based on existing lists or other sequences.
# --------------------

# Create a list of squares of numbers from 1 to 10
squares = [x**2 for x in range(1, 11)]
print("Squares:", squares)

# Output: Squares: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Create a list of names in uppercase
names = ["John", "Alice", "Bob"]
uppercase_names = [name.upper() for name in names]
print("Uppercase Names:", uppercase_names)

# Output: Uppercase Names: ['JOHN', 'ALICE', 'BOB']

# Dictionary Comprehensions: It is a way to create new dictionaries based on existing dictionaries or other mappings.
# -------------------------

# Create a dictionary of squares of numbers from 1 to 10
squares_dict = {x: x**2 for x in range(1, 11)}
print("Squares Dictionary:", squares_dict)

# Output: Squares Dictionary: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}

# Create a dictionary of names with their lengths
names_dict = {name: len(name) for name in names}
print("Names Dictionary:", names_dict)

# Output: Names Dictionary: {'John': 4, 'Alice': 5, 'Bob': 3}

# Generators: It is a way to create iterators that can be used to generate values on the fly.
# ----------

# Create a generator that yields numbers from 1 to 10
def numbers_generator():
    for x in range(1, 11):
        yield x

# Print the numbers generated
print("Numbers Generator:")
for num in numbers_generator():
    print(num)

# Output:
# Numbers Generator:
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10

# Iterators: It is a way to iterate over a sequence of values.
# ----------

# Create a list of numbers from 1 to 10
numbers = [x for x in range(1, 11)]

# Create an iterator from the list
# iter is a built-in function that returns an iterator from a sequence and uses next to iterate over the sequence
numbers_iterator = iter(numbers)

# Print the numbers iterated
print("Numbers Iterator:")
while True:
    try:
        print(next(numbers_iterator)) # next is a built-in function that returns the next value from the iterator
    except StopIteration:
        break

# Output:
# Numbers Iterator:
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10

# Collections Module
# ------------------

# Deque: It is a double-ended queue that can be used to add and remove elements from both ends.
# e.g. 
# -----

# Create a deque of numbers from 1 to 5
from collections import deque
numbers_deque = deque([x for x in range(1, 6)])
print("Numbers Deque:", numbers_deque)

# Output: Numbers Deque: deque([1, 2, 3, 4, 5])

# Add numbers to the left and right of the deque
numbers_deque.appendleft(0)
numbers_deque.append(6)
print("Numbers Deque after append:", numbers_deque)

# Output: Numbers Deque after append: deque([0, 1, 2, 3, 4, 5, 6])

# Counter: It is a dictionary that counts the occurrences of elements in a sequence.
# ------

# Create a counter of names
from collections import Counter
names_counter = Counter(names)
print("Names Counter:", names_counter)

# Output: Names Counter: Counter({'John': 1, 'Alice': 1, 'Bob': 1})

# Update the counter with new names
names_counter.update(["John", "Alice", "Charlie"])
print("Names Counter after update:", names_counter)

# Output: Names Counter after update: Counter({'John': 2, 'Alice': 2, 'Bob': 1, 'Charlie': 1})

# DefaultDict: It is a dictionary that returns a default value when a key is not found.
# ------------

# Create a default dictionary of names with their lengths
from collections import defaultdict
names_defaultdict = defaultdict(int)
for name in names:
    names_defaultdict[name] = len(name)
print("Names DefaultDict:", names_defaultdict)

# Output: Names DefaultDict: defaultdict(<class 'int'>, {'John': 4, 'Alice': 5, 'Bob': 3})

# Get the length of a non-existent name
print("Length of non-existent name:", names_defaultdict["NonExistentName"])

# Output: Length of non-existent name: 0