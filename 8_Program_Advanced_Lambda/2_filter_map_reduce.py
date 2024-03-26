"""
Example of Filter,map,reduce
"""
from functools import reduce

x1 = [1, 2, 3, 4, 5, 6, 7, 8]
l1 = filter(lambda x: x % 2 == 0, x1)
print(list(l1))

# Example of Map

m2 = map(lambda x: x ** 2, x1)
print(list(m2))

# Example of Reduce
m3 = reduce(lambda x, y: x + y, x1)
print(m3)
