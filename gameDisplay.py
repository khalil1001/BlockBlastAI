import pygame
import numpy as np
import random as rd

from stage import Stage
from player import Player

def sign(x,eps=2):
    if x>eps:
        return 1
    if x<-eps:
        return -1
    return 0

# pygame setup
pygame.init()
screen = pygame.display.set_mode((960, 960))
clock = pygame.time.Clock()
running = True
dt = 0
elapsed = 0

delay = 1
i = 0

squareSize = 50

stg = Stage()
player = Player()

def gameOver():
    transparent_surface = pygame.Surface((screen.get_width(), screen.get_height()), pygame.SRCALPHA)
    pygame.draw.rect(transparent_surface, pygame.Color(128, 128, 128, 125), pygame.Rect(0, 0, screen.get_width(), screen.get_height()))
    screen.blit(transparent_surface, (0, 0))
    font = pygame.font.SysFont('Arial', 150)
    text_surface = font.render('Game Over!', True, 'brown2')
    screen.blit(text_surface, (screen.get_width()/2-text_surface.get_width()/2, screen.get_height()/2-text_surface.get_height()/2))


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")
    stg.displayStage(screen,(screen.get_width() / 2, screen.get_height() / 2-4*squareSize))
    
    
    if elapsed > i*delay:
        possiblePieces = stg.getPossiblePieces()
        if len(possiblePieces) != 0:
            p,pos = player.getNextMove(stg,possiblePieces,stg.score)
            stg.play(p,pos)
            i += 1
        else:
            gameOver()
        
    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000
    elapsed += dt
pygame.quit()