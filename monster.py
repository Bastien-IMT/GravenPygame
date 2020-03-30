import pygame
from random import randint


class Monster(pygame.sprite.Sprite):

    def __init__(self, game, screen):
        super().__init__()
        self.game = game
        self.screen = screen
        self.health = 100
        self.max_health = 100
        self.attack = 5
        self.image = pygame.image.load("assets/mummy.png")
        self.rect = self.image.get_rect()
        self.rect.x = self.screen.get_rect().size[0] - self.image.get_rect().size[0]
        self.rect.y = 530
        print(self.rect)
        self.velocity = randint(1, 3)

    def forward(self):
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
