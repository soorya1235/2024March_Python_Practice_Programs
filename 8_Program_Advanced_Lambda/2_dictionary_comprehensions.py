"""
Below program is example of dictionary comprehensions.
#{x:y for x,y in dic.items()}
#{x:y**2 for x,y in dic.items() if x%2==0 or condition}
#{if/else condition for x,y in dic.items()}
"""

d1 = {"a": 1, "b": 20, "c": 3, "d": 2, "e": 40, "f": 25}
d21 = {"a": 1, "b": 20, "c": 3, "d": 2, "e": 40, "f": 25}

# Method 1 dictonary comprehenisons

d1 = {x: y ** 2 for x, y in d1.items()}
print(d1)

# Method 2 dictionary comprehension2

d2 = {x: "True" if y % 2 == 0 else "False" for x, y in d1.items()}
print(d2)

# Method 3 of using dictionary comprehensions

d3 = {x: y for x, y in d21.items()}
print(d3)
