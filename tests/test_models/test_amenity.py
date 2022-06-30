#!/usr/bin/python3
"""This file defines tests cases for the class Amenity"""
import unittest
import pycodestyle


class Test_Amenity(unittest.TestCase):
    """
    Tests for class Amenity
    """

    # Test for Documentation

    def test_pep8_base(self):
        """
        Test that checks PEP8 | Pycodestyle
        """
        syntax = pycodestyle.StyleGuide(quit=True)
        check = syntax.check_files(['models/amenity.py'])
        self.assertEqual(
            check.total_errors, 0,
            "Found code style error (and warnings)"
        )
