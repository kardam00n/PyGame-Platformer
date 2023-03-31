import pygame
class Box:
    def __init__(self, x, y):
        img = pygame.image.load('assets/pav-creations-platforms-stage-2.png')
        self.image = pygame.transform.scale(img, (50,50))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y