#!/usr/bin/python3
"""This file defines tests cases for the class User"""
import unittest
import pycodestyle


class Test_User(unittest.TestCase):
    """
    Tests for class User
    """

    # Test for Documentation

    def test_pep8_base(self):
        """
        Test that checks PEP8 | Pycodestyle
        """
        syntax = pycodestyle.StyleGuide(quit=True)
        check = syntax.check_files(['models/user.py'])
        self.assertEqual(
            check.total_errors, 0,
            "Found code style error (and warnings)"
        )
