import pygame.key

import Box
import Find
class Player():
    def __init__(self, x, y):
        self.v_y = 0
        self.v_x = 0
        img = pygame.image.load('assets/player-right.png')
        self.image = pygame.transform.scale(img, (50,50))
        self.rect = self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.points = 0
        self.jump=False
        self.in_air=True
    def update(self, blocks):
        # movement
        dx=0
        dy=0
        key=pygame.key.get_pressed()
        if key[pygame.K_SPACE] and not self.jump and not self.in_air:
            self.jump=True
            self.v_y=-25
        if not key[pygame.K_SPACE]:
            self.jump=False
        if key[pygame.K_LEFT]:
            dx-=10
            self.image = pygame.transform.scale(pygame.image.load('assets/player-left.png'), (50,50))
        if key[pygame.K_RIGHT]:
            dx+=10
            self.image = pygame.transform.scale(pygame.image.load('assets/player-right.png'), (50,50))

        # grawitacja
        if self.v_y<=20:
            self.v_y+=2
        dy+=self.v_y


        # interakcja z blokami
        self.in_air=True
        for block in blocks:
            if block.rect.colliderect(self.rect.x + dx, self.rect.y, self.rect.width, self.rect.height):
                dx=0
            if block.rect.colliderect(self.rect.x, self.rect.y + dy, self.rect.width, self.rect.height):
                if self.v_y<0:
                    dy = block.rect.bottom - self.rect.top
                    self.v_y=0
                else:
                    dy = block.rect.top - self.rect.bottom
                    self.in_air=False
                    self.v_y=0
        self.rect.x += dx
        self.rect.y += dy
    def get_Find(self, find: Find.Find):
        self.points+=find.points
