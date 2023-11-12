import json
import requests


def read_json_file(json_file):
    return json.loads(json_file)


def send_request(json_file: str):
    data = read_json_file(json_file)
    response = call_endpoint(data['url'], data['method'], data['payload'])
    response_body = response.json()
    data['output'] = response_body

    return data


def call_endpoint(url: str, method: str, payload: dict):
    response = requests.request(method.upper(), url, json=payload)
    response.raise_for_status()
    return response
