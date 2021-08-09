from src.tests.integration_test.util.make_http_calls import get
import logging


def test_get_users(config):
    logging.info("****")
    get(config["base_url"], "", 200, config["schema_file_path_get_user"])


