import json
from jsonschema import validate
"""
pip install jsonschema
"""

# JSON Schema
schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "age": {"type": "integer"},
        "city": {"type": "string"}
    },
    "required": ["name", "age", "city"]
}

# JSON data to be validated
json_data = {
    "name": "John Doe",
    "age": 30,
    "city": "New York"
}

try:
    # Validate JSON data against the schema
    validate(instance=json_data, schema=schema)
    print("JSON data is valid.")
except Exception as e:
    print("JSON data is not valid:", e)
