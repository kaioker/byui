import constants
from game.casting.actor import Actor
from game.shared.point import Point
from game.casting.cast import Cast


class Tron(Actor):
    """
    A long limbless reptile.
    
    The responsibility of tron is to move itself.

    Attributes:
        _points (int): The number of points the food is worth.
    """
    def __init__(self, player):
        super().__init__()
        self.player = player
        self._segments = []
        self._prepare_body()
        self._dead = False

    def die(self):
        self._dead = True
        for segment in self._segments:
            segment.set_color(constants.WHITE)

    def get_segments(self):
        return self._segments

    def move_next(self):
        # move all segments
        for segment in self._segments:
            segment.move_next()
        # update velocities
        for i in range(len(self._segments) - 1, 0, -1):
            trailing = self._segments[i]
            previous = self._segments[i - 1]
            velocity = previous.get_velocity()
            trailing.set_velocity(velocity)
        self.grow_tail(1)

    def get_head(self):
        return self._segments[0]

    def grow_tail(self, number_of_segments):
        for i in range(number_of_segments):
            tail = self._segments[-1]
            velocity = tail.get_velocity()
            offset = velocity.reverse()
            position = tail.get_position().add(offset)
            
            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text("#")
            if self._dead:
                body_color = constants.WHITE
            elif self.player == 1:
                body_color = constants.RED
            elif self.player == 2:
                body_color = constants.GREEN

            segment.set_color(body_color)
            self._segments.append(segment)

    def turn_head(self, velocity):
        self._segments[0].set_velocity(velocity)
    
    def _prepare_body(self):
        if self.player == 1:
            x = int(constants.MAX_X / 3)
            y = int(constants.MAX_Y / 2)
        elif self.player == 2:
            x = int(constants.MAX_X / 3 * 2)
            y = int(constants.MAX_Y / 2)

        for i in range(constants.tron_LENGTH):
            position = Point(x - i * constants.CELL_SIZE, y)
            velocity = Point(1 * constants.CELL_SIZE, 0)
            text = "8" if i == 0 else "#"
            color = constants.YELLOW
            
            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text(text)
            segment.set_color(color)
            self._segments.append(segment)