class Guest:

    def __init__(self, name, cash, favourite_song):
       self.name = name
       self.cash = cash 
       self.favourite_song = favourite_song

    def guest_pays_entry_fee(self, entry_fee):
        self.cash -= entry_fee

    def guests_favourite_song(self, room_playlist):
        if self.favourite_song in room_playlist:
            return "Woohoo!"