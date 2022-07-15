import unittest

from src.guest import Guest

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest = Guest("Arthur Dent")
        
    def test_guests_exists(self):
        self.assertEqual("Arthur Dent", self.guest.name)
        