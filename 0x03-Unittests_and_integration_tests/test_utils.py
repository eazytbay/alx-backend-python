#!/usr/bin/env python3
"""Unittest created for access_nested_map function of utils module"""


from utils import access_nested_map, get_json, memoize
import unittest
import requests
from unittest.mock import MagicMock, patch
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """A unittest for the access_nested_map function"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
        ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        self.assertEqual(access_nested_map(nested_map, path), expected_result)

    @parameterized.expand([
        ({}, ("a")),
        ({"a": 1}, ("a", "b")),
        ])
    def test_access_nested_map_exception(self, nested_map, path):
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """A unittest for the get_json function"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('utils.requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        mock_response = MagicMock()
        mock_response.json.return_value = test_payload

        mock_get.return_value = mock_response

        rslt = get_json(test_url)
        self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    """ Tests the memoized wrapper function"""
    def test_memoize(self):
        """testing the memoized wrapper function if it memoizes values"""
        class TestClass:
            """A class used for testing memoization"""
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()
        with patch.object(TestClass, 'a_method', return_value=42) as mocked:
            test = TestClass()
            rslt1 = test.a_property
            rslt2 = test.a_property
            self.assertEqual(result1, 42)
            mocked.assert_called_once()
