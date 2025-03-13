# Lists
# -----
# A list is a collection of items that can be of any data type, including strings, integers, floats, and other lists.
# Lists are ordered, meaning that the order of the items matters, and they are mutable, meaning they can be changed after creation.
fruits = ['apple', 'banana', 'cherry']

# Accessing elements
print(fruits[0])  # Output: apple

# Slicing
print(fruits[1:3])  # Output: ['banana', 'cherry']

# Append an element
fruits.append('date')
print(fruits)  # Output: ['apple', 'banana', 'cherry', 'date']

# Insert an element at a specific position
fruits.insert(2, 'elderberry')
print(fruits)  # Output: ['apple', 'banana', 'elderberry', 'cherry', 'date']

# Remove an element
fruits.remove('banana')
print(fruits)  # Output: ['apple', 'elderberry', 'cherry', 'date']

# Sort the list
fruits.sort()
print(fruits)  # Output: ['apple', 'cherry', 'date', 'elderberry']

# Tuples
# ----
# A tuple is a collection of items that can be of any data type, including strings, integers, floats, and other tuples.
# Tuples are ordered, meaning that the order of the items matters, but they are immutable, meaning they cannot be changed after creation.
numbers = (1, 2, 3)

# Accessing elements
print(numbers[0])  # Output: 1

# Tuples are immutable, so we can't modify them
# numbers[0] = 10  # This will raise a TypeError

# Sets
# ----
# A set is an unordered collection of unique items, meaning that each item can only appear once in the set.
# Sets are mutable, meaning they can be changed after creation, but they do not maintain any particular order.
colors = {'red', 'green', 'blue'}

# Add an element
colors.add('yellow')
print(colors)  # Output: {'red', 'green', 'blue', 'yellow'}

# Remove an element
colors.remove('green')
print(colors)  # Output: {'red', 'blue', 'yellow'}

# Check if an element is in the set
print('red' in colors)  # Output: True

# Workaround of converting the immutable tuple to a mutable list
numbers = (1, 2, 3)

# Convert the tuple to a list
# This is because tuples are immutable, so we can't modify them directly
numbers_list = list(numbers)

# Modify the list
# We can modify the list because it's mutable
numbers_list[1] = 10

# Convert the list back to a tuple
# Now that we've modified the list, we can convert it back to a tuple
numbers = tuple(numbers_list)

# Print the modified tuple
print(numbers)  # Output: (1, 10, 3)

# Dictionaries
# ------------
# A dictionary is an unordered collection of key-value pairs, where each key is unique and maps to a specific value.
# Dictionaries are mutable, meaning they can be changed after creation, and they are often used to store and retrieve data by key.
person = {'name': 'John', 'age': 30, 'city': 'New York'}

# Accessing elements
print(person['name'])  # Output: John

# Update an element
person['age'] = 31
print(person)  # Output: {'name': 'John', 'age': 31, 'city': 'New York'}

# Add a new element
person['country'] = 'USA'
print(person)  # Output: {'name': 'John', 'age': 31, 'city': 'New York', 'country': 'USA'}

# Remove an element
del person['city']
print(person)  # Output: {'name': 'John', 'age': 31, 'country': 'USA'}

# Common Operations and Methods
# -----------------------------

# List comprehension
squares = [x**2 for x in range(10)]
print(squares)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Dictionary comprehension
student_grades = {'John': 90, 'Jane': 85, 'Bob': 78}
passing_students = {name: grade for name, grade in student_grades.items() if grade >= 80}
print(passing_students)  # Output: {'John': 90, 'Jane': 85}

# Set intersection
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print(set1 & set2)  # Output: {3, 4}

# Set union
print(set1 | set2)  # Output: {1, 2, 3, 4, 5, 6}

# List sorting
numbers = [4, 2, 7, 1, 3]
numbers.sort()
print(numbers)  # Output: [1, 2, 3, 4, 7]

# Dictionary sorting
person = {'name': 'John', 'age': 30, 'city': 'New York', 'country': 'USA'}

# Sort the dictionary by keys
sorted_person = dict(sorted(person.items()))
print(sorted_person)  # Output: {'age': 30, 'city': 'New York', 'country': 'USA', 'name': 'John'}

# Sort the dictionary by values
# We can use a lambda function, key=lambda item:, to sort the dictionary by values
# We apply str(item[1]) and not just item[1] because item[1] is an integer and we need to convert it to a string to compare
# Otherwise, we would get an error TypeError: '<' not supported between instances of 'int' and 'str'
sorted_person = dict(sorted(person.items(), key=lambda item: str(item[1])))
print(sorted_person)  # Output: {'age': 30, 'name': 'John', 'city': 'New York', 'country': 'USA'}

# Sort the dictionary by keys in reverse order
sorted_person = dict(sorted(person.items(), reverse=True))
print(sorted_person)  # Output: {'name': 'John', 'country': 'USA', 'city': 'New York', 'age': 30}

# Sort the dictionary by values in reverse order
# We can use a lambda function, key=lambda item:, to sort the dictionary by values
# We apply str(item[1]) and not just item[1] because item[1] is an integer and we need to convert it to a string to compare
# Otherwise, we would get an error TypeError: '<' not supported between instances of 'int' and 'str'
sorted_person = dict(sorted(person.items(), key=lambda item: str(item[1]), reverse=True))
print(sorted_person)  # Output: {'country': 'USA', 'city': 'New York', 'name': 'John', 'age': 30}