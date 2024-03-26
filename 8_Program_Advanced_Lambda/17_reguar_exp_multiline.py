import re

# Example multiline string
multiline_text = """
This is line 1.
This is line 2.
This is line 3.
"""

# Pattern to match lines starting with "This is"
pattern = re.compile(r'^This is', flags=re.MULTILINE)

# Find all lines starting with "This is"
matches = pattern.findall(multiline_text)
print(matches)
