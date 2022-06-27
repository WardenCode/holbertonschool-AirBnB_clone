#!/usr/bin/python3
"""This model defines several tests cases for the BaseModel class"""
from distutils.ccompiler import new_compiler
import unittest
from models.base_model import BaseModel
from datetime import datetime, date


class Test_Base_Model(unittest.TestCase):
    """
        Tests for BaseModel class
    """

    def test_created_at(self):
        """Tests 'created_at' time"""
        new_model = BaseModel()
        now = datetime.now().microsecond
        then = new_model.created_at.microsecond
        self.assertLess(now - then, 10)

    def test_update(self):
        """Tests 'update_at' time"""
        new_model = BaseModel()
        then = new_model.created_at.microsecond
        new_model.save()
        now = new_model.update_at.microsecond
        self.assertGreater(now, then)

    def test_id(self):
        """Tests 'id' values """
        new_model = BaseModel()
        new_model2 = BaseModel()
        self.assertNotEqual(new_model.id, new_model2.id)

    def test_str(self):
        """"Tests __str__ magic method"""
        new_model = BaseModel()
        str_repr = str(new_model)
        self.assertIn(new_model.__class__.__name__, str_repr)
        self.assertIn(new_model.id, str_repr)
        self.assertIn(str(new_model.__dict__), str_repr)

    def test_dict(self):
        """Tests to 'to_dict' method"""
        new_model = BaseModel()
        to_dict = new_model.to_dict()
        for i in to_dict:
            self.assertIsInstance(i, str)
        raised = False
        try:
            datetime.fromisoformat(to_dict["created_at"])
            datetime.fromisoformat(to_dict["update_at"])
        except ValueError as e:
            raised = True
        self.assertFalse(raised)
