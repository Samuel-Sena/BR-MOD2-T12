import pygame
import random
import os

# Global Constants
TITLE = "Dino Runner"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
FONT_STYLE = "freesansbold.ttf"
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

COLORS = {
    'white': (255,255,255),
    'black': (0,0,0),
    'gray': (200, 200, 200),
    'green': (0, 255, 0)
}

MOOD_Y_POS = 325
LARGE_CACTUS_Y_POS = 300
CASPER_Y_POS = 250
CASPER_Y_POS2 = 200

DEFAULT_TYPE = "default"
SHIELD_TYPE = "shield"

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "DinoWallpaper.png"))

RUNNING = [
    pygame.image.load(os.path.join(IMG_DIR, "Cube/cube.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cube/cube2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cube/cube3.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cube/cube4.png")),
]

RUNNING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Cube/cube.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cube/cube.png")),
]

RUNNING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Cube/cube.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cube/cube.png")),
]

JUMPING = pygame.image.load(os.path.join(IMG_DIR, "Cube/cube.png"))
JUMPING_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Cube/cube.png"))
JUMPING_HAMMER = pygame.image.load(os.path.join(IMG_DIR, "Cube/cube.png"))

DUCKING = [
    pygame.image.load(os.path.join(IMG_DIR, "Cube/cube.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cube/cube.png")),
]

DUCKING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Cube/cube.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cube/cube.png")),
]

DUCKING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Cube/cube.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cube/cube.png")),
]

MOOD = [
    pygame.image.load(os.path.join(IMG_DIR, "Mood/mood.png")),
]

CASPER = [
    pygame.image.load(os.path.join(IMG_DIR, "Casper/casper.png")),
]

CLOUD = pygame.image.load(os.path.join(IMG_DIR, 'Other/Cloud.png'))
SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))
HAMMER = pygame.image.load(os.path.join(IMG_DIR, 'Other/hammer.png'))

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Background2.png'))

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))

DEFAULT_TYPE = "default"
