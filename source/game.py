#!/usr/bin/env python

#!/usr/bin/env python

import os, pygame, sys
from pygame.locals import *

pygame.init()

k_up = k_down = k_right = k_left = 0
player = pygame.image.load('../images/hero_placeholder.png')
HEIGHT = 500
WIDTH = 675
"Window 675 x 500"
windowSurface = pygame.display.set_mode((WIDTH,HEIGHT))
position = (WIDTH/2, HEIGHT/2)
new_position = position

BLACK = pygame.Color(255,255,255) #Temp background
fpsClock = pygame.time.Clock()
windowSurface.blit(player, position)

while True:
    windowSurface.fill(BLACK)

    
    for event in pygame.event.get():
        if not hasattr(event, 'key'): continue
        if event.key == K_RIGHT: new_position = (position[0] + 10, position[1]) 
        elif event.key == K_LEFT: new_position = (position[0] - 10, position[1])
        elif event.key == K_UP: new_position = (position[0], position[1] -10)
        elif event.key == K_DOWN: new_position = (position[0], position[1] + 10)
        elif event.key == K_ESCAPE: sys.exit(0) # quit the game
    position = new_position
    windowSurface.blit(player, position)
    pygame.display.update()
        
                
    fpsClock.tick(30)