# Function to concatenate two strings
def concatenate_strings(string1, string2):
    return string1 + string2


# Function to find the length of a string
def find_string_length(string):
    return len(string)


# Function to convert a string to uppercase
def convert_to_uppercase(string):
    return string.upper()


# Function to convert a string to lowercase
def convert_to_lowercase(string):
    return string.lower()


# Function to capitalize the first letter of a string
def capitalize_string(string):
    return string.capitalize()


# Function to check if a string starts with a specified prefix
def starts_with_prefix(string, prefix):
    return string.startswith(prefix)


# Function to check if a string ends with a specified suffix
def ends_with_suffix(string, suffix):
    return string.endswith(suffix)


# Function to split a string into a list of substrings based on a delimiter
def split_string(string, delimiter):
    return string.split(delimiter)


# Function to replace occurrences of a substring with another substring in a string
def replace_substring(string, old_substring, new_substring):
    return string.replace(old_substring, new_substring)


# Function to strip leading and trailing whitespace from a string
def strip_whitespace(string):
    return string.strip()


# Function to check if a string contains only alphabetic characters
def is_alpha(string):
    return string.isalpha()


# Function to check if a string contains only alphanumeric characters
def is_alnum(string):
    return string.isalnum()


# Example usage
string1 = "hello"
string2 = "world"
prefix = "he"
suffix = "ld"
delimiter = ","
test_string = "   hello world   "
substring = "lo"
new_substring = "llo"

# Concatenating strings
print("Concatenated string:", concatenate_strings(string1, string2))

# Finding the length of a string
print("Length of string:", find_string_length(string1))

# Converting a string to uppercase
print("Uppercase string:", convert_to_uppercase(string1))

# Converting a string to lowercase
print("Lowercase string:", convert_to_lowercase(string2))

# Capitalizing the first letter of a string
print("Capitalized string:", capitalize_string(string1))

# Checking if a string starts with a prefix
print("Starts with prefix?", starts_with_prefix(string1, prefix))

# Checking if a string ends with a suffix
print("Ends with suffix?", ends_with_suffix(string2, suffix))

# Splitting a string into a list of substrings based on a delimiter
print("Split string:", split_string(test_string, delimiter))

# Replacing occurrences of a substring with another substring in a string
print("Replaced string:", replace_substring(string1, substring, new_substring))

# Stripping leading and trailing whitespace from a string
print("Stripped string:", strip_whitespace(test_string))

# Checking if a string contains only alphabetic characters
print("Is alpha?", is_alpha(string1))

# Checking if a string contains only alphanumeric characters
print("Is alphanumeric?", is_alnum(string1))
