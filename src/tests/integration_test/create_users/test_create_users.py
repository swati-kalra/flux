from src.tests.integration_test.util.make_http_calls import post
from src.tests.integration_test.util.filereader import read_json_file_and_return_json_data as jfr


def test_create_users(config):
    data = jfr(config["test_data_file_path_create_user"])
    request_body = data["user2_payload"]
    schema = jfr(config["schema_file_path_create_user"])
    post(config["base_url"], request_body, "", 201, schema["create_users_response_schema"])