import pygame
import sys


# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self, W, H):
        pygame.sprite.Sprite.__init__(self)
        self.W = W
        self.H = H
        self.image = pygame.Surface((50, 50))
        self.image.fill((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.centerx = self.W / 2
        self.rect.bottom = self.H - 20
        self.speedx = 0
        self.speedy = 0
        self.yvelocity = 0

    def update(self):
        self.updatexmovement()
        self.fall()

        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_UP] and self.rect.bottom == self.H - 20:
            self.jump()

    def updatexmovement(self):
        self.speedx = 0

        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_RIGHT]:
            self.speedx += 10
        if keystate[pygame.K_LEFT]:
            self.speedx -= 10

        self.rect.x += self.speedx

        if self.rect.right > self.W:
            self.rect.right = self.W
        if self.rect.left < 0:
            self.rect.left = 0

    def jump(self):
        self.yvelocity = -32

    def fall(self):
        if self.rect.bottom != 0:
            self.rect.y += self.yvelocity
        if self.rect.bottom < self.H - 20:
            self.yvelocity += 4
        if self.rect.bottom > self.H - 20:
            self.rect.bottom = self.H - 20
            self.yvelocity = 0