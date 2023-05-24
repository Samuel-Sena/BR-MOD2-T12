import random

from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import MOOD

class Mood(Obstacle):
    def __init__(self, images, Y):
        self.step_index = 0
        self.type = random.randint(0, 2)
        super().__init__(images, self.type)

        self.rect.y = Y