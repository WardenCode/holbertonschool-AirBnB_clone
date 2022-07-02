#!/usr/bin/python3
"""This model defines several tests cases for the BaseModel class"""
import unittest
import pycodestyle
from models import BaseModel, storage
from datetime import datetime


class Test_Base_Model(unittest.TestCase):
    """
    Tests for BaseModel class
    """

    # Test for Documentation

    def test_pep8_base(self):
        """
        Test that checks PEP8 | Pycodestyle
        """
        syntax = pycodestyle.StyleGuide(quit=True)
        check = syntax.check_files(['models/base_model.py'])
        self.assertEqual(
            check.total_errors, 0,
            "Found code style error (and warnings)"
        )

    # Test of Base Model
    def test_created_at(self):
        """Tests 'created_at' time"""
        new_model = BaseModel()
        now = datetime.now().microsecond
        then = new_model.created_at.microsecond
        self.assertLess(now - then, 50)

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

    def test_init_kwargs(self):
        """Tests '__init__' method with kwargs"""
        new_model = BaseModel()
        my_model_json = new_model.to_dict()
        new_model2 = BaseModel(**my_model_json)
        self.assertEqual(new_model.to_dict(), new_model2.to_dict())

    def test_init_args(self):
        """Tests '__init__' method trying args"""
        new_model = BaseModel(5, "05/12/99", "05/12/99")
        self.assertNotEqual(new_model, None)

    # def test_init_bad_kwargs(self):
    #     """Tests '__init__' method with a bad id"""
    #     new_model = BaseModel(id=51)
    #     to_dict = new_model.to_dict()
    #     new_model_2 = BaseModel(to_dict)
    #     self.assertEqual(new_model.to_dict(), new_model_2.to_dict())

    # Test of FileStorage

    def test_function_all(self):
        """Test functions 'all, new, save & reload'"""
        new_model = BaseModel()
        obj_name = new_model.__class__.__name__
        id = new_model.id
        self.assertNotEqual(None, storage.all().get(f"{obj_name}.{id}", None))
