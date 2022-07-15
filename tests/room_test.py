import unittest

from src.room import Room

class TestRoom(unittest.TestCase):
    
    def setUp(self):
        self.room = Room("Karoake Room")
        
    def test_room_exists(self):
        self.assertEqual("Karoake Room", self.room.name)





