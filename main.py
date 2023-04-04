import pygame
import Player
# import Tile
import Find
import Box
import Camera
pygame.init()


#rozmiary mapy wysokosc 600 szerokosc 2400, kamera 600 x 800
Tiles = []
win = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pierwsza gra")
#make and display background in pygame from file

x = 0
y = 40
szerokosc = 50
wysokosc = 50
krok = 20
run = True
player = Player.Player(0,400)
camera = Camera.Camera(player)
rect1 = pygame.Rect(0,500,800,100)

# lista zawierajaca znajdzki/monety
monets = [Find.Find(40, 450), Find.Find(150, 450), Find.Find(260, 450), Find.Find(300, 400)]

# lista zawierajaca bloki
blocks = [Box.Box(0+50*i, 500) for i in range(48)]
for i in range(48):
    blocks.append(Box.Box(0+50*i, 550))
blocks.append(Box.Box(300, 450))
blocks.append(Box.Box(250, 350))
while run:
    background = pygame.image.load("assets/Background.png")
    background = pygame.transform.scale(background, (800, 600))
    win.blit(background, (0, 0))
    # zamkniecie gry
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    # opóźnienie w grze
    pygame.time.delay(50)

    # dodawanie obiektow do mapy
    a = player.update(blocks)
   
    for moneta in monets:
        win.blit(moneta.image, (moneta.rect.x - camera.offset.x, moneta.rect.y - camera.offset.y))
    for block in blocks:
        win.blit(block.image, (block.rect.x - camera.offset.x, block.rect.y - camera.offset.y))

    # zbieranie monet
    for moneta in monets:
        if player.rect.colliderect(moneta.rect):
            player.get_Find(moneta)
            monets.remove(moneta)

    # wyswietlacz punktow
    font = pygame.font.Font('freesansbold.ttf', 36)
    points = font.render(str(player.points), True, (0, 0, 0), None)
    pointsRect = points.get_rect()
    pointsRect.x=0
    pointsRect.y=0
    camera.scroll()
    win.blit(player.image, (player.rect.x-camera.offset.x, player.rect.y-camera.offset.y))
    win.blit(points, pointsRect)

    # odświeżenie ekranu
    pygame.display.update()