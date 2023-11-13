import pygame
import random
from game_parameters import *
from player import *

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.x = random.randint(GRASS_TILE_SIZE, SCREEN_WIDTH-(2*GRASS_TILE_SIZE))
        self.y = y
        self.X_CHANGE = 0
        self.Y_CHANGE = 0
        self.MAX_SPEED = 5

    def move_zombie(self):
        if self.x > Player.player_x:
            self.X_CHANGE += self.MAX_SPEED
        elif self.x < Player.player_x:
            self.X_CHANGE -= self.MAX_SPEED
        else:
            self.X_CHANGE = 0