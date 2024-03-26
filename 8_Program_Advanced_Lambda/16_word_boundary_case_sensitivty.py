import re

# Example text
text = "The quick brown fox JUMPED over the lazy dog."

# Pattern to match the word "jumped" case insensitively
pattern = re.compile(r'\bjumped\b', re.IGNORECASE)

# Find all occurrences of the word "jumped" (case insensitive)
matches = pattern.findall(text)
print(matches)  # Output: ['JUMPED']

""""
In this example, \bjumped\b matches the word "jumped" regardless of its case, as \b ensures that it matches only standalone occurrences.

These examples demonstrate how \b is used to match word boundaries in regular expressions, allowing you to match whole words or numbers in text.
"""