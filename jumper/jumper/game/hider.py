import random

class Hider:
    """The person hiding from the Seeker. 
    
    The responsibility of Hider is to keep track of its location and distance from the seeker. 
    
    Attributes:
        _location (int): The location of the hider (1-1000).
        _distance (List[int]): The distance from the seeker.
    """

    def __init__(self, word):
        """Constructs a new Hider.

        Args:
            self (Hider): An instance of Hider.
        """
        self._location = word
        
    def check_letters(self, seeker):
        """Watches the seeker by keeping track of how far away it is.

        Args:
            self (Hider): An instance of Hider.
        """
        
        seeker_letters = seeker.get_letters()
        hider_letters = self._location
        for letter in hider_letters:
            if letter in seeker_letters:
                print(letter, end="")
            else:
                print("_", end="")

        print()

    def wrong_letters(self, seeker):
        """Watches the seeker by keeping track of how far away it is.

        Args:
            self (Hider): An instance of Hider.
        """
        seeker_letters = seeker.get_letters()
        hider_letters = self._location
        wrong_letters = []
        for letter in seeker_letters:
            if letter not in hider_letters:
                wrong_letters.append(letter)
        return wrong_letters
            
    def is_found(self, seeker):
        """Determines if the seeker has found the hider.

        Args:
            self (Hider): An instance of Hider.

        Returns:
            boolean: True if the seeker has found the hider, False if not.
        """
        seeker_letters = seeker.get_letters()
        hider_letters = self._location
        for letter in hider_letters:
            if letter not in seeker_letters:
                return False
        return True