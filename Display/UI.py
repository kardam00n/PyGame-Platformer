import pygame 
from enum import Enum
from Levels import MapParser

class GameState(Enum):
    MAINMENU = 1
    RUNNING = 2
    GAMEOVER = 3
    FINISHED = 4
    CREDITS = 5

class UI():
    def __init__(self, win, map):
        self.win = win
        self.map = map
        self.currentState = GameState.MAINMENU
    def displayUI(self):

        win = self.win
        map = self.map

        if map.player.health<=0:
            self.currentState = GameState.GAMEOVER
        if map.player.completed:
            self.currentState = GameState.FINISHED

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

    def displayGameOver(self):

        win = self.win
        map = self.map

        font = pygame.font.Font('freesansbold.ttf', 24)
        gameOverStr = font.render("GAME OVER", True, (255, 0, 0), None)
        gameOverRect = gameOverStr.get_rect()
        gameOverRect.x = map.DISPLAY_W/2
        gameOverRect.y = map.DISPLAY_H/2

        BackStr = font.render("Powrót", True, (255, 0, 0), None)
        BackRect = BackStr.get_rect()
        BackRect.x = map.DISPLAY_W/2
        BackRect.y = map.DISPLAY_H/5 + 250

        if pygame.mouse.get_pressed()[0]:
            if BackRect.collidepoint(pygame.mouse.get_pos()):
                self.currentState = GameState.MAINMENU

        win.fill((0,0,0))
        win.blit(gameOverStr, (gameOverRect.x-gameOverRect.width/2, gameOverRect.y-gameOverRect.height/2))
        win.blit(BackStr, (BackRect.x-BackRect.width/2, BackRect.y-BackRect.height/2))
        pygame.display.update()

    def displayWin(self):

        win = self.win
        map = self.map

        font = pygame.font.Font('freesansbold.ttf', 24)
        winStr = font.render("LEVEL COMPLETED", True, (0, 255, 0), None)
        winRect = winStr.get_rect()
        winRect.x = map.DISPLAY_W/2
        winRect.y = map.DISPLAY_H/2
        
        BackStr = font.render("Powrót", True, (0, 255, 0), None)
        BackRect = BackStr.get_rect()
        BackRect.x = map.DISPLAY_W/2
        BackRect.y = map.DISPLAY_H/5 + 250
        
        if pygame.mouse.get_pressed()[0]:
            if BackRect.collidepoint(pygame.mouse.get_pos()):
                self.currentState = GameState.MAINMENU

        win.fill((0,0,0))
        win.blit(winStr, (winRect.x-winRect.width/2, winRect.y-winRect.height/2))
        win.blit(BackStr, (BackRect.x-BackRect.width/2, BackRect.y-BackRect.height/2))
        pygame.display.update()

    def displayMainMenu(self):


        win = self.win
        map = self.map

        map.drawBG()
        font = pygame.font.Font('freesansbold.ttf', 36)
        TitleStr = font.render("Platformers", True, (255, 255, 255), None)
        TitleRect = TitleStr.get_rect()
        TitleRect.x = map.DISPLAY_W/2
        TitleRect.y = map.DISPLAY_H/5

        PlayStr = font.render("Rozpocznij", True, (255, 255, 255), None)
        PlayRect = PlayStr.get_rect()
        PlayRect.x = map.DISPLAY_W/2
        PlayRect.y = map.DISPLAY_H/5 + 100

        CreditsStr = font.render("Twórcy", True, (255, 255, 255), None)
        CreditsRect = CreditsStr.get_rect()
        CreditsRect.x = map.DISPLAY_W/2
        CreditsRect.y = map.DISPLAY_H/5 + 150

        if pygame.mouse.get_pressed()[0]:
            if PlayRect.collidepoint(pygame.mouse.get_pos()):
                self.currentState = GameState.RUNNING
                map.resetLevel()
            if CreditsRect.collidepoint(pygame.mouse.get_pos()):
                self.currentState = GameState.CREDITS

        win.blit(TitleStr, (TitleRect.x-TitleRect.width/2, TitleRect.y-TitleRect.height/2))
        win.blit(PlayStr, (PlayRect.x-PlayRect.width/2, PlayRect.y-PlayRect.height/2))
        win.blit(CreditsStr, (CreditsRect.x-CreditsRect.width/2, CreditsRect.y-CreditsRect.height/2))
        pygame.display.update()

    def displayCredits(self):
        win = self.win
        map = self.map
        map.drawBG()
        font = pygame.font.Font('freesansbold.ttf', 36)
        TitleStr = font.render("Twórcy:", True, (255, 255, 255), None)
        TitleRect = TitleStr.get_rect()
        TitleRect.x = map.DISPLAY_W/2
        TitleRect.y = map.DISPLAY_H/5

        font = pygame.font.Font('freesansbold.ttf', 24)
        PlayStr = font.render("Dawid Kardacz", True, (255, 255, 255), None)
        PlayRect = PlayStr.get_rect()
        PlayRect.x = map.DISPLAY_W/2
        PlayRect.y = map.DISPLAY_H/5 + 100

        Play2Str = font.render("Jakub Kroczek", True, (255, 255, 255), None)
        Play2Rect = Play2Str.get_rect()
        Play2Rect.x = map.DISPLAY_W/2
        Play2Rect.y = map.DISPLAY_H/5 + 150

        BackStr = font.render("Powrót", True, (255, 255, 255), None)
        BackRect = BackStr.get_rect()
        BackRect.x = map.DISPLAY_W/2
        BackRect.y = map.DISPLAY_H/5 + 250

        if pygame.mouse.get_pressed()[0]:
            if BackRect.collidepoint(pygame.mouse.get_pos()):
                self.currentState = GameState.MAINMENU

        win.blit(TitleStr, (TitleRect.x-TitleRect.width/2, TitleRect.y-TitleRect.height/2))
        win.blit(PlayStr, (PlayRect.x-PlayRect.width/2, PlayRect.y-PlayRect.height/2))
        win.blit(Play2Str, (Play2Rect.x-Play2Rect.width/2, Play2Rect.y-Play2Rect.height/2))
        win.blit(BackStr, (BackRect.x-BackRect.width/2, BackRect.y-BackRect.height/2))
        pygame.display.update()
