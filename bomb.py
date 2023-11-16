import random
from game_parameters import SCREEN_WIDTH, SCREEN_HEIGHT, GRASS_TILE_SIZE, ROAD_TILE_SIZE, CHANCE_BOMB_SPAWN
import pygame
from enemy import enemies

bomb_image = pygame.image.load("assets/sprites/bomb.png")

class Bomb(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("assets/sprites/bomb.png")
        self.image.set_colorkey((255, 255, 255))
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()

    def draw(self, surface):
        self.rect.x = self.x
        self.rect.y = self.y
        surface.blit(self.image, (self.rect.x, self.rect.y))


nukes = pygame.sprite.Group()


def spawn_nuke():
    bomb_spawn = random.randint(0, CHANCE_BOMB_SPAWN)
    if bomb_spawn == CHANCE_BOMB_SPAWN and len(nukes) != 1:
        nukes.add(Bomb(SCREEN_WIDTH/2 - bomb_image.get_width(), SCREEN_HEIGHT/2 - bomb_image.get_height()))
