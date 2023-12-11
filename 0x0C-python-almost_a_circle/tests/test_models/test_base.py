#!/usr/bin/python3

"""

Unittests for Base class.

"""

import unittest
import json

from models.base import Base


class TestBase(unittest.TestCase):
    """Define unittests for Base class."""

    def test_id(self):
        """Test id attribute."""
        b1 = Base()
        b2 = Base()
        b3 = Base(12)
        b4 = Base()
        b5 = Base(3.5)
        b6 = Base("string")
        b7 = Base(True)
        b8 = Base([1, 2, 3])
        b9 = Base({"a": 1, "b": 2})
        b10 = Base(None)
        b11 = Base(-5)
        b12 = Base(0)

        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 12)
        self.assertEqual(b4.id, 3)
        self.assertEqual(b5.id, 3.5)
        self.assertEqual(b6.id, "string")
        self.assertEqual(b7.id, True)
        self.assertEqual(b8.id, [1, 2, 3])
        self.assertEqual(b9.id, {"a": 1, "b": 2})
        self.assertEqual(b10.id, 4)
        self.assertEqual(b11.id, -5)
        self.assertEqual(b12.id, 0)

    def test_to_json_string(self):
        """Test to_json_string method."""
        dict1 = {"id": 1, "width": 2, "height": 3, "x": 4, "y": 5}
        dict2 = {"id": 6, "width": 7, "height": 8, "x": 9, "y": 10}
        dict3 = {"id": 11, "width": 12, "height": 13, "x": 14, "y": 15}
        dict4 = {"id": 16, "width": 17, "height": 18, "x": 19, "y": 20}
        dict5 = {"id": 21, "width": 22, "height": 23, "x": 24, "y": 25}
        dict6 = {"id": 26, "width": 27, "height": 28, "x": 29, "y": 30}

        list_dicts = [dict1, dict2, dict3, dict4, dict5, dict6]
        json_list_dicts = Base.to_json_string(list_dicts)
        self.assertEqual(type(list_dicts), list)
        self.assertEqual(type(json_list_dicts), str)
        self.assertEqual(list_dicts, json.loads(json_list_dicts))
        self.assertEqual("[]", Base.to_json_string([]))
        self.assertEqual("[{\"id\": 12}]", Base.to_json_string([{'id': 12}]))
        self.assertEqual("[]", Base.to_json_string(None))


if __name__ == "__main__":
    unittest.main()
