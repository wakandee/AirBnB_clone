#!/usr/bin/python3
"""Test Review Module"""

import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """Test Review class"""

    def test_attributes(self):
        """Test Review attributes"""
        review = Review()
        self.assertTrue(hasattr(review, "place_id"))
        self.assertEqual(review.place_id, "")
        self.assertTrue(hasattr(review, "user_id"))
        self.assertEqual(review.user_id, "")
        self.assertTrue(hasattr(review, "text"))
        self.assertEqual(review.text, "")
