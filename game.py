import pygame
import random
import sys

from background import *
from player import *
from enemy import *
from bomb import *

# Initialize pygame
pygame.init()

# Create Screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("RUN!")
start_font = pygame.font.Font("assets/fonts/Carnevalee_Freakshow.ttf", 64)
instructions_font = pygame.font.Font("assets/fonts/Carnevalee_Freakshow.ttf", 32)
game_over_font = pygame.font.Font("assets/fonts/Carnevalee_Freakshow.ttf", 40)

# Clock objects
clock = pygame.time.Clock()

# Main Loop
running = True
background = screen.copy()
draw_background(background)

# Create Player stuff
health = 3
score = 0
highscore = 0

while running:

    # Start Menu
    start = True
    while start:

        # Display Title and start instructions
        screen.fill((0, 0, 0))
        message = start_font.render("ZOMBIE RUN!", True, (255, 0, 0))
        screen.blit(message, (SCREEN_WIDTH / 2 - message.get_width() / 2, SCREEN_HEIGHT / 2 - message.get_height() / 2))
        instructions = instructions_font.render("Press WASD to move and ENTER to start", True, (255, 0, 0))
        screen.blit(instructions, (SCREEN_WIDTH / 2 - instructions.get_width() / 2, (SCREEN_HEIGHT / 2 - instructions.get_height() / 2) + message.get_height()))
        screen.blit(start_screen_zombie, (SCREEN_WIDTH/2 - start_screen_zombie.get_width()/2, 20))

        # Flip the display
        pygame.display.flip()

        # Quit game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                start = False
                pygame.quit()
                sys.exit()

        # Start Game and change modifiers
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_RETURN]:
            start_time = pygame.time.get_ticks()
            start = False

    # Logic for when the player is alive
    while health > 0:
        # Close Game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Draw Background
        screen.blit(background, (0, 0))

        # Draw Bomb
        spawn_nuke()

        # Explode bomb if collided
        if nukes:
            nukes.draw(screen)
            result_bomb = pygame.sprite.spritecollide(player, nukes, True)
            if result_bomb:
                enemies.empty()
                nukes.empty()

        # Show the score
        score_timer = pygame.time.get_ticks() - start_time
        if score_timer % 10 == 0:
            score += 1
        if score > highscore:
            highscore = score

        score_text = game_over_font.render(f"Score: {score}", True, (255, 0, 0))
        screen.blit(score_text, (SCREEN_WIDTH - GRASS_TILE_SIZE - score_text.get_width(), ROAD_TILE_SIZE))
        highscore_text = game_over_font.render(f"Highscore: {highscore}", True, (255, 0, 0))
        screen.blit(highscore_text, (GRASS_TILE_SIZE, ROAD_TILE_SIZE))

        # Draw health icons
        for i in range(health):
            screen.blit(life_icon, ((i * GRASS_TILE_SIZE) + GRASS_TILE_SIZE, SCREEN_HEIGHT - 2*ROAD_TILE_SIZE))

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
                pygame.quit()
                sys.exit()

        # Set screen to black
        screen.fill((0, 0, 0))

        # Display the game over text
        message_game_over = game_over_font.render("GAME OVER!", True, (255, 0, 0))
        screen.blit(message_game_over, (SCREEN_WIDTH / 2 - message_game_over.get_width() / 2, SCREEN_HEIGHT / 2 - message_game_over.get_height() / 2))
        instructions = instructions_font.render("Press ENTER to restart", True, (255, 0, 0))
        screen.blit(instructions, (SCREEN_WIDTH / 2 - instructions.get_width() / 2,
                                   (SCREEN_HEIGHT / 2 - instructions.get_height() / 2) + message_game_over.get_height()))

        # Restart the Game
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_RETURN]:
            health = 3
            score = 0
            player.player_x = SCREEN_WIDTH/2
            player.player_y = SCREEN_HEIGHT/2
            enemies.empty()
            nukes.empty()
            dead = False

        # Flip the Display
        pygame.display.flip()

pygame.quit()
