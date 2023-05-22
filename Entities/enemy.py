import random
import time
import pygame

from Entities import HealthBar
from Display import Arrows

class Enemy():
    def __init__(self, x, y, attack, health,step_ani):
        # wczytywanie animacji
        self.step_ani = step_ani
        self.image = self.step_ani[0]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.left = False
        self.step = 0
        self.v_y = 0
        self.speed = 4
        self.attack = attack
        self.health = health
        self.HealhBar = HealthBar.HealthBar(self.health, self.health)
        self.iFrameTime = 0
    def update(self, map):
        blocks = map.blocks
        distance_to_player=map.player.rect.x-self.rect.x
        if (abs(distance_to_player)<150):
            if (distance_to_player<0):
                self.left=True
            else:
                self.left=False
        else:
            if (random.random()<0.005):
                self.left = not self.left
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
        if dx==0 and not abs(distance_to_player)<150:
            dx=-self.speed
            if self.left:
                dx=self.speed
        for block in blocks:
            if block.rect.colliderect(self.rect.x + dx, self.rect.y, self.rect.width, self.rect.height):
                dx = 0
        if dx>0:
            self.left=False
        else: self.left = True
        self.rect.x+=dx
        self.rect.y+=dy
        if self.step>5:
            self.step=0
        if self.left:
            self.image = pygame.transform.flip(self.step_ani[self.step], True, False)
        else: self.image = self.step_ani[self.step]
        self.step+=1
        self.rect.x = max(map.LEFT_BORDER, self.rect.x)
        self.rect.x = min(self.rect.x, map.RIGHT_BORDER - self.rect.width)
    def renderEnemy(self, win, camera):
        win.blit(self.image, (self.rect.x - camera.offset.x, self.rect.y - camera.offset.y))
        self.HealhBar.render(win,camera, self.rect.x, self.rect.y, self.health)
    def takeDmg(self, dmg):
        dt = time.time() * 1000 - self.iFrameTime
        if dt > 500 or self.iFrameTime == 0:
            self.iFrameTime = time.time() * 1000
            self.health -= dmg
class EnemyMlee(Enemy):
    def __init__(self, x, y):
        img = pygame.image.load('assets/NightBorne.png').convert_alpha()
        step_ani = []
        for i in range(6):
            step_ani.append(self.getimg(i, 0, 80, 80, img))
        super().__init__(x,y, 10, 200, step_ani)
    def getimg(self, col, row, width, height, img):
        image = pygame.Surface((width, height))
        image.blit(img, (0, 0), ((col * width), (row*height), width, height))
        image.set_colorkey((0,0,0))

        image = pygame.transform.scale(image, (80, 80))
        return image
class EnemyArcher(Enemy):
    def __init__(self, x, y):
        step_ani = []
        for i in range(1, 7):
            path = 'assets/Archer/run/Archer_run' + str(i) + '.png'
            img = pygame.image.load(path).convert_alpha()
            image = pygame.transform.scale(img, (80, 80))
            step_ani.append(image)
        super().__init__(x,y,10, 100, step_ani)

    def update(self, map):
        if random.random()<0.05 and abs(map.player.rect.x - self.rect.x)<300:
            Arrows.Classic(self.rect.x, self.rect.y, False, (map.player.rect.x - self.rect.x, map.player.rect.y - self.rect.y), 5, map)
        super().update(map)
       
