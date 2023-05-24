import random

from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import CASPER

class Casper(Obstacle):
    def __init__(self, images, Y):
        self.step_index = 0
        self.type = random.randint(0, 1)
        super().__init__(images, self.type)

        self.rect.y = Y

    """
    def fly(self):
        self.image = CASPER[0] if self.step_index < 35 else CASPER[1]
        self.dino_rect = self.image.get_rect()
        self.step_index += 1

        if self.step_index >=40:
            self.step_index = 0

    def update(self, game_speed, obstacles):
        self.fly()
        super().update(game_speed, obstacles)

    """
