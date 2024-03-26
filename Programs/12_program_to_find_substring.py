"""
Program to find sub stirng.
"""

abcd = "This is the fist name of the color god in the country"
check = "god"
pos = -1
length = len(abcd) - 1

while True:
    val = abcd.find(check, pos + 1, length)
    if val == -1:
        print("String not found")
        break
    else:
        print("String Found", val)
        break
