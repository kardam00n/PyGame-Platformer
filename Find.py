import pygame
class Find:
    def __init__(self, x, y):
        self.points=5
        img = pygame.image.load('assets/png-clipart-platinum-design-bitcoin-bitcoin-platinum-coins-thumbnail.png')
        self.image = pygame.transform.scale(img, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y