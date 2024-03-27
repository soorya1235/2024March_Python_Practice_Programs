"""
Below is an example of Method Overriding
"""


class Person:

    def __init__(self):
        print("Constructor Called of Person")

    def excercise(self, min):
        print(f"I am exercising for {min} Minutes")


class Employee(Person):

    def __init__(self, m1, m2):
        print("Constructor Called of Employee")
        self.m1 = m1
        self.m2 = m2

    def add_employee_marks(self):
        return self.m1 + self.m2

    def excercise(self, min):
        print(f"I am excersing from Employee class {min + 10}")


p1 = Person()
p1.excercise(10)
e1 = Employee(10, 20)
sum_marks = e1.add_employee_marks()
print(f"The Sum of Marks is {sum_marks}")

# Now I am going to make Person as a parent of Employee
# So what ever function is available in Person will be part of Employee
print(e1.excercise(10))
