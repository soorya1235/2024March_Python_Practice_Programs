"""
Below is an example of using class method as alternative constructors
"""


class Person:

    def __init__(self, name, age):
        self.name = name

        self.age = age

    @classmethod
    def from_birth_year(cls, name, birth_year):
        # breakpoint()
        age = cls.calculate_age(birth_year)

        return cls(name, age)

    @staticmethod
    def calculate_age(birth_year):
        current_year = 2024  # Assuming the current year is 2024

        return current_year - birth_year


person1 = Person("Alice", 25)
print(f"{person1.name} is {person1.age} years old.")

# Creating an instance using the class method as an alternative constructor
person2 = Person.from_birth_year("Bob", 1990)
print(f"{person2.name} is {person2.age} years old.")
