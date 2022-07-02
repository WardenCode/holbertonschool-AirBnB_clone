#!/usr/bin/python3
"""This file defines tests cases for the class Place"""
import unittest
import pycodestyle


class Test_Place(unittest.TestCase):
    """
    Tests for class Place
    """

    # Test for Documentation

    def test_pep8_base(self):
        """
        Test that checks PEP8 | Pycodestyle
        """
        syntax = pycodestyle.StyleGuide(quit=True)
        check = syntax.check_files(['models/place.py'])
        self.assertEqual(
            check.total_errors, 0,
            "Found code style error (and warnings)"
        )
