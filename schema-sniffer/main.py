import json

def sniff_schema(json_file, output_file):
    with open(json_file, 'r') as file:
        data = json.load(file)
    
    schema = {}
    message = data.get('message', {})
    
    for key, value in message.items():
        if isinstance(value, dict):
            if 'type' in value:
                schema[key] = {
                    'type': value['type'],
                    'tag': '',
                    'description': '',
                    'required': False
                }
            else:
                schema[key] = sniff_nested_schema(value)
    
    with open(output_file, 'w') as file:
        json.dump(schema, file, indent=4)

def sniff_nested_schema(data):
    schema = {}
    
    for key, value in data.items():
        if isinstance(value, dict):
            if 'type' in value:
                schema[key] = {
                    'type': value['type'],
                    'tag': '',
                    'description': '',
                    'required': False
                }
            else:
                schema[key] = sniff_nested_schema(value)
        elif isinstance(value, list):
            if value and isinstance(value[0], dict):
                schema[key] = {
                    'type': 'array',
                    'items': sniff_nested_schema(value[0]),
                    'tag': '',
                    'description': '',
                    'required': False
                }
            elif value and isinstance(value[0], str):
                schema[key] = {
                    'type': 'enum',
                    'enum': value,
                    'tag': '',
                    'description': '',
                    'required': False
                }
        elif isinstance(value, int):
            schema[key] = {
                'type': 'integer',
                'tag': '',
                'description': '',
                'required': False
            }
        elif isinstance(value, str):
            schema[key] = {
                'type': 'string',
                'tag': '',
                'description': '',
                'required': False
            }
    
    return schema

# Usage example
input_file = './data/data_2.json'
output_file = './schema/schema_2.json'

sniff_schema(input_file, output_file)
