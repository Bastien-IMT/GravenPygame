import pygame


class Projectile(pygame.sprite.Sprite):

    def __init__(self, player, screen):
        super().__init__()
        self.velocity = 7
        self.player = player
        self.screen = screen
        self.image = pygame.image.load('assets/projectile.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 120
        self.rect.y = player.rect.y + 80
        self.origin_image = self.image
        self.angle = 0

    def rotate(self):
        # make projectile rotate
        self.angle += 12
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)

    def remove(self):
        # remove projectile from group
        self.player.all_projectiles.remove(self)
        self.player.nbProjectiles -= 1

    def move(self):
        # move projectile
        self.rect.x += self.velocity
        self.rotate()
        # if projectile out of screen
        if self.rect.x > self.screen.get_width() or self.rect.x < 0:
            # delete it
            self.remove()
