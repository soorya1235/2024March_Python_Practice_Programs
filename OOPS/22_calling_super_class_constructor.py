"""
Example of calling super class constructor
"""


class Parent:
    def __init__(self, parent_attribute):
        self.parent_attribute = parent_attribute
        print("Parent class constructor called")


class Child(Parent):
    def __init__(self, parent_attribute, child_attribute):
        super().__init__(parent_attribute)  # Calling the superclass constructor
        self.child_attribute = child_attribute
        print("Child class constructor called")


# Creating an instance of the Child class
child_obj = Child("Parent attribute value", "Child attribute value")

# Accessing attributes of the Child class
print("Parent attribute:", child_obj.parent_attribute)
print("Child attribute:", child_obj.child_attribute)
