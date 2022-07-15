import unittest

from src.song import Song

class TestSong(unittest.TestCase):

    def setUp(self):
        self.song = Song("Wonderwall")
        
    def test_room_exists(self):
        self.assertEqual("Wonderwall", self.song.name)

