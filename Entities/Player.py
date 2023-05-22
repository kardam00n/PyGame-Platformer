import pygame.key
import time

from Display import Block, Coin, Arrows

class Player():
    def __init__(self, x, y):
        self.v_y = 0
        self.v_x = 0
        self.completed = False
        self.img = pygame.image.load('assets/Adventurer Sprite Sheet v1.5.png').convert_alpha()
        # wczytywanie animacji
        self.step_ani = []
        for i in range(8):
            self.step_ani.append(self.getimg(i, 1,32, 32))
        self.stand_ani = []
        for i in range(13):
            self.stand_ani.append(self.getimg(i, 0, 32, 32))
        self.image = self.stand_ani[0]
        self.jump_ani = []
        for i in range(6):
            self.jump_ani.append(self.getimg(i, 5, 32, 32))
        self.mlee_ani = []
        for i in range(8):
            self.mlee_ani.append(self.getimg(i, 2, 32, 32))
        self.arrow_ani=[]
        for i in range(3):
            self.arrow_ani.append(self.getimg(i, 9, 32, 32))
        self.arrow_ani.append(self.getimg(6,9,32,32))
        #
        self.rect = self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.points = 0
        self.jump=False
        self.in_air=True
        self.stand=0
        self.step=0
        self.air_time = 0
        self.mlee_time = 0
        self.mlee_attack = False
        self.left_side=False
        self.attack = 10
        self.maxHealth = 200
        self.health=self.maxHealth
        self.iFrameTime = 0
        self.pop_x = 0
        self.arrow_attack=False
        self.arrow_attack_time_z=0
        self.arrow_attack_time_x=0
        self.arrow_attack_time_c=0
    def getimg(self, col, row, width, height):
        image = pygame.Surface((width, height))
        image.blit(self.img, (0, 0), ((col * width), (row*height), width, height))
        image.set_colorkey((0,0,0))

        image = pygame.transform.scale(image, (50, 50))
        return image

    def update(self, map):
        blocks = map.blocks
        enemies = map.enemies
        finish = map.finish
        # movement
        dx=0
        dy=0
        key=pygame.key.get_pressed()
        # idle animation
        self.stand += 1
        if self.stand > 12:
            self.stand = 0
        self.image = self.stand_ani[self.stand]


        if key[pygame.K_SPACE] and not self.jump and not self.in_air:
            self.jump=True
            self.v_y=-25
        if not key[pygame.K_SPACE]:
            self.jump=False
        if key[pygame.K_a]:
            dx-=10
            self.step+=1
            if self.step>7:
                self.step=0
            self.image = pygame.transform.flip(self.step_ani[self.step], True, False)
            self.left_side = True
        if key[pygame.K_d]:
            dx+=10
            self.step += 1
            if self.step > 7:
                self.step = 0
            self.image = self.step_ani[self.step]
            self.left_side=False
        if key[pygame.K_q]:
            self.mlee_attack = True
            self.mlee_time=0
        # if key[]
        # grawitacja
        if self.v_y<=20:
            self.v_y+=2
        dy+=self.v_y

        # interakcja z blokami
        self.in_air=True
        touch_x = False
        touch_y = False
        #dotarcie do mety
        if finish.rect.colliderect(self.rect.x + dx, self.rect.y, self.rect.width, self.rect.height):
            self.completed = True
        for block in blocks:
            if block.rect.colliderect(self.rect.x + dx, self.rect.y, self.rect.width, self.rect.height):
                dx=0
                touch_x = True
            if block.rect.colliderect(self.rect.x + dx - 15*(self.left_side), self.rect.y, self.rect.width+15*(not self.left_side), self.rect.height):
                    if(self.mlee_attack and block.breakBlock()):
                        map.blocks.remove(block)
            if block.rect.colliderect(self.rect.x, self.rect.y + dy, self.rect.width, self.rect.height):
                if self.v_y<0:
                    dy = block.rect.bottom - self.rect.top
                    self.v_y=0
                else:
                    dy = block.rect.top - self.rect.bottom
                    if not touch_x:
                        dx = block.slow(dx, self.pop_x)
                    self.health-=block.hit()
                    self.v_y = 0
                    if not touch_y:
                        if (self.jump):
                            self.v_y-=2*block.bounce()
                        else:
                            self.v_y-=block.bounce()
                    self.in_air=False
        if self.in_air:
            if self.air_time < 4:
                self.air_time+=1
            if self.left_side:
                self.image = pygame.transform.flip(self.jump_ani[self.air_time], True, False)
            else:
                self.image = self.jump_ani[self.air_time]
        else:
            self.air_time = 0
        # atak
        if self.mlee_time>=0:
            self.image = self.mlee_ani[self.mlee_time]
            if self.left_side:
                self.image = pygame.transform.flip(self.mlee_ani[self.mlee_time], True, False)
            self.mlee_time+=1
            if self.mlee_time == 8:
                self.mlee_time=-1
                self.mlee_attack=False
        # interakcja z wrogami
        dt = time.time()*1000 - self.iFrameTime
        for en in enemies:
            if en.rect.colliderect(self.rect.x + dx, self.rect.y+dy, self.rect.width, self.rect.height):
                if self.mlee_attack:
                    if (self.left_side and self.rect.x>en.rect.x) or (not self.left_side and self.rect.x<en.rect.x):
                        en.takeDmg(self.attack)
                        # en.rect.x += 10 * (-1 if self.left_side else 1)
                        if en.health <= 0:
                            enemies.remove(en)
                        self.points+=10
                        continue
                elif dt > 1000 or self.iFrameTime == 0:
                    dy-=10
                    self.iFrameTime = time.time() * 1000
                    self.health-=en.attack
                    # self.rect.x += 10 * (-1 if en.left else 1) 

        if self. rect.y > map.DISPLAY_H:
            self.health -= 10

        # strzały klasyczna
        if key[pygame.K_z] and self.arrow_attack_time_z<8:
            if self.left_side:
                self.image = pygame.transform.flip(self.arrow_ani[self.arrow_attack_time_z // 2], True, False)
            else: self.image = self.arrow_ani[self.arrow_attack_time_z // 2]
            self.arrow_attack_time_z+=1

        if (not key[pygame.K_z] and self.arrow_attack_time_z > 0) or self.arrow_attack==8:
            x = pygame.mouse.get_pos()[0] - self.rect.x
            y = pygame.mouse.get_pos()[1] - self.rect.y
            Arrows.Classic(self.rect.x, self.rect.y, True, (x, y), self.arrow_attack_time_z, map)
            self.arrow_attack_time_z = 0

        # penetrating arrow
        if key[pygame.K_x] and self.arrow_attack_time_x<8:
            if self.left_side:
                self.image = pygame.transform.flip(self.arrow_ani[self.arrow_attack_time_x // 2], True, False)
            else: self.image = self.arrow_ani[self.arrow_attack_time_x // 2]
            self.arrow_attack_time_x+=1

        if (not key[pygame.K_x] and self.arrow_attack_time_x > 0) or self.arrow_attack==8:
            x = pygame.mouse.get_pos()[0] - self.rect.x
            y = pygame.mouse.get_pos()[1] - self.rect.y
            Arrows.Penetrating(self.rect.x, self.rect.y, True, (x, y), self.arrow_attack_time_x, map)
            self.arrow_attack_time_x = 0

        # caboom arrow
        if key[pygame.K_c] and self.arrow_attack_time_c<8:
            if self.left_side:
                self.image = pygame.transform.flip(self.arrow_ani[self.arrow_attack_time_c // 2], True, False)
            else: self.image = self.arrow_ani[self.arrow_attack_time_c // 2]
            self.arrow_attack_time_c+=1

        if (not key[pygame.K_c] and self.arrow_attack_time_c > 0) or self.arrow_attack==8:
            x = pygame.mouse.get_pos()[0] - self.rect.x
            y = pygame.mouse.get_pos()[1] - self.rect.y
            Arrows.Caboom(self.rect.x, self.rect.y, True, (x, y), self.arrow_attack_time_c, map)
            self.arrow_attack_time_c = 0

        self.pop_x = dx
        # odswierzanie pozycji
        self.rect.x += dx
        self.rect.y += dy
        # self.rect.x = max(map.LEFT_BORDER, self.rect.x)
        # self.rect.x = min(self.rect.x, map.RIGHT_BORDER - self.rect.width)
    
    def get_Coin(self, coin: Coin.Coin):
        self.points+=coin.points