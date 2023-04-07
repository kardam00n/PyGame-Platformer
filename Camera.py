import pygame
vec = pygame.math.Vector2

class Camera():
    def __init__(self,player):
        self.player = player
        self.offset = vec(0,0)
        self.offset_float = vec(0,0)
        self.DISPLAY_W = 800
        self.DISPLAY_H = 600
        self.LEFT_BORDER = 0
        self.RIGHT_BORDER = 2400
        self.CENTER = vec(-self.DISPLAY_W/2, -self.DISPLAY_H/2)
        self.BOTTOM_BORDER = self.DISPLAY_H
    def scroll(self):
        self.offset_float.x += (self.player.rect.x - self.offset_float.x + self.CENTER.x)
        self.offset_float.y += (self.player.rect.y - self.offset_float.y + self.CENTER.y)
        self.offset.x = int(self.offset_float.x)
        self.offset.y = int(self.offset_float.y)
        self.offset.x = max(self.LEFT_BORDER, self.offset.x)
        self.offset.x = min(self.RIGHT_BORDER - self.DISPLAY_W, self.offset.x)
        self.offset.y = min(self.BOTTOM_BORDER - self.DISPLAY_H, self.offset.y)