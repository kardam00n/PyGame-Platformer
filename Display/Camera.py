import pygame
vec = pygame.math.Vector2

class Camera():
    def __init__(self,player, map):
        self.player = player
        self.offset = vec(0,0)
        self.LEFT_BORDER = map.LEFT_BORDER
        self.RIGHT_BORDER = map.RIGHT_BORDER
        self.DISPLAY_W = map.DISPLAY_W
        self.DISPLAY_H = map.DISPLAY_H
        self.CENTER = vec(-self.DISPLAY_W/2, -self.DISPLAY_H/2)
        self.BOTTOM_BORDER = self.DISPLAY_H
    def scroll(self):

        self.offset.x += (self.player.rect.x - self.offset.x + self.CENTER.x)
        self.offset.y += (self.player.rect.y - self.offset.y + self.CENTER.y)
  
        #granice wyswietlania kamery
        self.offset.x = max(self.LEFT_BORDER, self.offset.x)
        self.offset.x = min(self.RIGHT_BORDER - self.DISPLAY_W, self.offset.x)
        self.offset.y = min(self.BOTTOM_BORDER - self.DISPLAY_H, self.offset.y)