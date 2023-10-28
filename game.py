import pygame
import random
import sys
from background import *
from game_parameters import *
from car import *

# Initialize pygame
pygame.init()

# Create Screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Stuff and things!")

# Initialize Cars
for _ in range(2):
    cars.add(Car(random.randint(SCREEN_WIDTH, SCREEN_WIDTH * 1.5), 0))

# Clock object
clock = pygame.time.Clock()

# Main Loop
running = True
background = screen.copy()
draw_background(background)

while running:
    # Close Game
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            running = False

    # Draw the fish
    # cars.draw(screen)

    # Update the cars on the road
    # cars.update()

    # Draw Background
    screen.blit(background, (0, 0))

    # Update the display
    pygame.display.flip()

    # Limit Frame Rate
    clock.tick(60)

pygame.quit()
