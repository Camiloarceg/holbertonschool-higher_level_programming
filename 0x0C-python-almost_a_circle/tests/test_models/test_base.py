#!/usr/bin/python3
"""Unittest for max_integer([..])
"""

import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    def test_int_base_is_None(self):
        b1 = Base()
        self.assertEqual(b1.id, 2)
        b2 = Base()
        self.assertEqual(b2.id, 3)
        b3 = Base()
        self.assertEqual(b3.id, 4)

    def test_int_base(self):
        b4 = Base(12)
        self.assertEqual(b4.id, 12)
        b5 = Base()
        self.assertEqual(b5.id, 1)

    def test_json_string(self):
        dictionary = {'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10}
        self.assertEqual(Base.to_json_string([dictionary]), '[{"x": 1, "y": 9, "id": 1, "height": 2, "width": 10}]')
        dictionary = []
        self.assertEqual(Base.to_json_string(dictionary), '[]')

    def test_json_error(self):
        dictionary = 'a'
        self.assertIsNotNone(Base.to_json_string(dictionary), '[]')
        dictionary = ()
        self.assertIsNotNone(Base.to_json_string(dictionary), '[]')

    def test_from_json_string(self):
        list_input = [
        {'id': 89, 'width': 10, 'height': 4}, 
        {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = Base.to_json_string(list_input)
        self.assertEqual(Base.from_json_string(json_list_input), [{'id': 89, 'width': 10, 'height': 4}, {'id': 7, 'width': 1, 'height': 7}])
