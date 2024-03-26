"""
Example of Json load,loads,dump,dumps
"""
import json

data1 = {"a": 1, "b": 2, "c": 3}

# Example of Json dumps

data_dumps = json.dumps(data1)
print(type(data_dumps))
print(data_dumps)

# Example of Json loads.

data_loads = json.loads(data_dumps)
print(type(data_loads))
print(data_loads)

# Example of Json dump

# Sample data
data = {
    "name": "John Doe",
    "age": 30,
    "city": "New York"
}

# File path
file_path = "data.json"
# Writing JSON data to file using json.dump
with open(file_path, 'w') as json_file:
    json.dump(data, json_file)
print("JSON data has been written to", file_path)

# Example of json.load

# File path
file_path = "data.json"

# Reading JSON data from file using json.load
with open(file_path, 'r') as json_file:
    data = json.load(json_file)

print("Data loaded from", file_path)
print("Type of Data is",type(data))
print("Name:", data["name"])
print("Age:", data["age"])
print("City:", data["city"])
