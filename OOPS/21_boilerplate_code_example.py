"""
Let's consider an example of boilerplate code in Python where you have a class with multiple attributes and
corresponding getter and setter methods for each attribute. Here's an example:
"""


class Person:
    def __init__(self, name, age, address, email):
        self.name = name
        self.age = age
        self.address = address
        self.email = email

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age

    def get_address(self):
        return self.address

    def set_address(self, address):
        self.address = address

    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = email


"""
In this code:
Each attribute (name, age, address, email) has its own getter and setter methods, resulting in a lot of repetitive code.
To fix this, you can use Python's @property decorator for getters and setters. Here's how you can refactor the code:
"""


class Person:
    def __init__(self, name, age, address, email):
        self._name = name
        self._age = age
        self._address = address
        self._email = email

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, address):
        self._address = address

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email


"""
In this refactored version:
We use @property decorator for getter methods, eliminating the need for separate get_ methods.
We use @<attribute>.setter decorator for setter methods, eliminating the need for separate set_ methods.
We use private variables (_name, _age, _address, _email) to store the attributes internally, following the convention
for data encapsulation in Python.
This refactoring reduces the amount of boilerplate code, making the class more concise and easier to maintain. 
Additionally, it improves readability and adheres to Pythonic conventions.
"""
