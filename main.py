import pygame

from Entities import enemy, Player
from Display import Block, Camera, Coin, map, UI

pygame.init()


#rozmiary mapy wysokosc 600 szerokosc 2400, kamera 600 x 800
#w blokach: 12x48 (dla kamery 12x16)
win = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pierwsza gra")

run = True
gameOver = False
completed = False
map = map.Map(win)



# lista zawierajaca bloki


while run:
    map.drawBG()
    
    # zamkniecie gry
    if map.player.health<=0 and not completed:
        gameOver = True
    if map.player.completed and not gameOver:
        completed = True
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
        break
    while completed:
        UI.displayWin(win, map)
        break
    # odświeżenie ekranu
    pygame.display.update()
