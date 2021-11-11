from game.action import Action
from random import randint
from game.point import Point
from game import constants

class Change(Action):
    def execute(self, cast):
        if randint(0,50) != 50:
            return
        for artifact in cast["artifact"]:
            x = randint(0, constants.MAX_X - 1)
            y = randint(1, constants.MAX_Y - 1)
            position = Point(x, y)
            artifact.set_position(position)