import pygame
import Player
# import Tile
import Find
import Box
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
player = Player.Player(0,50)
rect1 = pygame.Rect(0,500,800,100)

# lista zawierajaca znajdzki/monety
monets = [Find.Find(40, 450), Find.Find(150, 450), Find.Find(260, 450), Find.Find(300, 400)]

# lista zawierajaca bloki
blocks = [Box.Box(0+50*i, 500) for i in range(25)]
blocks.append(Box.Box(300, 450))
blocks.append(Box.Box(250, 300))
while run:
    # czyszczenie ekranu
    win.fill((0, 0, 0))
    # zamkniecie gry
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    # opóźnienie w grze
    pygame.time.delay(50)

    # dodawanie obiektow do mapy
    a = player.update(blocks)
    win.blit(player.image, player.rect)
    for moneta in monets:
        win.blit(moneta.image, moneta.rect)
    for block in blocks:
        win.blit(block.image, block.rect)

    # zbieranie monet
    for moneta in monets:
        if player.rect.colliderect(moneta.rect):
            player.get_Find(moneta)
            monets.remove(moneta)

    # wyswietlacz punktow
    font = pygame.font.Font('freesansbold.ttf', 36)
    points = font.render(str(player.points), True, (0, 255, 0), (0, 0, 128))
    pointsRect = points.get_rect()
    pointsRect.x=0
    pointsRect.y=0
    win.blit(points, pointsRect)


    # pygame.draw.rect(win, (0, 255, 0), (x, y, szerokosc, wysokosc))

    # odświeżenie ekranu
    pygame.display.update()