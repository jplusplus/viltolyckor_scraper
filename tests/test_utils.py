# encoding: utf-8
"""Test utility functions."""
from unittest import TestCase
import os

from viltolyckor.utils import parse_result_page
from requests.exceptions import HTTPError

DATA_DIR = "tests/data"

class TestUtils(TestCase):

    def setUp(self):
        pass

    def test_parse_result_page(self):
        file_path = os.path.join(DATA_DIR, "result_page.html")
        with open(file_path) as f:
            content = f.read()
            data = [x for x in parse_result_page(content)]
            assert len(data) == 13 * 14
            result = data[0]
            assert "year" in result
            assert "viltslag" in result
            assert "month" in result
            assert "value" in result
            assert isinstance(result["value"], int)
