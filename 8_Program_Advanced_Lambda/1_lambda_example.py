"""
Example of lambda function
"""

x = lambda x: x ** 3
print(x(3))

x = lambda x, y: x + y
print(x(10, 20))

x = lambda x, y, z: x * y * z
print(x(2, 3, 4))
