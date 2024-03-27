"""
Below is an example of function overloading example
"""


class Student:

    def __init__(self):
        print("Default Constructor Called")

    def add_marks_two(self, m1, m2):
        return self.m1 + self.m2

    def add_marks_two(self, m1, m2, m3):
        return self.m1 + self.m2 + self.m3


s1 = Student()
a1 = s1.add_marks_two(10, 20)
a2 = s1.add_marks_two(10, 20, 30)

"""
If you run the above code,i will get below error saying m3 argument is missing.
TypeError: Student.add_marks_two() missing 1 required positional argument: 'm3'
Normally add_marks_two will take the last function, if we have overloaded functions. 
"""