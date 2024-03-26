"""
Dictionary Sorting
"""

d1 = {"a": 12, "f": 10, "j": 5, "d": 55, "e": 100}

# Sorting by First Element

sorted_dic1 = sorted(d1.items(), key=lambda x: x[0])

# Sorting by Second Element

sorted_dic2 = sorted(d1.items(), key=lambda x: x[1])

print(sorted_dic1)
print(sorted_dic2)
