"""
Program to reverse the String
"""

str = "soorya"
rev = ""
length = len(str) - 1
while length >= 0:
    rev = rev + str[length]
    length -= 1
print(f"The reverse of the String is {rev}")
