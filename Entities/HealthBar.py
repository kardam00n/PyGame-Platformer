import pygame

class HealthBar():
    def __init__(self, health, maxHealth):
            self.health = health
            self.maxHealth = maxHealth
    def render(self, win,camera, x ,y, currentHealth):
            font = pygame.font.Font('freesansbold.ttf', 12)
            healthVal = font.render(str(currentHealth) + "/" + str(self.maxHealth), True, (255, 255, 255), None)
            healthRect = healthVal.get_rect()
            healthRect.x = x
            healthRect.y = y
            pygame.draw.rect(win, (0,0,0), (x - camera.offset.x, y - camera.offset.y, 100, 10))
            pygame.draw.rect(win, (255,0,0), (x - camera.offset.x, y - camera.offset.y,currentHealth/self.maxHealth * 100,10))
            win.blit(healthVal, (healthRect.x - camera.offset.x, healthRect.y - camera.offset.y))