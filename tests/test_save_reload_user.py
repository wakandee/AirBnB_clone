#!/usr/bin/python3
"""Module for testing User class."""
import unittest
import os
from models.user import User
from models.engine.file_storage import FileStorage


class TestUser(unittest.TestCase):
    """Test cases for User class."""

    def setUp(self):
        """Set up test environment."""
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def tearDown(self):
        """Tear down test environment."""
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_instance_creation(self):
        """Test User instance creation."""
        user = User()
        self.assertIsInstance(user, User)
        self.assertIsInstance(user, BaseModel)

    def test_attributes_initialization(self):
        """Test User attributes initialization."""
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_to_dict(self):
        """Test to_dict() method of User."""
        user = User()
        user_dict = user.to_dict()
        self.assertIsInstance(user_dict, dict)
        self.assertEqual(user_dict["__class__"], "User")

    def test_save_and_reload(self):
        """Test saving and reloading User instance."""
        user = User()
        user.first_name = "John"
        user.email = "john@example.com"
        user.password = "password"
        user.save()
        user_id = user.id

        storage = FileStorage()
        storage.reload()
        loaded_user = storage.all()["User.{}".format(user_id)]
        self.assertEqual(loaded_user.id, user_id)
        self.assertEqual(loaded_user.first_name, "John")
        self.assertEqual(loaded_user.email, "john@example.com")
        self.assertEqual(loaded_user.password, "password")

if __name__ == "__main__":
    unittest.main()
       
