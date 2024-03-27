"""
Below is an example of sample class
"""


class Student:

    def __init__(self, a, b):
        self.a = a
        self.b = b
        print("Construtor Called")

    def __del__(self):
        print("Destructor Called")

    def __repr__(self):
        return f"The value of a is {self.a} and value of b is {self.b}"


obj1 = Student(10, 20)
print(obj1.a)
print(obj1.b)
print(obj1)
