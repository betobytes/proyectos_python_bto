import pygame as pg
import random

#inicializar
pg.init()

#creamos la ventana
screen = pg.display.set_mode((800,600))

#titulo e icono
pg.display.set_caption("sapce_invaders")
icon = pg.image.load('arcade-game.png')
pg.display.set_icon(icon)

#cargar imagen del jugador
playerimg = pg.image.load('002-space-shuttle.png')
playerX = 380
playerY = 480

#enemigo
enemyimg = pg.image.load('001-space-ship.png')
enemyX = random.randint(64,736)
enemyY = random.randint(64,400)
enemyX_change = 0

playerX_change = 0

def player(x, y):
    screen.blit(playerimg,(x, y))

def enemy(x, y):
    screen.blit(enemyimg,(x, y))
#BUCLE DE JUEGO --GAME LOOP--
game_over = False

while game_over != True:

    #color de pantalla
    screen.fill((0,0,10))


    for event in pg.event.get():
        if event.type == pg.QUIT:
            game_over = True

        if event.type == pg.KEYDOWN:
            #print(' a keystroke is press')
            if event.key == pg.K_LEFT:
                playerX_change = -0.4
                #print('left arrow is pressed')
            if event.key == pg.K_RIGHT:
                playerX_change = 0.4
                #print('right row is pressed')
        if event.type == pg.KEYUP:
            if event.key == pg.K_LEFT or event.key == pg.K_RIGHT:
                playerX_change = 0
                #print('keystoke has been released')

    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    player(playerX, playerY)
    enemy(enemyX, enemyY)
    enemy(64, 100)
    pg.display.update()
