# Encapsulation is the process of wrapping data and methods within a class to control access and modify them.
# This can be achieved through the use of private attributes and methods.

# Student Class Example

class Student:
    # Constructor or initializer 
    def __init__(self, name, age, grade):
        # Private attributes. Not accessible outside the class
        self.__name = name
        self.__age = age
        self.__grade = grade

    # Public method to get student name. Accessible outside the class
    def get_name(self):
        return self.__name

    # Public method to get student age. Accessible outside the class
    def get_age(self):
        return self.__age

    # Public method to get student grade. Accessible outside the class
    def get_grade(self):
        return self.__grade

    # Public method to update student grade. Accessible outside the class
    def update_grade(self, new_grade):
        if 0 <= new_grade <= 100:
            self.__grade = new_grade
            print(f"Updated grade to {self.__grade}")
        else:
            print("Invalid grade")

    # Public method to display student details. Accessible outside the class
    def display_details(self):
        print(f"Name: {self.__name}")
        print(f"Age: {self.__age}")
        print(f"Grade: {self.__grade}")

# Create an instance and test encapsulation
student = Student("John Doe", 16, 85)
print(student.get_name())
print(student.get_age())
print(student.get_grade())

# Output:
# John Doe
# 16
# 85

student.update_grade(90)
student.display_details()

# Output:
# Name: John Doe
# Age: 16
# Grade: 90

# Try to access private attribute directly (will raise an AttributeError)
try:
    print(student.__grade)
except AttributeError:
    print("Error: cannot access private attribute directly")

# Output:   
# Error: cannot access private attribute directly