import pygame
import Entities.Player as Player
import Display.Box as Box
import Display.Coin as Coin
import Display.Camera as Camera
import Entities.enemy as enemy

class Map:
    def __init__(self, win):
        
        self.player = Player.Player(50,400)
        self.enemies = [enemy.Enemy(340, 200)]
        self.coins = [Coin.Coin(40, 450), Coin.Coin(150, 450), Coin.Coin(260, 450), Coin.Coin(300, 400)]
        self.blocks = [Box.Box(0+50*i, y) for i in range(48) for y in (500,550)]
        self.blocks.append(Box.Box(300, 450))
        self.blocks.append(Box.Box(250, 350))
        self.blocks.append(Box.Box(500, 450))
        for i in range(-100,500, 50):
            self.blocks.append(Box.Box(-50, i))
            self.blocks.append(Box.Box(2400, i))

        self.camera = Camera.Camera(self.player)
        self.win = win

        self.LEFT_BORDER = self.camera.LEFT_BORDER
        self.RIGHT_BORDER = self.camera.RIGHT_BORDER
        self.DISPLAY_W = self.camera.DISPLAY_W
        self.DISPLAY_H = self.camera.DISPLAY_H

    def render(self):
        for coin in self.coins:
            self.win.blit(coin.image, (coin.rect.x - self.camera.offset.x, coin.rect.y - self.camera.offset.y))
        for block in self.blocks:
            self.win.blit(block.image, (block.rect.x - self.camera.offset.x, block.rect.y - self.camera.offset.y))
        for en in self.enemies:
            en.renderEnemy(self.win, self.camera)
        
        self.win.blit(self.player.image, (self.player.rect.x-self.camera.offset.x, self.player.rect.y-self.camera.offset.y))

        self.player.update(self)
    
        for en in self.enemies:
            en.update(self)
        
        # zbieranie monet
        for coin in self.coins:
            if self.player.rect.colliderect(coin.rect):
                self.player.get_Coin(coin)
                self.coins.remove(coin)


    def drawBG(self):
        background = pygame.image.load("assets/Background.png")
        background = pygame.transform.scale(background, (800, 600))
        self.win.blit(background, (0, 0))