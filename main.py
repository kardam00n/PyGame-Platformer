import pygame
import Entities.Player as Player
# import Tile
import Display.Coin as Coin
import Display.Box as Box
import Display.Camera as Camera
import Entities.enemy as enemy
import Display.map as map
import Display.UI as UI

pygame.init()


#rozmiary mapy wysokosc 600 szerokosc 2400, kamera 600 x 800
win = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pierwsza gra")

run = True
gameOver = False
map = map.Map(win)



# lista zawierajaca bloki


while run:
    map.drawBG()
    
    # zamkniecie gry
    if map.player.health<=0:
        gameOver = True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            gameOver = False
    
    # opóźnienie w grze
    pygame.time.delay(20)

    # dodawanie obiektow do mapy
    map.render()
    

    UI.displayUI(win, map)
    
    while gameOver:
        UI.displayGameOver(win, map)
    # odświeżenie ekranu
    pygame.display.update()
