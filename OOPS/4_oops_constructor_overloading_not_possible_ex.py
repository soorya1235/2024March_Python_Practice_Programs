"""
Below is an example of constructor overloading example
"""


class Student:

    def __init__(self):
        print("Default Constructor Called")

    def __int__(self, a, b):
        self.a = a
        self.b = b
        print("Default Constructor Called with values a and b")


s1 = Student()
s1 = Student(10, 20)

"""
If you run the program with out commenting line 17 and 18,i will get error
TypeError: Student.__init__() takes 1 positional argument but 3 were given
Constructor Overloading is not possible,it will take the default constructor
with no parameters.
"""
