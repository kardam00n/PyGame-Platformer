import pygame

from Entities import Player, enemy
from Display import Block, Camera, Coin
from Levels import MapParser

class Map:
    def __init__(self, win):
        self.win = win

        self.DISPLAY_W = 800
        self.DISPLAY_H = 600
        self.LEFT_BORDER = 0
        self.RIGHT_BORDER = 2400


        

        self.player = Player.Player(0,0)
        self.finish = Block.Finish(self.DISPLAY_W, 0)
        self.blocks = []
        self.coins = []
        self.enemies = []
        self.arrows = []
        MapParser.parseLvl("Levels/lvl1.txt", self)
        self.camera = Camera.Camera(self.player, self)


    def render(self):
        for coin in self.coins:
            self.win.blit(coin.image, (coin.rect.x - self.camera.offset.x, coin.rect.y - self.camera.offset.y))
        for block in self.blocks:
            self.win.blit(block.image, (block.rect.x - self.camera.offset.x, block.rect.y - self.camera.offset.y))
        for en in self.enemies:
            en.renderEnemy(self.win, self.camera)
        
        self.win.blit(self.player.image, (self.player.rect.x-self.camera.offset.x, self.player.rect.y-self.camera.offset.y))
        self.win.blit(self.finish.image, (self.finish.rect.x-self.camera.offset.x, self.finish.rect.y-self.camera.offset.y))
        self.player.update(self)
    
        for en in self.enemies:
            en.update(self)

        for arrow in self.arrows:
            arrow.update(self)
        
        # zbieranie monet
        for coin in self.coins:
            if self.player.rect.colliderect(coin.rect):
                self.player.get_coin(coin)
                self.coins.remove(coin)


    def drawBG(self):
        background = pygame.image.load("assets/Background.png")
        background = pygame.transform.scale(background, (800, 600))
        self.win.blit(background, (0, 0))

    def resetLevel(self):
        self.player = Player.Player(0,0)
        self.finish = Block.Finish(self.DISPLAY_W, 0)
        self.blocks = []
        self.coins = []
        self.enemies = []
        self.arrows = []
        MapParser.parseLvl("Levels/lvl1.txt", self)
        self.camera = Camera.Camera(self.player, self)