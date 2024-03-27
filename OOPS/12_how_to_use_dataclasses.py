"""
Below is an example of using data classes.
The @dataclass decorator is used to create a data class.
The Point class has two attributes x and y.
Instances of the Point class can be created without writing explicit __init__ or __repr__ methods;
these are automatically generated.
The __repr__ method provides a string representation of the object.
Data classes provide default implementations of comparison methods (__eq__, __ne__, etc.), so you can easily compare
instances.
Data classes are especially useful when you need to create simple classes to hold data without a lot of boilerplate code.
They are a concise and convenient way to define classes for data storage.
"""

from dataclasses import dataclass


@dataclass
class Point:
    x: int
    y: int


# Creating instances of the Point class

point1 = Point(1, 2)

point2 = Point(x=3, y=4)

# Printing the instances

print(point1)  # Output: Point(x=1, y=2)
print(point2)  # Output: Point(x=3, y=4)

# Accessing attributes
print(f"X coordinate: {point1.x}")  # Output: X coordinate: 1
print(f"Y coordinate: {point2.y}")  # Output: Y coordinate: 4

# Comparison

print(point1 == point2)  # Output: False
