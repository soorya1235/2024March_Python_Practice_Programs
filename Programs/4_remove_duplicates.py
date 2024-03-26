"""
Program to remove the duplicates from the string
"""

str = "aaaaaaaabbbbbbbbbbbbbbccccccccccccccceeeeeeeeeeeeeeeeffffffffffffff"
dup_list = []

for i in str:
    if i not in dup_list:
        dup_list.append(i)

print("Characters without duplicate is {}".format(dup_list))
