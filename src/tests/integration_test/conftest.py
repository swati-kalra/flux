import pytest
from src.tests.integration_test.util.filereader import read_json_file_and_return_json_data as jfr


@pytest.fixture()
def config():
    config = jfr("test_data/environments/dev.json")
    return config
