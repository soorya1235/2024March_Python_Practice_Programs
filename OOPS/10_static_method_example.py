"""
Example of using the static method
Suppose you want to create a utility function that performs some calculation but doesn't depend on any class or
instance variables. In such cases, a static method is appropriate.

In this example, the add and multiply methods don't rely on any instance or class variables.
They simply perform mathematical operations on the input parameters. Therefore, it's appropriate to define them as
static methods.

In summary:
Use class methods when the method relates to the class itself or involves class-level variables.
Use static methods when the method doesn't depend on instance or class variables and is more like a utility function.
"""


class MathUtils:
    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def multiply(x, y):
        return x * y


# Using static methods for mathematical operations
print("Adding 5 and 3:", MathUtils.add(5, 3))  # Output: 8
print("Multiplying 5 and 3:", MathUtils.multiply(5, 3))  # Output: 15
