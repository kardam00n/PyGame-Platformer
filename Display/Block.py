import pygame
class Block:
    def __init__(self, x, y, img):
        self.image = pygame.transform.scale(img, (50,50))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def slow(self, dx, pop):
        return dx
    def hit(self):
        return 0
    def bounce(self):
        return 0
    def breakBlock(self):
        return False

class Grass(Block):
    def __init__(self, x, y):
        img = pygame.image.load('assets/pav-creations-platforms-stage-2.png')
        super().__init__(x,y, img)

class Ice(Block):
    def __init__(self, x, y):
        img = pygame.image.load('assets/ice.png')
        super().__init__(x,y,img)
    def slow(self, dx, pop):
        return 0.05 * dx + 0.95 * pop
    
class Mud(Block):
    def __init__(self, x, y):
        img = pygame.image.load('assets/mud.png')
        super().__init__(x,y,img)
    def slow(self, dx, pop):
        return 0.3 * dx
    
class Lava(Block):
    def __init__(self, x, y):
        img = pygame.image.load('assets/lava.png')
        super().__init__(x, y, img)
    def slow(self, dx, pop):
        return 0.6 * dx
    def hit(self):
        return 50
    
class Trampoline(Block):
    def __init__(self,x,y):
        img = pygame.image.load('assets/trampoline.png')
        super().__init__(x,y,img)
    def bounce(self):
        return 20

class Crate(Block):
    def __init__(self,x,y):
        img = pygame.image.load('assets/crate.png')
        super().__init__(x,y,img)
    def breakBlock(self):
        return True

class Finish(Block):
    def __init__(self, x, y):
        img = pygame.image.load('assets/finish.png')
        super().__init__(x,y, img)
