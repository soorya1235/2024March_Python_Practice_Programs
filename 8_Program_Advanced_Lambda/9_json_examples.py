import json

# Example data
data = {
    "name": "John Doe",
    "age": 30,
    "city": "New York"
}


# json.dump() - Serialize Python object to a JSON formatted stream (write to file)
def example_json_dump(data, file_path):
    with open(file_path, 'w') as json_file:
        json.dump(data, json_file)


# json.load() - Deserialize JSON formatted string or file-like object to a Python object (read from file)
def example_json_load(file_path):
    with open(file_path, 'r') as json_file:
        loaded_data = json.load(json_file)
    return loaded_data


# json.dumps() - Serialize Python object to a JSON formatted string (serialize to string)
def example_json_dumps(data):
    json_string = json.dumps(data)
    return json_string


# json.loads() - Deserialize JSON formatted string to a Python object (deserialize from string)
def example_json_loads(json_string):
    loaded_data = json.loads(json_string)
    return loaded_data


# Example usage
file_path = "data.json"

# Using json.dump() to write data to a file
example_json_dump(data, file_path)

# Using json.load() to read data from a file
loaded_data = example_json_load(file_path)
print("Data loaded from", file_path, ":", loaded_data)

# Using json.dumps() to serialize data to a JSON formatted string
json_string = example_json_dumps(data)
print("Serialized JSON string:", json_string)

# Using json.loads() to deserialize JSON formatted string to a Python object
loaded_data_from_string = example_json_loads(json_string)
print("Data loaded from JSON string:", loaded_data_from_string)
