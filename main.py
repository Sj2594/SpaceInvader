import pygame
from pygame import image
import random


pygame.init()
screen = pygame.display.set_mode((800,600))

running = True

#display
pygame.display.set_caption("SPACE INVADERS")
image = pygame.image.load('space-invaders.png')
pygame.display.set_icon(image)

#player
playerimg = pygame.image.load('spaceship.png')
playerx = 380
playery = 520
playerx_change=0

#ufo
#player
ufoimg = pygame.image.load('ufo.png')
ufox = random.randint(0,770)
ufoy = random.randint(50,150)

def player(x,y):
    screen.blit(playerimg,(x,y))

def ufo(x,y):
    screen.blit(ufoimg,(x,y))

#Game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        #Keystroke for Player
        if event.type == pygame.KEYDOWN:
            print("A Key Pressed")   
            if event.key == pygame.K_LEFT:
                playerx_change=-0.1
            if event.key == pygame.K_RIGHT:
                playerx_change=0.1
        if event.type == pygame.KEYUP:    
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerx_change=0
    playerx +=playerx_change
    if playerx <= 0:
        playerx = 0
    if playerx >=736:
        playerx = 736
        
                        
    screen.fill((0,0,0))
    player(playerx,playery)
    ufo(ufox,ufoy)
    pygame.display.update()
        
    