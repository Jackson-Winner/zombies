import pygame
import random
from game_parameters import *
from player import player

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("../zombies/assets/sprites/zombie.png")
        self.x = x
        self.y = y
        self.X_CHANGE = 0
        self.Y_CHANGE = 0
        self.MAX_SPEED = 3


    def move_zombie(self):
        if self.x > player.player_x:
            self.X_CHANGE = -self.MAX_SPEED
        elif self.x < player.player_x:
            self.X_CHANGE = self.MAX_SPEED
        else:
            self.X_CHANGE = 0

        if self.y > player.player_y:
            self.Y_CHANGE = -self.MAX_SPEED
        elif self.y < player.player_y:
            self.Y_CHANGE = self.MAX_SPEED
        else:
            self.Y_CHANGE = 0

        self.x += self.X_CHANGE
        self.y += self.Y_CHANGE

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))

enemies = pygame.sprite.Group

for _ in range(5):
    enemies.add(Enemy(random.randint(GRASS_TILE_SIZE,SCREEN_WIDTH-2*GRASS_TILE_SIZE), ROAD_TILE_SIZE))
#enemy = Enemy(random.randint(GRASS_TILE_SIZE,SCREEN_WIDTH-2*GRASS_TILE_SIZE), ROAD_TILE_SIZE)
