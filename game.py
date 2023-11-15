import pygame
import random
import sys

from pygame import Surface, SurfaceType

from background import *
from game_parameters import *
from player import *
from enemy import *

# Initialize pygame
pygame.init()

# Create Screen
screen: Surface | SurfaceType = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("RUN!")

# Clock objects
clock = pygame.time.Clock()

# Create the Player
#player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

#enemy = Enemy(random.randint(GRASS_TILE_SIZE,SCREEN_WIDTH-2*GRASS_TILE_SIZE), ROAD_TILE_SIZE)

# Main Loop
running = True
background = screen.copy()
draw_background(background)

while running:
    # Close Game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw Background
    screen.blit(background, (0, 0))

    player.move()
    enemies.move_zombie()

    # Draw the Player
    player.draw(screen)
    enemies.draw(screen)

    # Update the display
    pygame.display.update()

    # Limit Frame Rate
    clock.tick(60)

pygame.quit()
