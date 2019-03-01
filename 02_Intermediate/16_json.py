''' This script shows how to convert python objs to json and vice versa '''
import json

data = {'data':["This is a apple", None, 1, 0, 'string']}

# This will convert python obj to json to use for sending data or storing
json_obj = json.dumps(data, indent=4)

print(json_obj)
# Output :- {"data": ["This is a apple", null, 1, 0, "string"]}

# Convert json obj to pyton obj 
python_obj = json.loads(json_obj)

print(python_obj)
# Output :- {'data': ['This is a apple', None, 1, 0, 'string']}
