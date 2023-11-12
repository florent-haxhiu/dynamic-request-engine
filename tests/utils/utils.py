import json


def read_json_resource(file_name: str):
    with open(f'resources/{file_name}', 'r') as f:
        return json.load(f)
