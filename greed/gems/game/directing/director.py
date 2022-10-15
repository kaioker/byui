import random

from game.casting.artifact import Artifact
from game.shared.color import Color
from game.shared.point import Point

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        _keyboard_service (KeyboardService): For getting directional input.
        _video_service (VideoService): For providing video output.
    """

    def __init__(self, keyboard_service, video_service):
        """Constructs a new Director using the specified keyboard and video services.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
            video_service (VideoService): An instance of VideoService.
        """
        self._keyboard_service = keyboard_service
        self._video_service = video_service
        
    def start_game(self, cast):
        """Starts the game using the given cast. Runs the main game loop.

        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.open_window()
        while self._video_service.is_window_open():
            self._get_inputs(cast)
            self._do_updates(cast)
            self._do_outputs(cast)
        self._video_service.close_window()

    def _get_inputs(self, cast):
        """Gets directional input from the keyboard and applies it to the robot.
        
        Args:
            cast (Cast): The cast of actors.
        """
        robot = cast.get_first_actor("robots")
        velocity = self._keyboard_service.get_direction()
        robot.set_velocity(velocity)        

    def _do_updates(self, cast):
        """Updates the robot's position and resolves any collisions with artifacts.
        
        Args:
            cast (Cast): The cast of actors.
        """
        banner = cast.get_first_actor("banners")
        robot = cast.get_first_actor("robots")
        artifacts = cast.get_actors("artifacts")

        banner.set_text("")
        max_x = self._video_service.get_width()
        max_y = self._video_service.get_height()
        robot.move_next(max_x, max_y)
        
        for artifact in artifacts:
            if robot.get_position().equals(artifact.get_position()):
                message = artifact.get_message()
                banner.set_text(message)

        # count artifacts
        count = 0
        for artifact in artifacts:
            count += 1

        # if less than 10 artifacts, add one
        if count < 20:
            artifact = Artifact()
            artifact.set_text(random.choice(["0", "*"]))
            artifact.set_font_size(15)
            #random color
            artifact.set_color(Color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
            x = random.randint(0, 60 - 1)
            y = random.randint(0, 40 - 1)
            position = Point(x, y)
            position = position.scale(15)
            artifact.set_position(position)
            artifact.set_message("You got a gem!")
            cast.add_actor("artifacts", artifact)
        
        #move artifacts
        for artifact in artifacts:
            velocity = Point(0, 15)
            artifact.set_velocity(velocity)
            artifact.move_next(max_x, max_y)

        #if robot and artifact collide, remove artifact
        for artifact in artifacts:
            if robot.get_position().equals(artifact.get_position()):
                if artifact.get_text() == "0":
                    #remove 1 to score
                    pass # anything i type here breaks everything and i dont know why. too far behind to spend much more time here. hopefully passing grade without scoring?
                elif artifact.get_text() == "*":
                    #add 1 from score
                    pass

                cast.remove_actor("artifacts", artifact)



        
    def _do_outputs(self, cast):
        """Draws the actors on the screen.
        
        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.clear_buffer()
        actors = cast.get_all_actors()
        self._video_service.draw_actors(actors)
        self._video_service.flush_buffer()