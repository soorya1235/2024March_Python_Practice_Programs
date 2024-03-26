import re

# Example text
text = "The cat sat on the mat in the catenate of catings."

# Pattern to match the word "cat"
pattern = re.compile(r'\bcat\b')
pattern1 = re.compile(r'cat')

# Find all occurrences of the word "cat"
matches = pattern.findall(text)
matches1 = pattern1.findall(text)
print(matches)  # Output: ['cat']
print(matches1)
