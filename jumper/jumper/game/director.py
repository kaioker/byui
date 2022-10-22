import os
import random
from game.terminal_service import TerminalService
from game.hider import Hider
from game.seeker import Seeker


class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        hider (Hider): The game's hider.
        is_playing (boolean): Whether or not to keep playing.
        seeker (Seeker): The game's seeker.
        terminal_service: For getting and displaying information on the terminal.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self._is_playing = True
        self._seeker = Seeker()
        self._terminal_service = TerminalService()
        with open(os.path.dirname(os.path.abspath(__file__)) + "/words.txt", "r") as file:
            words = file.readlines()
            #random word
            word = random.choice(words)
            word = word.strip()
            
        print(word)
        self._hider = Hider(word)
        
    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """

        #python read a text file 


        while self._is_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

    def _get_inputs(self):
        """Moves the seeker to a new location.

        Args:
            self (Director): An instance of Director.
        """
        letter = self._terminal_service.read_text("\nEnter a letter: ")
        self._seeker.add_letter(letter)
        
    def _do_updates(self):
        """Keeps watch on where the seeker is moving.

        Args:
            self (Director): An instance of Director.
        """
        self._hider.check_letters(self._seeker)
        
    def _do_outputs(self):
        """Provides a hint for the seeker to use.

        Args:
            self (Director): An instance of Director.
        """

        wrong = len(self._hider.wrong_letters(self._seeker))

        # self._terminal_service.write_text(hint)
        # if self._hider.is_found():
        #     self._is_playing = False

        strings = [
            "   ___   ",
            " /_____\ ",
            " \     / ",
            "  \   /  ",
            "    0    ",
            "   /|\   ",
            "   / \   ",
        ]

        for i in range(0, len(strings)):
            if wrong <= i:    
                print(strings[i])


        if wrong >= 4:
            self._is_playing = False
            print("You lose!")
            print(f"The word was {self._hider._location}")

        if self._hider.is_found(self._seeker):
            self._is_playing = False
            print("You win!")
            print(f"The word was {self._hider._location}")

        