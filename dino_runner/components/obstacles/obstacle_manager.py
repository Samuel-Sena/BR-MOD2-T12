import random

from dino_runner.components.obstacles.mood import Mood
from dino_runner.components.obstacles.casper import Casper

from dino_runner.utils.constants import MOOD, MOOD_Y_POS , CASPER, CASPER_Y_POS, CASPER_Y_POS2

list_random_obs = [Mood(MOOD, MOOD_Y_POS),
                   Casper(CASPER, CASPER_Y_POS),
                   Casper(CASPER, CASPER_Y_POS2)]

class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def update(self, game):

        if len(self.obstacles) == 0:
            self.obstacles.append(random.choice(list_random_obs))

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)

            if game.player.dino_rect.colliderect(obstacle.rect):
                game.time.delay(500)
                game.playing = False
                game.death_count += 1
                break

    def draw(self, screen):
        print(self.obstacles)
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacles(self):
        self.obstacles.clear()