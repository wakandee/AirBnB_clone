import unittest
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import os


class TestFileStorage(unittest.TestCase):
    """Test cases for the FileStorage class."""

    def test_attributes(self):
        """Test the attributes of FileStorage class."""
        self.assertTrue(hasattr(FileStorage, '_FileStorage__file_path'))
        self.assertTrue(hasattr(FileStorage, '_FileStorage__objects'))
        self.assertIsInstance(storage, FileStorage)

    def test_all(self):
        """Test the all() method."""
        obj_dict = storage.all()
        self.assertIsInstance(obj_dict, dict)
        self.assertIs(obj_dict, storage._FileStorage__objects)

    def test_new(self):
        """Test the new() method."""
        bm = BaseModel()
        storage.new(bm)
        key = "{}.{}".format(type(bm).__name__, bm.id)
        obj_dict = storage.all()
        self.assertIn(key, obj_dict)

    def test_save(self):
        """Test the save() method."""
        bm = BaseModel()
        storage.new(bm)
        storage.save()
        file_path = storage._FileStorage__file_path
        self.assertTrue(os.path.exists(file_path))
        with open(file_path, 'r') as file:
            lines = file.readlines()
            self.assertGreater(len(lines), 0)

    def test_reload(self):
        """Test the reload() method."""
        bm = BaseModel()
        bm.save()
        storage._FileStorage__objects = {}
        storage.reload()
        key = "{}.{}".format(type(bm).__name__, bm.id)
        obj_dict = storage.all()
        self.assertIn(key, obj_dict)


if __name__ == '__main__':
    unittest.main()
