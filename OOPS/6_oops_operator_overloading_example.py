"""
Operator Overloading Example
"""


class Student:

    def __init__(self, marks):
        print("Default Constructor Called")
        self.marks = marks

    def __add__(self, other):
        return self.marks + other.marks


s1 = Student(10)
s2 = Student(20)
s3 = s1 + s2
print(s3)
