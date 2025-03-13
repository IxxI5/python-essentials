# Loops in Python
# Loops are used to repeat a block of code multiple times.

# 1. For loop with range and step
print("For loop with range:")
for i in range(1, 10, 2):                   # Loops from 1 to 9 with a step of 2
    print(i)                                # Output: 1 3 5 7 9

# 2. While loop with condition
print("\nWhile loop:")
count = 0
while count < 5:
    print(count)                            # Output: 0 1 2 3 4
    count += 1             

# 3. Loop with break statement
print("\nFor loop with break:")
for i in range(10):                         # Loops from 0 to 9
    if i == 5:
        print("Breaking the loop at", i)    
        break
    print(i)                                # Output: 0 1 2 3 4 Breaking the loop at 5

# 4. Loop with continue statement
print("\nFor loop with continue:")
for i in range(10):
    if i == 5:
        print("Skipping", i)                # Output: Skipping 5
        continue                            # Skips the iteration when i is 5
    print(i)                                # Output: 0 1 2 3 4 Skipping 5 6 7 8 9

# 5. Loop with else (executes if no break occurs)
print("\nFor loop with else:")
for i in range(3):
    print(i)                                # Output: 0 1 2 Loop finished successfully!
else:
    print("Loop finished successfully!")

# 6. Nested loops (Multiplication table)
print("\nNested loops - Multiplication table:")
for i in range(1, 4):                       # Outer loop
    for j in range(1, 4):                   # Inner loop
        print(f"{i} x {j} = {i * j}")      
    print("------")
    # Output:
    # Nested loops - Multiplication table:
    # 1 x 1 = 1
    # 1 x 2 = 2
    # 1 x 3 = 3
    # ------
    # 2 x 1 = 2
    # 2 x 2 = 4
    # 2 x 3 = 6
    # ------
    # 3 x 1 = 3
    # 3 x 2 = 6
    # 3 x 3 = 9
    # ------

# 7. Looping through a dictionary
print("\nLooping through a dictionary:")
sample_dict = {'a': 1, 'b': 2, 'c': 3}
for key, value in sample_dict.items():
    print(f"Key: {key}, Value: {value}")

# Output:   
# Looping through a dictionary: 
# Key: a, Value: 1
# Key: b, Value: 2
# Key: c, Value: 3  

# 8. Using enumerate() in a loop
print("\nUsing enumerate in a loop:")
fruits = ['apple', 'banana', 'cherry']
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")

# Output:
# Using enumerate in a loop:
# Index 0: apple
# Index 1: banana
# Index 2: cherry   

# 9. Using list comprehension inside a loop
print("\nList comprehension:")
squares = [x**2 for x in range(6)]
print(squares)

# Output:
# List comprehension:
# [0, 1, 4, 9, 16, 25]

# 10. Using zip() to iterate over two lists together
print("\nUsing zip to iterate over two lists:")
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(f"{name} is {age} years old")

# Output:
# Using zip to iterate over two lists:
# Alice is 25 years old
# Bob is 30 years old
# Charlie is 35 years old

# 11. Infinite loop with a break condition
print("\nInfinite loop with break condition:")
x = 0
while True:
    print("x =", x)
    x += 1
    if x > 3:
        break  # Exits loop when x > 3

# Output:
# Infinite loop with break condition:
# x = 0
# x = 1
# x = 2
# x = 3
