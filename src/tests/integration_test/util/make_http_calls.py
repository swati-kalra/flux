import requests
from src.tests.integration_test.util.filereader import read_json_file_and_return_json_data as jfr
from src.tests.integration_test.util.validate_schema import validate_schema


def get(base_url, headers, expected_response_code, expected_schema):
    response = requests.get(base_url, headers=headers)
    validate_api_status_code(expected_response_code, response.status_code)
    schema = jfr(expected_schema)
    validate_api_schema(schema, response.json())


def post(base_url, request_body, headers, expected_response_code, expected_schema):
    response = requests.post(base_url, request_body, headers=headers)
    validate_api_status_code(expected_response_code, response.status_code)
    validate_api_schema(expected_schema, response.json())


def validate_api_status_code(expected_response_code, actual_response_code):
    assert expected_response_code == actual_response_code, f"Assertion failed for response code ${expected_response_code} != ${actual_response_code}"


def validate_api_schema(expected_schema, actual_schema):
    validate_schema(expected_schema, actual_schema)