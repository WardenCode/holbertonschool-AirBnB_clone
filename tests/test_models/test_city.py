#!/usr/bin/python3
"""This file defines tests cases for the class City"""
import unittest
import pycodestyle


class Test_City(unittest.TestCase):
    """
    Tests for class City
    """

    # Test for Documentation

    def test_pep8_base(self):
        """
        Test that checks PEP8 | Pycodestyle
        """
        syntax = pycodestyle.StyleGuide(quit=True)
        check = syntax.check_files(['models/city.py'])
        self.assertEqual(
            check.total_errors, 0,
            "Found code style error (and warnings)"
        )
