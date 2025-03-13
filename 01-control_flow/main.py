# Control Flow
# Control Flow is the process of making decisions in a program based on certain conditions.

# Use an if-else statement to evaluate multiple conditions and return one of three possible values
x = 10

if x < 5:  
    result = "LOW"
elif x < 10:  
    result = "MEDIUM"  
else:  # If none of the above conditions are true
    result = "HIGH" 

# Print the result
print(result)  # Output: HIGH

# Define a function to calculate grades using a match statement
def calculate_grade(score):
    match score:
        case score if score >= 90:
            return "A"
        case score if score >= 80:
            return "B"
        case score if score >= 70:
            return "C"
        case score if score >= 60:
            return "D"
        case _:
            return "F"

# Define a list of student scores
student_scores = [85, 92, 78, 65, 98, 72]

# Use a for loop to iterate over the scores and calculate grades
for score in student_scores:
    grade = calculate_grade(score)

    # The 'f' prefix before the string indicates (formatted string literal)
    # This is equivalent to concatenating the strings "Score: " and score using the + operator
    print(f"Score: {score}, Grade: {grade}") 

    # Output:
    # Score: 85, Grade: B
    # Score: 92, Grade: A
    # Score: 78, Grade: C
    # Score: 65, Grade: D
    # Score: 98, Grade: A
    # Score: 72, Grade: C

# Use a while loop to ask the user for input until they enter a valid score
# The try except block is used to handle errors as the user enters invalid input
while True:
    user_score = input("Enter a score (0-100): ")
    try:
        user_score = int(user_score)
        if user_score < 0 or user_score > 100:
            print("Invalid score. Please try again.")
        else:
            user_grade = calculate_grade(user_score)
            print(f"Score: {user_score}, Grade: {user_grade}")
            break
    except ValueError:
        print("Invalid input. Please enter a number.")

# Output:
# Enter a score (0-100): 85
# Score: 85, Grade: B

# Use a nested loop to print a multiplication table
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i} x {j} = {i*j}")

        # Output:
        # 1 x 1 = 1
        # 1 x 2 = 2
        # 1 x 3 = 3
        # 1 x 4 = 4
        # 1 x 5 = 5
        # 2 x 1 = 2
        # 2 x 2 = 4
        # 2 x 3 = 6
        # 2 x 4 = 8
        # 2 x 5 = 10
        # .......

# Use a recursive function to calculate the factorial of a number
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))     # Output: 120

# Use a list comprehension to create a list of squared numbers
numbers = [1, 2, 3, 4, 5]
squared_numbers = [x**2 for x in numbers]
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]

# Use a generator expression to create a generator of squared numbers
numbers = [1, 2, 3, 4, 5]
squared_numbers = (x**2 for x in numbers)
for num in squared_numbers:
    print(num)
    # Output:
    # 1
    # 4
    # 9
    # 16
    # 25

# Use a ternary operator to print a message based on a condition
x = 5
y = "Greater than 10" if x > 10 else "Less than or equal to 10"
print(y)                # Output: Less than or equal to 10

# Use chained if statements to print a message based on multiple conditions
x = 5
if x > 10:
    print("Greater than 10")
elif x == 5:
    print("Equal to 5") # Output: Equal to 5    
else:
    print("Less than 10")

