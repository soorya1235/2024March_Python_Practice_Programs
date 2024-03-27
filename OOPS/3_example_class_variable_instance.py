"""
Example of Class and instance variables.
Instance Variables:
Instance variables are unique to each instance (object) of a class.
They are defined within a class but outside of any methods.
Each object of the class has its own copy of instance variables, and changes made to these variables are local to that object.
Instance variables are typically initialized within the constructor method (__init__ in Python) using the self keyword.
They represent the attributes or properties of individual objects.

Class Variables:
Class variables are shared among all instances of a class.
They are defined within a class but outside of any instance methods, usually at the top of the class definition.
Class variables are accessed using the class name itself or through any instance of the class.
Changes made to class variables are reflected across all instances of the class.
They represent attributes or properties that are common to all objects of that class.
"""


class Car:
    wheels = 4  # Class variable

    def __init__(self, make, model):
        self.make = make  # Instance variable
        self.model = model  # Instance variable


# Creating instances of the Car class
car1 = Car("Toyota", "Camry")
car2 = Car("Honda", "Accord")

# Accessing and printing instance variables
print("Car 1 Make:", car1.make)  # Output: Toyota
print("Car 2 Make:", car2.make)  # Output: Honda

# Accessing and printing class variable through instances
print("Car 1 Wheels:", car1.wheels)  # Output: 4
print("Car 2 Wheels:", car2.wheels)  # Output: 4

# Accessing and printing class variable through class name
print("Class Variable Wheels:", Car.wheels)  # Output: 4

# Modifying class variable
Car.wheels = 6
print("Car 1 Wheels after modification:", car1.wheels)  # Output: 6
print("Car 2 Wheels after modification:", car2.wheels)  # Output: 6
