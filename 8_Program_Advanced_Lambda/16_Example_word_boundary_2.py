import re

# Example text
text = "The cost is $20.00. 201."

# Pattern to match the number 20
pattern = re.compile(r'\b20\b')

# Find all occurrences of the number 20
matches = pattern.findall(text)
print(matches)  # Output: ['20']

"""
In this example, \b20\b matches the number 20 when it's a standalone number, but not when it's part of another number like 201 or 2020.
"""