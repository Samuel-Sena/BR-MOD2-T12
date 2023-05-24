import pygame
import random

from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird

from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD, SMALL_CACTUS_Y_POS, LARGE_CACTUS_Y_POS, BIRD_Y_POS, BIRD_Y_POS2, BIRD_Y_POS3

list_random_obs = [Cactus(SMALL_CACTUS, SMALL_CACTUS_Y_POS),
                   Cactus(LARGE_CACTUS, LARGE_CACTUS_Y_POS),
                   Bird(BIRD, BIRD_Y_POS),
                   Bird(BIRD, BIRD_Y_POS2),
                   Bird(BIRD, BIRD_Y_POS3)]

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
                