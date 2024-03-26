"""
Any iterator which will return the value as string.
"""

mydict = {"name": "john", "country": "norway"}
myseparator = "test"

output = myseparator.join(mydict)
output1 = "".join(mydict)
print(output)
print(output1)
