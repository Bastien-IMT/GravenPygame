from player import Player
from monster import Monster
import pygame


class Game:
    def __init__(self, screen):
        self.screen = screen
        self.all_players = pygame.sprite.Group()
        self.player = Player(screen, self)
        self.all_players.add(self.player)
        self.all_monsters = pygame.sprite.Group()
        self.pressed = {}
        self.spawn_monster()

    def spawn_monster(self):
        self.all_monsters.add(Monster(self, self.screen))

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, dokill=False, collided=pygame.sprite.collide_mask)
