class Room:
    
    def __init__(self, name):
       self.name = name
       self.guest_list = []
       self.playlist = []

    def add_guest(self, guest_name):
        self.guest_list.append(guest_name)

    def add_song_to_playlist(self, song_to_be_added):
        self.playlist.append(song_to_be_added)

    def check_out_guest(self, guest_name):
        self.guest_list.remove(guest_name)


