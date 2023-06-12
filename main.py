import pygame

from enum import Enum
from Entities import enemy, Player
from Display import Block, Camera, Coin, map, UI
from Display.UI import GameState


if __name__ == '__main__':
    pygame.init()


    #rozmiary mapy wysokosc 600 szerokosc 2400, kamera 600 x 800
    #w blokach: 12x48 (dla kamery 12x16)
    win = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Platformers")

    run = True
    map = map.Map(win)
    currentState = GameState.MAINMENU
    ui = UI.UI(win, map)

    while run:
        map.drawBG()

        # zamkniecie gry
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # opóźnienie w grze
        pygame.time.delay(15)

        currentState = ui.currentState
        # dodawanie obiektow do mapy
        if currentState == GameState.FINISHED:
            ui.displayWin()
        if currentState == GameState.GAMEOVER:
            ui.displayGameOver()
        if currentState == GameState.RUNNING:
            map.render()
            ui.displayUI()
        if currentState == GameState.CREDITS:
            ui.displayCredits()
        if currentState == GameState.MAINMENU:
            ui.displayMainMenu()
            
        # odświeżenie ekranu
        pygame.display.update()
