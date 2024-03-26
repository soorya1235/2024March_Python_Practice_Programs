"""
Program to count no of characters in a string.
"""
a = 'aaaaaabbbbbccccccdddddddeeee'

d = {}

for x in a:
    if x in d:
        d[x] = d[x] + 1
    else:
        d[x] = 1
for k, v in d.items():
    print("{}->{} times".format(k, v))
