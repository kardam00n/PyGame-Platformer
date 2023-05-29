import pygame 



def displayUI(win, map):

    font = pygame.font.Font('freesansbold.ttf', 24)    
    
    # wyswietlacz punktow
    points = font.render("Points: " + str(map.player.points), True, (0, 0, 0), None)
    pointsRect = points.get_rect()
    pointsRect.x= map.DISPLAY_W - pointsRect.width - 10;
    pointsRect.y=10
    map.camera.scroll()
    win.blit(points, pointsRect)

    # wyswietlacz zdrowia
    
    health = font.render(str(map.player.health) + "/" + str(map.player.maxHealth), True, (255, 255, 255), None)
    
    healthRect = health.get_rect()
    healthRect.x = 60
    healthRect.y = 12
    map.camera.scroll()
    pygame.draw.rect(win, (0,0,0), (10, 10, 200, 25))
    pygame.draw.rect(win, (255,0,0), (10,10,map.player.health,25))
    win.blit(health, healthRect)

    #wysiwietlacz strzal
    arrows = pygame.image.load(map.player.ARROWS[map.player.selectedArrows].getDisplayImg())
    arrows = pygame.transform.scale(arrows, (50,50))
    arrowsRect = arrows.get_rect()
    arrowsRect.y = arrowsRect.y + 40
    arrowsRect.x = arrowsRect.x + 10
    win.blit(arrows,arrowsRect)

def displayGameOver(win, map):
    font = pygame.font.Font('freesansbold.ttf', 24)
    gameOverStr = font.render("GAME OVER", True, (255, 0, 0), None)
    gameOverRect = gameOverStr.get_rect()
    gameOverRect.x = map.DISPLAY_W/2
    gameOverRect.y = map.DISPLAY_H/2
    win.fill((0,0,0))
    win.blit(gameOverStr, (gameOverRect.x-gameOverRect.width/2, gameOverRect.y-gameOverRect.height/2))
    pygame.display.update()

def displayWin(win, map):
    font = pygame.font.Font('freesansbold.ttf', 24)
    gameOverStr = font.render("LEVEL COMPLETED", True, (0, 255, 0), None)
    gameOverRect = gameOverStr.get_rect()
    gameOverRect.x = map.DISPLAY_W/2
    gameOverRect.y = map.DISPLAY_H/2
    win.fill((0,0,0))
    win.blit(gameOverStr, (gameOverRect.x-gameOverRect.width/2, gameOverRect.y-gameOverRect.height/2))
    pygame.display.update()