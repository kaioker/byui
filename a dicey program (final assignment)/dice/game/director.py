from game.die import Die
from game.player import Player
from game.table import Table


class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        dice (List[Die]): A list of Die instances.
        is_playing (boolean): Whether or not the game is being played.
        score (int): The score for one round of play.
        total_score (int): The score for the entire game.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self._players = []
        self._turn = 0
        self._game_not_over = True
        self._is_playing = True
        self._die = None
        self._table = None

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        self._get_players()
        self._get_die()

        self._table = Table(self._die.max())

        while self._game_not_over:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

    def _get_die(self):
        sides = int(input("How many sides? "))
        self._die = Die(sides)

    def _get_players(self):
        players = int(input("How many players? "))
        score = int(input("How many coins? "))
        for i in range(players):
            name = input(f"Player {i + 1} name: ")
            player = Player(name, score)
            self._players.append(player)

    def get_inputs(self):
        """Ask the user if they want to roll.

        Args:
            self (Director): An instance of Director.
        """
        player = self._players[self._turn]
        print()
        print(f"{player.get_name()} has {player.get_coins()} coins.")
        print()

        roll_dice = input("Roll dice? [y/n] ")
        player.set_playing(roll_dice == "y")
       
    def do_updates(self):
        """Updates the player's score.

        Args:
            self (Director): An instance of Director.
        """

        player = self._players[self._turn]

        if not player.is_playing():
            return 

        value = self._die.roll()
        
        if self._table.add_slot(value):
            player.subtract_coins(1)
            print()
            print(f"You rolled a {value}!")

        else:
            print()
            print(f"You rolled a duplicate {value}.")
            player.add_coins(self._table.get_coins())
            self._table.clear_coins()
            player.set_playing(False)

    def do_outputs(self):
        """Displays the dice and the score. Also asks the player if they want to roll again. 

        Args:
            self (Director): An instance of Director.
        """
        player = self._players[self._turn]

        if not player.is_playing():
            self._turn = (self._turn + 1) % len(self._players)

        elif player.get_coins() == 0:
            print()
            print(f"{player.get_name()} has won!")
            self._game_not_over = False
            return
        
        print()
        self._table.print_coins()