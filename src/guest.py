class Guest:

    def __init__(self, name, cash):
       self.name = name
       self.cash = cash   

    def guest_pays_entry_fee(self, entry_fee):
        self.cash -= entry_fee