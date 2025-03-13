# Special Methods (init, str, etc.) in Python are functions that are called automatically 
# by the interpreter when certain operations are performed on objects.

# vector.py

class Vector:
    """
    A simple Vector class that supports basic operations.
    """

    def __init__(self, x, y):
        """
        Initializes a Vector object with x and y coordinates.

        Args:
            x (float): The x-coordinate of the vector.
            y (float): The y-coordinate of the vector.
        """
        self.x = x
        self.y = y

    def __str__(self):
        """
        Returns a string representation of the vector.

        Returns:
            str: A string in the format "(x, y)".
        """
        return f"({self.x}, {self.y})"

    def __repr__(self):
        """
        Returns a representation of the vector that can be used to recreate it.

        Returns:
            str: A string in the format "Vector(x, y)".
        """
        return f"Vector({self.x}, {self.y})"

    def __eq__(self, other):
        """
        Checks if two vectors are equal.

        Args:
            other (Vector): The vector to compare with.

        Returns:
            bool: True if the vectors are equal, False otherwise.
        """
        return self.x == other.x and self.y == other.y

    def __lt__(self, other):
        """
        Checks if one vector is less than another.

        Args:
            other (Vector): The vector to compare with.

        Returns:
            bool: True if the current vector is less than the other vector, False otherwise.
        """
        return self.x < other.x and self.y < other.y

    def __add__(self, other):
        """
        Adds two vectors together.

        Args:
            other (Vector): The vector to add.

        Returns:
            Vector: A new vector that is the sum of the two vectors.
        """
        return Vector(self.x + other.x, self.y + other.y)


# Example usage:

v1 = Vector(2, 3)
v2 = Vector(4, 5)

print(v1)  # Output: (2, 3)
print(repr(v1))  # Output: Vector(2, 3)

print(v1 == v2)  # Output: False
print(v1 < v2)  # Output: True

v3 = v1 + v2
print(v3)  # Output: (6, 8)