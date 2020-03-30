import pygame

from projectile import Projectile


class Player(pygame.sprite.Sprite):
    def __init__(self, screen):
        super().__init__()
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 5
        self.image = pygame.image.load('assets/player.png')
        self.rect = self.image.get_rect()
        self.nbProjectiles = 0
        self.all_projectiles = pygame.sprite.Group()
        self.screen = screen
        self.rect.x = self.screen.get_width() / 2 - 90
        self.rect.y = 500

    def mov_right(self):
        self.rect.x += self.velocity

    def mov_left(self):
        self.rect.x -= self.velocity

    def launch_projectile(self):
        # create instance of 1 projectile and adding it in group
        if self.nbProjectiles < 5:
            self.all_projectiles.add(Projectile(self, self.screen))
            self.nbProjectiles += 1
