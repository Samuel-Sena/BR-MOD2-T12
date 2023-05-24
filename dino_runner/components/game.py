import pygame

from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, COLORS, FONT_STYLE
from dino_runner.components.cube import Cube
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager

FONT_STYLE = 'freesansbold.ttf'
color_black = COLORS['black']
color_white = COLORS['white']
color_gray = COLORS['gray']
color_green = COLORS['green']

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.executing = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 0
        self.player = Cube()
        self.obstacle_manager = ObstacleManager()
        self.death_count = 0
        self.score = 0

    def run(self):
        self.playing = True
        self.reset_game()
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def execute(self):
        self.executing = True
        while self.executing:
            if not self.playing:
                self.show_menu()
        pygame.display.quit()    
        pygame.quit()

    def reset_game(self):
        self.obstacle_manager.reset_obstacles()
        self.game_speed = 20
        self.score = 0

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.executing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        user_input2 = pygame.key.get_pressed()
        self.player.update(user_input, user_input2)
        self.obstacle_manager.update(self)
        self.update_score()

    def update_score(self):
        self.score+=1

        if self.score%150 == 0:
            self.game_speed+=1

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.draw_score()
        pygame.display.update()
        pygame.display.flip()

    def draw_score(self):
        font = pygame.font.Font(FONT_STYLE, 22)
        text = font.render(f"Score: {self.score}", True, (0,0,0))
        text_rect = text.get_rect()
        text_rect.center = (1000, 50)

        self.screen.blit(text, text_rect)

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.fill(color_gray)
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def show_menu(self):
        self.screen.fill((color_gray))

        half_screen_height = SCREEN_HEIGHT //2
        half_screen_width = SCREEN_WIDTH //2

        font = pygame.font.Font(FONT_STYLE, 22)
        text = font.render("Press (Space) to start playing", True, (0,0,0))
        text_rect = text.get_rect()
        text_rect.center = (half_screen_width, half_screen_height)
        self.screen.blit(text, text_rect)

        font = pygame.font.Font(FONT_STYLE, 22)
        text = font.render(f"Score: {self.score}", True, (0,0,0))
        text_rect = text.get_rect()
        text_rect.center = (1000, 50)

        self.screen.blit(text, text_rect)
        pygame.display.update()

        self.handle_events_on_menu()

    def handle_events_on_menu(self):
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                self.playing = False
                self.executing = False
            elif event.type == pygame.KEYDOWN:
                if pygame.key.get_pressed()[pygame.K_SPACE] and self.death_count == 0:
                    self.run()
                elif pygame.key.get_pressed()[pygame.K_SPACE]: 
                    self.run()