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

#background
background = pygame.image.load('1876.png')


#player
playerimg = pygame.image.load('spaceship.png')
playerx = 380
playery = 520
playerx_change = 0

#ufo

ufoimg = pygame.image.load('ufo.png')
ufox = random.randint(0,800)
ufoy = random.randint(50,150)
ufox_change = 0.5
ufoy_change = 40

#bullet

blastimg = pygame.image.load('blast.png')
blastx = 0
blasty = 480
blast_state = "ready"
blasty_change = 10

def player(x,y):
    screen.blit(playerimg,(x,y))

def ufo(x,y):
    screen.blit(ufoimg,(x,y))
    
def blast(x,y):
    global blast_state
    blast_state = "fire"
    screen.blit(blastimg,(x+16,y+10))
    

#Game loop
while running:
    #RGB
    screen.fill((0,0,0))
    #Background image
    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        #Keystroke for Player
        if event.type == pygame.KEYDOWN:
            print("A Key Pressed")   
            if event.key == pygame.K_LEFT:
                playerx_change=-0.3
            if event.key == pygame.K_RIGHT:
                playerx_change=0.3
            if event.key == pygame.K_SPACE:
                blast(playerx,playery)
        if event.type == pygame.KEYUP:    
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerx_change=0
        
            
    # Define boundry  for player       
    playerx +=playerx_change
    if playerx <= 0:
        playerx = 0
    if playerx >=736:
        playerx = 736
    # Define boundry  for ufo
    ufox += ufox_change
    
    if ufox <= 0:
        ufox_change = 0.3
        ufoy += ufoy_change
    if ufox >=736:
        ufox_change = -0.3
        ufoy += ufoy_change
        
    #blast movement
    if blasty < 0:
        blasty = 480
        blast_state = 'ready'    
    if blast_state is 'fire':
        blast(playerx,blasty)    
        blasty -=blasty_change              
    
    player(playerx,playery)
    ufo(ufox,ufoy)
    pygame.display.update()
        
    