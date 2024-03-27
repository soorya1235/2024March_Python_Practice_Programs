"""
How to access the private method and attribute
"""


class MyClass:
    def __init__(self):
        self.__private_attribute = "I am private"

    def __private_method(self):
        return "I am a private method"


# Accessing private attributes and methods from outside the class
obj = MyClass()

# Accessing private attribute using name mangling
print(obj._MyClass__private_attribute)  # Output: I am private

# Accessing private method using name mangling
print(obj._MyClass__private_method())  # Output: I am a private method
