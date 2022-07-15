import unittest

from src.room import Room
from src.song import Song
from src.guest import Guest

class TestRoom(unittest.TestCase):
    
    def setUp(self):
        self.room = Room("Karoake Room", 2, 5, 0)
        self.guest = Guest("Arthur Dent", 20)
        self.guest2 = Guest("Frank Zappa", 30)
        self.guest3 = Guest("Sophie Ellis-Bexter", 40)
        self.song = Song("Wonderwall")
        
    def test_room_exists(self):
        self.assertEqual("Karoake Room", self.room.name)

    def test_guest_can_enter_room(self):
        self.room.check_in_guest(self.guest.name)
        self.assertEqual("Arthur Dent", self.room.guest_list[0])

    def test_room_has_song_on_playlist(self):
        self.room.add_song_to_playlist("Wonderwall")
        self.assertEqual("Wonderwall", self.room.playlist[0])

    def test_guest_can_leave_room(self):
        self.room.check_in_guest(self.guest.name)
        self.assertEqual("Arthur Dent", self.room.guest_list[0])
        self.room.check_out_guest(self.guest.name)
        self.assertEqual(0, len(self.room.guest_list))

    def test_room_capacity(self):
        self.room.check_in_guest(self.guest.name)
        self.room.check_in_guest(self.guest2.name)
        self.assertEqual("Room full", self.room.check_in_guest(self.guest3))

    def test_guest_check_in_with_payment(self):
        self.room.check_in_guest(self.guest.name)
        self.guest.guest_pays_entry_fee(self.room.entry_fee)
        self.assertEqual("Arthur Dent", self.room.guest_list[0])
        self.assertEqual(15, self.guest.cash)

    def test_entry_fee_received(self):
        self.room.check_in_guest(self.guest.name)
        self.guest.guest_pays_entry_fee(self.room.entry_fee)
        self.assertEqual(5, self.room.money)










