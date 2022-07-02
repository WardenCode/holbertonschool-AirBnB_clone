#!/usr/bin/python3
"""This file defines tests cases for the class Review"""
import unittest
import pycodestyle


class Test_Review(unittest.TestCase):
    """
    Tests for class Review
    """

    # Test for Documentation

    def test_pep8_base(self):
        """
        Test that checks PEP8 | Pycodestyle
        """
        syntax = pycodestyle.StyleGuide(quit=True)
        check = syntax.check_files(['models/review.py'])
        self.assertEqual(
            check.total_errors, 0,
            "Found code style error (and warnings)"
        )
