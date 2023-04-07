import random

import pygame
class Enemy():
    def __init__(self, x, y):
        self.img = pygame.image.load('assets/NightBorne.png').convert_alpha()
        # wczytywanie animacji
        self.step_ani = []
        for i in range(6):
            self.step_ani.append(self.getimg(i, 0, 80, 80))
        self.image = self.step_ani[0]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.left = False
        self.step = 0
        self.v_y = 0
        self.speed = 4
    def getimg(self, col, row, width, height):
        image = pygame.Surface((width, height))
        image.blit(self.img, (0, 0), ((col * width), (row*height), width, height))
        image.set_colorkey((0,0,0))

        image = pygame.transform.scale(image, (50, 50))
        return image
    def update(self, blocks):
        dx=self.speed
        dy=0
        if self.v_y==0 and random.random()<0.05:
            self.v_y=-20
        # grawitacja
        if self.v_y <= 20:
            self.v_y += 2
        dy += self.v_y
        if self.left:
            dx=-self.speed
        for block in blocks:
            if block.rect.colliderect(self.rect.x + dx, self.rect.y, self.rect.width, self.rect.height):
                dx=0
            if block.rect.colliderect(self.rect.x, self.rect.y + dy, self.rect.width, self.rect.height):
                if self.v_y<0:
                    dy = block.rect.bottom - self.rect.top
                    self.v_y=0
                else:
                    dy = block.rect.top - self.rect.bottom
                    # self.in_air=False
                    self.v_y=0
        if dx==0:
            dx=-self.speed
            if self.left:
                dx=self.speed
        for block in blocks:
            if block.rect.colliderect(self.rect.x + dx, self.rect.y, self.rect.width, self.rect.height):
                dx = 0
        if dx>=0:
            self.left=False
        else: self.left = True
        self.rect.x+=dx
        self.rect.y+=dy
        if self.step>5:
            self.step=0
        if self.left:
            self.image = pygame.transform.flip(self.step_ani[self.step], True, False)
        else: self.image = self.step_ani[self.step]
