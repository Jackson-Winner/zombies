import pygame
from game_parameters import *
from player import player


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("../zombies/assets/sprites/zombie.png")
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.X_CHANGE = 0
        self.Y_CHANGE = 0

    def update(self):

        if self.x > player.player_x:
            self.X_CHANGE = -random.uniform(ZOMBIE_MIN_SPEED, ZOMBIE_MAX_SPEED)
        elif self.x < player.player_x:
            self.X_CHANGE = random.uniform(ZOMBIE_MIN_SPEED, ZOMBIE_MAX_SPEED)
        else:
            self.X_CHANGE = 0

        if self.y > player.player_y:
            self.Y_CHANGE = -random.uniform(ZOMBIE_MIN_SPEED, ZOMBIE_MAX_SPEED)
        elif self.y < player.player_y:
            self.Y_CHANGE = random.uniform(ZOMBIE_MIN_SPEED, ZOMBIE_MAX_SPEED)
        else:
            self.Y_CHANGE = 0

        self.x += self.X_CHANGE
        self.y += self.Y_CHANGE
        self.rect.x = self.x
        self.rect.y = self.y

    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))


# Create a sprite group for the zombies
enemies = pygame.sprite.Group()


# This creates a function so that you can choose how many enemies spawn at once and in total
def add_enemies(total, amount):

    if len(enemies) < total:
        for _ in range(amount):
            random_number = random.randint(0, 1)
            if random_number == 0:
                enemies.add(Enemy(random.randint(GRASS_TILE_SIZE, SCREEN_WIDTH - 2 * GRASS_TILE_SIZE), -ROAD_TILE_SIZE))
            elif random_number == 1:
                enemies.add(Enemy(random.randint(GRASS_TILE_SIZE, SCREEN_WIDTH - 2 *
                                                 GRASS_TILE_SIZE), SCREEN_HEIGHT))


class Delay:

    def __init__(self, wait=500):
        self.last = pygame.time.get_ticks()
        self.wait = wait

    def spawn(self, total, amount):
        # Spawn zombie only after 1 second
        now = pygame.time.get_ticks()
        if now - self.last >= self.wait:
            self.last = now
            add_enemies(total, amount)


cooldown = Delay(COOLDOWN_TIME)
