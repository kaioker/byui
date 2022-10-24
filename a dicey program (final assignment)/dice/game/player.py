class Player:

    def __init__(self, name, score):
        
        self._is_playing = True
        self._coins = score
        self.rolls = 0
        self.name = name

    def get_coins(self):
        return self._coins

    def add_coins(self, coins):
        self._coins += coins

    def subtract_coins(self, coins):
        self._coins -= coins

    def is_playing(self):
        return self._is_playing

    def set_playing(self, playing):
        self._is_playing = playing

    def get_name(self):
        return self.name
        

