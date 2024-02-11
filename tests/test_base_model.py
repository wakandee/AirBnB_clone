import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """
    Test the BaseModel class
    """

    def test_instance_creation(self):
        """
        Test instance creation
        """
        my_model = BaseModel()
        self.assertIsInstance(my_model, BaseModel)

    def test_attributes(self):
        """
        Test instance attributes
        """
        my_model = BaseModel()
        self.assertTrue(hasattr(my_model, 'id'))
        self.assertTrue(hasattr(my_model, 'created_at'))
        self.assertTrue(hasattr(my_model, 'updated_at'))

    def test_str_method(self):
        """
        Test __str__ method
        """
        my_model = BaseModel()
        self.assertEqual(str(my_model), "[BaseModel] ({}) {}".format(
            my_model.id, my_model.__dict__))

    def test_save_method(self):
        """
        Test save method
        """
        my_model = BaseModel()
        old_updated_at = my_model.updated_at
        my_model.save()
        self.assertNotEqual(old_updated_at, my_model.updated_at)

    def test_to_dict_method(self):
        """
        Test to_dict method
        """
        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89
        my_model_json = my_model.to_dict()
        self.assertEqual(my_model_json['id'], my_model.id)
        self.assertEqual(my_model_json['__class__'], 'BaseModel')
        self.assertEqual(my_model_json['name'], "My_First_Model")
        self.assertEqual(my_model_json['my_number'], 89)
        self.assertEqual(my_model_json['created_at'], my_model.created_at.strftime(
            "%Y-%m-%dT%H:%M:%S.%f"))
        self.assertEqual(my_model_json['updated_at'], my_model.updated_at.strftime(
            "%Y-%m-%dT%H:%M:%S.%f"))

    def test_kwargs_datetime(self):
        """
        Test if datetime strings are properly converted to datetime objects
        """
        kwargs = {
            'id': '123',
            'created_at': '2024-02-11T12:00:00.000000',
            'updated_at': '2024-02-11T12:00:00.000000'
        }
        my_model = BaseModel(**kwargs)
        self.assertEqual(my_model.id, '123')
        self.assertEqual(my_model.created_at,
                         datetime(2024, 2, 11, 12, 0, 0))
        self.assertEqual(my_model.updated_at,
                         datetime(2024, 2, 11, 12, 0, 0))


if __name__ == '__main__':
    unittest.main()
