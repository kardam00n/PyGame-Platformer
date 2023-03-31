import pygame
# import Player
# import Tile

pygame.init()


#rozmiary mapy wysokosc 800 szerokosc 1800
win = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pierwsza gra")

x = 0
y = 40
szerokosc = 50
wysokosc = 50
krok = 20
run = True

rect1 = pygame.Rect(0,500,800,100)

while run:
    # opóźnienie w grze
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    # obsługa zdarzeń
    keys = pygame.key.get_pressed()

    rect2 = pygame.Rect(x, y, szerokosc, wysokosc);
    collide = rect1.colliderect(rect2)

    # warunki do zmiany pozycji obiektu
    if keys[pygame.K_LEFT]:
        x -= krok
    if keys[pygame.K_RIGHT]:
        x += krok
    if keys[pygame.K_SPACE] and collide:
        y-= krok*5

    if(collide==0):
        y+=krok/5
    # if keys[pygame.K_UP]:
    #     y -= krok
    # if keys[pygame.K_DOWN] :
    #     y += krok

    # "czyszczenie" ekranu
    win.fill((0, 0, 0))
    # rysowanie prostokąta
    color = (255,255,255)
    pygame.draw.rect(win, color, (0, 500, 800, 100))

    pygame.draw.rect(win, (0, 255, 0), (x, y, szerokosc, wysokosc))

    # odświeżenie ekranu
    pygame.display.update()