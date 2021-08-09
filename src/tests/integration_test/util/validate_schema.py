from cerberus import Validator
import logging


def validate_schema(expected_schema, response_body):
    validate_response_schema = Validator(expected_schema)
    validate_response_schema(response_body)
    logging.info(validate_response_schema.errors)
    assert validate_response_schema(response_body) == True, f"Schema didn't match ${expected_schema} != schema in the response ${response_body}"