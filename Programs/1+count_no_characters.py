"""
python program to count no of characters in the stirng.
"""
from collections import Counter
from operator import countOf

data = "aaaaaaabbbbbbbbbbbbbcccccccccccdddddddddddeeeeeeeeeeeeefffffffffgggggggggggggghhhhh"

output1 = Counter(data)
print(f"No of occurences of Each Character is {output1}")
print("No of occurences of Each Character is {}".format(output1))

# program to find the no of count of characters.

data = countOf(data,"a")
print("No of occurence of character a is {}".format(data))

