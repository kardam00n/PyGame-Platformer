import pygame



class Arrow:
    def __init__(self, x, y, friendly, v_x, v_y, img, attack):
        self.friendly = friendly
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.v_x = v_x
        self.v_y = v_y
        self.attack = attack
    def update(self, map):
        pass
class Classic(Arrow):
    def __init__(self, x, y, friendly, pos, time, map):
        img = pygame.image.load('assets/arrows1.png').convert_alpha()
        image = pygame.Surface((32, 32))
        image.blit(img, (0, 0), (0, 0, 32, 32))
        image.set_colorkey((255, 255, 255))
        image = pygame.transform.scale(image, (32, 32))
        v = (pos[0]**2 + (pos[1])**2)**0.5
        if v==0: v+=0.00001
        v_x = (pos[0]/v)*time*5
        v_y = (pos[1]/v)*time*5
        super().__init__(x,y,friendly, v_x, v_y, image, 15)
        map.arrows.append(self)
    def update(self, map):
        self.rect.x += self.v_x
        self.rect.y += self.v_y
        self.v_y += 1
        alive = True
        for block in map.blocks:
            if block.rect.colliderect(self.rect.x, self.rect.y, 50, 20):
                map.arrows.remove(self)
                alive=False
                break
        if alive:
            if self.friendly:
                for en in map.enemies:
                    if en.rect.colliderect(self.rect.x, self.rect.y, 50, 20):
                        en.takeDmg(self.attack)
                        if en.health<=0:
                            map.enemies.remove(en)
                            map.player.points += 10
                        map.arrows.remove(self)
                        alive=False
                        break
            else:
                if map.player.rect.colliderect(self.rect.x, self.rect.y, 50, 20):
                    map.player.health-=self.attack
                    map.arrows.remove(self)
                    alive = False
            map.win.blit(self.image, (self.rect.x - map.camera.offset.x, self.rect.y - map.camera.offset.y))
class Penetrating(Arrow):
    def __init__(self, x, y, friendly, pos, time, map):
        img = pygame.image.load('assets/arrows1.png').convert_alpha()
        image = pygame.Surface((32, 32))
        image.blit(img, (0, 0), (0, 32, 32, 32))
        image.set_colorkey((255, 255, 255))
        image = pygame.transform.scale(image, (32, 32))
        v = (pos[0] ** 2 + (pos[1]) ** 2) ** 0.5
        if v == 0: v += 0.00001
        v_x = (pos[0] / v) * time * 5
        v_y = (pos[1] / v) * time * 5
        super().__init__(x, y, friendly, v_x, v_y, image, 10)
        map.arrows.append(self)
    def update(self, map):
        self.rect.x += self.v_x
        self.rect.y += self.v_y
        self.v_y += 1
        alive = True
        if alive:
            if self.friendly:
                for en in map.enemies:
                    if en.rect.colliderect(self.rect.x, self.rect.y, 50, 20):
                        en.takeDmg(self.attack)
                        if en.health<=0:
                            map.enemies.remove(en)
                            map.player.points += 10
                        map.arrows.remove(self)
                        alive=False
                        break
            else:
                if map.player.rect.colliderect(self.rect.x, self.rect.y, 50, 20):
                    map.player.health-=self.attack
                    map.arrows.remove(self)
                    alive = False
            map.win.blit(self.image, (self.rect.x - map.camera.offset.x, self.rect.y - map.camera.offset.y))
class Caboom(Arrow):
    def __init__(self, x, y, friendly, pos, time, map):
        img = pygame.image.load('assets/arrows1.png').convert_alpha()
        image = pygame.Surface((32, 32))
        image.blit(img, (0, 0), (0, 0, 32, 32))
        image.set_colorkey((255, 255, 255))
        image = pygame.transform.scale(image, (32, 32))
        v = (pos[0]**2 + (pos[1])**2)**0.5
        if v==0: v+=0.00001
        v_x = (pos[0]/v)*time*5
        v_y = (pos[1]/v)*time*5
        super().__init__(x,y,friendly, v_x, v_y, image, 5)
        map.arrows.append(self)
    def update(self, map):
        self.rect.x += self.v_x
        self.rect.y += self.v_y
        self.v_y += 1
        alive = True
        for block in map.blocks:
            if block.rect.colliderect(self.rect.x, self.rect.y, 50, 20):
                if self.friendly:
                    for en in map.enemies:
                        if ((self.rect.x-en.rect.x)**2+(self.rect.y-en.rect.y)**2)<50000:
                            en.takeDmg(self.attack)
                            if en.health <= 0:
                                map.enemies.remove(en)
                                map.player.points += 10
                else:
                    if ((self.rect.x-map.player.rect.x)**2+(self.rect.y-map.player.rect.y)**2)<50000:
                        map.player.health-=self.attack
                map.arrows.remove(self)
                alive=False
                break
        map.win.blit(self.image, (self.rect.x - map.camera.offset.x, self.rect.y - map.camera.offset.y))