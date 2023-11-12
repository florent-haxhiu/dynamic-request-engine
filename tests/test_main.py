import json
from unittest import TestCase

from src.main import send_request
from tests.utils.utils import read_json_resource


class MyTestCase(TestCase):

    def test_request_is_successful(self):
        payload = read_json_resource("example_request.json")
        actual = send_request(json.dumps(payload))

        self.assertEqual("Hello User", actual['output'])
