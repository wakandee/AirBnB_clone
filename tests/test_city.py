#!/usr/bin/python3
"""Test City Module"""

import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """Test City class"""

    def test_attributes(self):
        """Test City attributes"""
        city = City()
        self.assertTrue(hasattr(city, "state_id"))
        self.assertEqual(city.state_id, "")
        self.assertTrue(hasattr(city, "name"))
        self.assertEqual(city.name, "")
