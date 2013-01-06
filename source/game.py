#!/usr/bin/env python

#!/usr/bin/env python

import os, pygame, sys
from pygame.locals import *

pygame.init()


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

pygame.key.set_repeat(1, 10)
while True:
    windowSurface.fill(BLACK)

# Need to filter events to only KEYDOWN
# this change may be temporary depending on how the game goes
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
         if event.key == K_RIGHT and position[0] < (WIDTH - 20): new_position = (position[0] + 10, position[1])
         elif event.key == K_LEFT and position[0] > 20: new_position = (position[0] - 10, position[1])
         elif event.key == K_UP and position[1] > (20):new_position = (position[0], position[1] -10)
         elif event.key == K_DOWN and position [1] < (HEIGHT -20): new_position = (position[0], position[1] + 10)
         elif event.key == K_ESCAPE: sys.exit(0) # quit the game
    position = new_position
    windowSurface.blit(player, position)
    pygame.display.update()
        
                
    fpsClock.tick(30)
    
    
