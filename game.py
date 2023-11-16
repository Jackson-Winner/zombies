import pygame
import random
import sys

from background import *
from player import *
from enemy import *

# Initialize pygame
pygame.init()

# Create Screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("RUN!")
start_font = pygame.font.Font("assets/fonts/Carnevalee_Freakshow.ttf", 64)
instructions_font = pygame.font.Font("assets/fonts/Carnevalee_Freakshow.ttf", 32)
game_over_font = pygame.font.Font("assets/fonts/Black_Crayon.ttf", 40)

# Clock objects
clock = pygame.time.Clock()

# Main Loop
running = True
background = screen.copy()
draw_background(background)

# Create Player Health
health = 3

while running:

    # Start Menu
    start = True
    while start:

        # Display Title and start instructions
        message = start_font.render("ZOMBIE RUN!", True, (255, 0, 0))
        screen.blit(message, (SCREEN_WIDTH / 2 - message.get_width() / 2, SCREEN_HEIGHT / 2 - message.get_height() / 2))
        instructions = instructions_font.render("Press ENTER to start", True, (255, 0, 0))
        screen.blit(instructions, (SCREEN_WIDTH / 2 - instructions.get_width() / 2, (SCREEN_HEIGHT / 2 - instructions.get_height() / 2) + message.get_height()))

        # Flip the display
        pygame.display.flip()

        # Quit game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                start = False
                health = 0
                dead = False
                running = False

        # Start Game and change modifiers
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_RETURN]:
            start = False

    # Logic for when the player is alive
    while health > 0:
        # Close Game
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                health = 0
                running = False

        # Draw Background
        screen.blit(background, (0, 0))

        # Add enemies to screen
        cooldown.spawn(TOTAL_ZOMBIES, SPAWN_PER_INSTANCE)

        # Updates the positions of all sprites
        player.move()
        enemies.update()

        # Check for enemy collisions with the player
        result_enemy = pygame.sprite.spritecollide(player, enemies, True)
        if result_enemy:
            health -= 1

        # Draw the Player and the enemies
        player.draw(screen)
        enemies.draw(screen)

        # Update the display
        pygame.display.update()

        # Limit Frame Rate
        clock.tick(60)

    dead = True
    while dead:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                dead = False
                running = False

        # Set screen to black
        screen.fill((0, 0, 0))

        # Display the game over text
        message_game_over = game_over_font.render("GAME OVER!", True, (255, 0, 0))
        screen.blit(message_game_over, (SCREEN_WIDTH / 2 - message_game_over.get_width() / 2, SCREEN_HEIGHT / 2 - message_game_over.get_height() / 2))
        instructions = instructions_font.render("Press ENTER to start", True, (255, 0, 0))
        screen.blit(instructions, (SCREEN_WIDTH / 2 - instructions.get_width() / 2,
                                   (SCREEN_HEIGHT / 2 - instructions.get_height() / 2) + message_game_over.get_height()))

        # Restart the Game
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_RETURN]:
            health = 3
            enemies.remove()
            dead = False

        # Flip the Display
        pygame.display.flip()

pygame.quit()
