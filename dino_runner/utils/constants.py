import pygame
import os

TITLE = "Geometry Dash"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
FONT_STYLE = "pusab.tiff"

IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")
MUSIC_DIR = os.path.join(os.path.dirname(__file__), "..", "assets/Other/april_in_summer.mp3")

SMALL_CACTUS_Y_POS = 300

LARGE_CACTUS_Y_POS = 300

BIRD_Y_POS = 250

DEFAULT_TYPE = "default"
SHIELD_TYPE = "shield"
HAMMER_TYPE = "hammer"

ICON = pygame.image.load(os.path.join(IMG_DIR, "DinoWallpaper.png"))

RUNNING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/cube.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/cube.png")),
]

RUNNING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/cube_blue.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/cube_blue.png")),
]

RUNNING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/cube_red.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/cube_red.png")),
]

JUMPING = pygame.image.load(os.path.join(IMG_DIR, "Dino/cube.png"))
JUMPING_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Dino/cube_blue.png"))
JUMPING_HAMMER = pygame.image.load(os.path.join(IMG_DIR, "Dino/cube_red.png"))

DUCKING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/cube_duck.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/cube_duck.png")),
]

DUCKING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/cube_blue_duck.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/cube_blue_duck.png")),
]

DUCKING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/cube_red_duck.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/cube_red_duck.png")),
]

SMALL_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/tri_evil2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/tri_evil2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/tri_evil2.png")),
]
LARGE_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/tri_evil.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/tri_evil.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/tri_evil.png")),
]

BIRD = [
    pygame.image.load(os.path.join(IMG_DIR, "Bird/blue.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/blue.png")),
]

CLOUD = pygame.image.load(os.path.join(IMG_DIR, 'Other/Cloud.png'))
SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))
HAMMER = pygame.image.load(os.path.join(IMG_DIR, 'Other/hammer.png'))

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Background.png'))

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))

DEFAULT_TYPE = "default"
