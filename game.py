from player import Player
from monster import Monster
import pygame


class Game:
    def __init__(self, screen):
        self.player = Player(screen)
        self.all_monster = pygame.sprite.Group()
        self.pressed = {}
        self.spawn_monster()

    def spawn_monster(self):
        self.all_monster.add(Monster())
