import unittest

from src.room import Room
from src.song import Song
from src.guest import Guest

class TestRoom(unittest.TestCase):
    
    def setUp(self):
        self.room = Room("Karoake Room")
        self.guest = Guest("Arthur Dent")
        self.song = Song("Wonderwall")
        
    def test_room_exists(self):
        self.assertEqual("Karoake Room", self.room.name)

    def test_guest_can_enter_room(self):
        self.room.add_guest("Arthur Dent")
        self.assertEqual("Arthur Dent", self.room.guest_list[0])

    def test_room_has_song_on_playlist(self):
        self.room.add_song_to_playlist("Wonderwall")
        self.assertEqual("Wonderwall", self.room.playlist[0])

    def test_guest_can_leave_room(self):
        self.room.add_guest("Arthur Dent")
        self.assertEqual("Arthur Dent", self.room.guest_list[0])
        self.room.check_out_guest("Arthur Dent")
        self.assertEqual(0, len(self.room.guest_list))






