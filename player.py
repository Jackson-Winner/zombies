import pygame
from game_parameters import *


# Create class for player
class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        # TODO Flip fish if going other way
        self.image = pygame.image.load("../zombies/assets/sprites/player.png")
        self.rect = self.image.get_rect()
        self.player_x = SCREEN_WIDTH/2
        self.player_y = SCREEN_HEIGHT/2
        self.X_CHANGE = 0
        self.Y_CHANGE = 0
        self.MAX_SPEED = 7

    def move(self):

        keys = pygame.key.get_pressed()

        # Left and right movement
        if keys[pygame.K_a] and not keys[pygame.K_d]:
            self.X_CHANGE = -self.MAX_SPEED
        elif keys[pygame.K_d] and not keys[pygame.K_a]:
            self.X_CHANGE = self.MAX_SPEED
        else:
            self.X_CHANGE = 0

        # Up and down movement
        if keys[pygame.K_w] and not keys[pygame.K_s]:
            self.Y_CHANGE = -self.MAX_SPEED
        elif keys[pygame.K_s] and not keys[pygame.K_w]:
            self.Y_CHANGE = self.MAX_SPEED
        else:
            self.Y_CHANGE = 0

        # Move the player
        self.player_x += self.X_CHANGE
        self.player_y += self.Y_CHANGE

        # Bound the Player to the play area
        if self.player_x >= SCREEN_WIDTH - 2 * GRASS_TILE_SIZE:
            self.player_x = SCREEN_WIDTH - 2 * GRASS_TILE_SIZE
        elif self.player_x < GRASS_TILE_SIZE:
            self.player_x = GRASS_TILE_SIZE

        if self.player_y >= SCREEN_HEIGHT - 2 * ROAD_TILE_SIZE:
            self.player_y = SCREEN_HEIGHT - 2 * ROAD_TILE_SIZE
        elif self.player_y < ROAD_TILE_SIZE:
            self.player_y = ROAD_TILE_SIZE

        self.rect.x = self.player_x
        self.rect.y = self.player_y

    def draw(self, surface):
        surface.blit(self.image, (self.player_x, self.player_y))


# Create an instance of the Player class
player = Player()
