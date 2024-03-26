import re

text = "The color of the sky is blueeeeeee."

# Match "blue" followed by at least one "e", and capture only "blue"
pattern = re.compile(r'blue')
match = pattern.search(text)
if match:
    print(match.group())  # Output: 'blue'
