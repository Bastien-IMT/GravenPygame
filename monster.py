import pygame
from random import randint


class Monster(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.health = 100
        self.max_health = 100
        self.attack = 5
        self.image = pygame.image.load("assets/mummy.png")
        self.rect = self.image.get_rect()
        self.rect.x = 970
        self.rect.y = 540
        self.velocity = randint(1, 3)

    def forward(self):
        self.rect.x -= self.velocity
