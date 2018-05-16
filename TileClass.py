import pygame
import sys


# tile class
class Tile(pygame.sprite.Sprite):
    def __init__(self, x, y, color, height, imgHeight):
        pygame.sprite.Sprite.__init__(self)
        self.sideLen = height / imgHeight
        self.image = pygame.Surface((self.sideLen, self.sideLen))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.left = self.sideLen * x
        self.rect.bottom = self.sideLen * y + self.sideLen