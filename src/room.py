class Room:
    
    def __init__(self, name, capacity, entry_fee, money):
       self.name = name
       self.capacity = capacity
       self.entry_fee = entry_fee
       self.money = money
       self.guest_list = []
       self.playlist = []

    def check_in_guest(self, guest_name):
        if len(self.guest_list) == self.capacity:
            return "Room full"
        self.guest_list.append(guest_name)
        self.money += 5

    def add_song_to_playlist(self, song_to_be_added):
        self.playlist.append(song_to_be_added)

    def check_out_guest(self, guest_name):
        self.guest_list.remove(guest_name)


