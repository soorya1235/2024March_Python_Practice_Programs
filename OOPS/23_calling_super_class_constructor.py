"""
Calling super class construstor.
In Python, the super() function is the standard way to call the constructor of a superclass (parent class).
However, there is an alternative method to call superclass constructors directly, but it's not recommended
and can lead to maintenance issues.

You can explicitly reference the superclass and call its constructor using the ClassName.__init__(self, args) syntax.
However, this approach is less flexible and can introduce errors if class names change or if the class hierarchy is modified.

Here's an example using this alternative approach:
In this example, Parent.__init__(self, parent_attribute) is used to call the Parent class constructor within the Child class constructor. However,
this method bypasses the flexibility and benefits provided by super() and can cause issues in more complex class hierarchies or when multiple inheritance is involved.
Therefore, it's generally recommended to use super() for calling superclass constructors in Python, as it provides a more flexible and maintainable approach, especially in scenarios involving multiple inheritance.
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
