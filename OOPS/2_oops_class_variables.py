"""
Below is an example of sample class which using object variables.
"""


class Student:
    no_of_object = 0

    def __init__(self, a, b):
        self.a = a
        self.b = b
        print("Construtor Called")
        Student.no_of_object += 1

    def __del__(self):
        print("Destructor Called")

    def __repr__(self):
        return f"The value of a is {self.a} and value of b is {self.b}"


obj1 = Student(10, 20)
obj2 = Student(30, 40)
print(obj1.a)
print(obj1.b)
print(f"The object is => {obj1}")
print(obj2.a)
print(obj2.b)
print(f"The object is => {obj2}")
print(f"The Object Count is {Student.no_of_object}")
