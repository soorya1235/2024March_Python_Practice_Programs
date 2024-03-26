"""
Below is an example of list comprehensions
3 types of list comprehensions
"""

data = list(range(0, 10))
print(data)

# Method 1

x = [x for x in data if x % 2 == 0]
print(x)

# Method 2

x = [x ** 2 for x in data]
print(x)

# Method 3
x = ["True" if x % 2 == 0 else "False" for x in data]
print(x)
