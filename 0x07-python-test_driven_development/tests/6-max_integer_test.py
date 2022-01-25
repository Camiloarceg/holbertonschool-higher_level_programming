#!/usr/bin/python3
""" Unittest for ``max_integer`` function """

import unittest
max_integer = __import__('6-max_integer').max_integer


class test_max_integer(unittest.TestCase):
    """
    # unittests for the function ``max_integer(list=[])``
    """

    def test_one_argument(self):
        self.assertEqual(max_integer([9]), 9)
        self.assertEqual(max_integer([-10]), -10)

    def test_positive_numbers(self):
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)
        self.assertEqual(max_integer([700, 0, 12, 6587]), 6587)

    def test_negative_numbers_list(self):
        self.assertEqual(max_integer([-3, -5, -44]), -3)
        self.assertEqual(max_integer([-700, -8, -1000]), -8)

    def test_float_numbers_list(self):
        self.assertEqual(max_integer([10.5, 8.9, 9.4]), 10.5)
        self.assertEqual(max_integer([9.6, 71.5, 9.4]), 71.5)

    def test_same_numbers(self):
        self.assertEqual(max_integer([9, 7, 9]), 9)
        self.assertEqual(max_integer([10, 10, 10]), 10)

    def test_none_list(self):
        self.assertEqual(max_integer([]), None)

    def test_string_list(self):
        """ This function compare with the ASCII values """

        item = ["Hello", "World", "Bye", "Holberton"]
        self.assertEqual(max_integer(item), "World")

    def test_tuple_list(self):
        item = [(7, 8, 9), (10, 11, 12)]
        self.assertEqual(max_integer(item), (10, 11, 12))

    def test_dictionary_list(self):
        item = [{"First": 10, "Second": 20}, {"Third": 1, "Fourth": 2}]
        with self.assertRaises(TypeError):
            max_integer(item)

    def test_string_value(self):
        """ This function compare with the ASCII values """

        self.assertEqual(max_integer("Hello World"), "r")
        self.assertEqual(max_integer("sergio"), "s")
        self.assertEqual(max_integer("Python"), "y")
        self.assertEqual(max_integer("Awesome"), "w")

    def test_mixed_list(self):
        item = ["Hello", 5, 10, "Bye"]
        with self.assertRaises(TypeError):
            max_integer(item)

        item = [10.5, 9, 3.4, 12]
        self.assertEqual(max_integer(item), 12)

        item = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(max_integer(item), [7, 8, 9])


if __name__ == "__main__":
    unittest.main()
