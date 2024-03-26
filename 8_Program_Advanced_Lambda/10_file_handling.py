# Function to read data from a file
def read_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            data = file.read()
        return data
    except FileNotFoundError:
        return "File not found"


# Function to write data to a file
def write_to_file(file_path, data):
    with open(file_path, 'w') as file:
        file.write(data)


# Function to append data to a file
def append_to_file(file_path, data):
    with open(file_path, 'a') as file:
        file.write(data)


# Function to remove newlines from a file
def remove_newlines(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
        # Remove newlines from each line
        lines = [line.strip() for line in lines]
        # Write back to the file
        with open(file_path, 'w') as file:
            file.writelines(lines)
    except FileNotFoundError:
        return "File not found"


# Example usage
file_path = "example.txt"
data_to_write = "Hello, world!\nThis is a new line."

# Writing to a file
write_to_file(file_path, data_to_write)

# Reading from a file
data_read = read_from_file(file_path)
print("Data read from file:", data_read)

# Appending to a file
data_to_append = "\nThis line is appended."
append_to_file(file_path, data_to_append)

# Reading from the file again after appending
data_read = read_from_file(file_path)
print("Data read from file after appending:", data_read)

# Removing newlines from the file
remove_newlines(file_path)

# Reading from the file after removing newlines
data_read = read_from_file(file_path)
print("Data read from file after removing newlines:", data_read)
