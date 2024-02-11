# models/__init__.py

"""This module initializes the package."""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
