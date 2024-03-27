"""
Certainly! Below is a Python file with documentation that demonstrates the usage of public, protected,
and private access specifiers within a class:
"""


class AccessSpecifierDemo:
    """
    This class demonstrates the usage of public, protected, and private access specifiers in Python.

    Attributes:
        public_attribute: A public attribute accessible from outside the class.
        _protected_attribute: A protected attribute intended for use within the class and its subclasses.
        __private_attribute: A private attribute intended for use only within the class.
    """

    def __init__(self):
        """
        Initializes the AccessSpecifierDemo class with attributes.
        """
        self.public_attribute = "I am public"
        self._protected_attribute = "I am protected"
        self.__private_attribute = "I am private"

    def public_method(self):
        """
        A public method accessible from outside the class.

        Returns:
            str: A string indicating that it is a public method.
        """
        return "I am a public method"

    def _protected_method(self):
        """
        A protected method intended for use within the class and its subclasses.

        Returns:
            str: A string indicating that it is a protected method.
        """
        return "I am a protected method"

    def __private_method(self):
        """
        A private method intended for use only within the class.

        Returns:
            str: A string indicating that it is a private method.
        """
        return "I am a private method"


# Example usage
obj = AccessSpecifierDemo()

# Accessing public members
print(obj.public_attribute)  # Accessing a public attribute
print(obj.public_method())  # Accessing a public method

# Accessing protected members
print(obj._protected_attribute)  # Accessing a protected attribute
print(obj._protected_method())  # Accessing a protected method

# Attempting to access private members will raise an AttributeError
# print(obj.__private_attribute)
# print(obj.__private_method())

"""
This code file includes a class named AccessSpecifierDemo, which demonstrates the usage of public, protected, 
and private access specifiers. Each member (attributes and methods) is documented with appropriate docstrings 
explaining its purpose and accessibility. The example usage section demonstrates how to access members with different
access levels from outside the class. Finally, attempting to access private members directly from outside the 
class will raise an AttributeError, showcasing the encapsulation principle in action.
"""
