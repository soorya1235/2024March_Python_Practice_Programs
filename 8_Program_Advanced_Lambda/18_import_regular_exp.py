import re

# Example text
text = "I love cats and dogs."

# Pattern to match "cats" or "dogs", but capture only the whole phrase
pattern = re.compile(r'I love (?:cats|dogs)')
pattern1 = re.compile(r'I love (cats|dogs)')

# Find all occurrences of "cats" or "dogs"
matches = pattern.findall(text)
matches1 = pattern1.findall(text)
print(matches)  # Output: ['I love cats', 'I love dogs']
print(matches1)
