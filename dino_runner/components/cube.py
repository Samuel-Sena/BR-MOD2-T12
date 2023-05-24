import pygame 

from dino_runner.utils.constants import RUNNING, JUMPING, DUCKING

X_POS = 80
Y_POS = 330
JUMP_VEL = 8.5

class Cube:
    def __init__(self):
        self.image = RUNNING[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = X_POS
        self.dino_rect.y = Y_POS

        self.dino_vel = JUMP_VEL
        self.dino_run = True 
        self.dino_jump = False
        self.dino_duck = False 
        self.dino_index = 0
        self.step_index = 0
        self.jump_vel = 8.5

    def run(self):
        self.image = RUNNING[0] if self.step_index < 5 else RUNNING[1]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = X_POS
        self.dino_rect.y = Y_POS
        self.step_index += 1
        
        if self.step_index >= 5:
            self.step_index = 0

    def jump(self):
        self.image = JUMPING
        
        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8

        if self.jump_vel < -JUMP_VEL:
            self.dino_jump = False 
            self.dino_rect.y = Y_POS
            self.jump_vel = JUMP_VEL

    def duck(self):
        self.image = DUCKING[0] if self.step_index < 5 else DUCKING[1]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = X_POS
        self.dino_rect.y = Y_POS + 35
        self.step_index += 1

    def update(self, user_input, user_input2):
        if not self.dino_jump:
            self.dino_jump = False
            self.dino_duck = False
            self.dino_run = True

        if user_input[pygame.K_UP] or user_input[pygame.K_w] or user_input[pygame.K_SPACE] and not self.dino_jump:
            self.dino_jump = True
            self.dino_run = False
            self.dino_duck = False
        
        if user_input2[pygame.K_DOWN] or user_input2[pygame.K_s] and not self.dino_jump:
            self.dino_duck = True

        if self.dino_run:
            self.run()

        if self.dino_jump:
            self.jump()

        if self.dino_duck and not self.dino_jump:
            self.duck()

    def draw(self, screen):
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))



        