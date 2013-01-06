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
x = WIDTH / 2
y = HEIGHT / 2
# new_position = (x,y)

BLACK = pygame.Color(255,255,255) #Temp background
fpsClock = pygame.time.Clock()
windowSurface.blit(player, (x,y))

pygame.key.set_repeat(1, 10)
while True:
    windowSurface.fill(BLACK)

# Need to filter events to only KEYDOWN
# this change may be temporary depending on how the game goes
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit(0) # Clicking the x now closes the game, not ESC
    
    keys = pygame.key.get_pressed()
    
    if keys[K_LEFT]:
        x -= 10
        if x <= 0:
            x = 0
    if keys[K_RIGHT]:
        x += 10
        if x >= 643:
            x = 643        
    if keys[K_DOWN]:
        y += 10
        if y >= 468:
            y = 468
    if keys[K_UP]:
        y -= 10
        if y <= 0:
            y = 0
        
    windowSurface.blit(player, (x,y))
    pygame.display.update()
    fpsClock.tick(30)
"""
    for event in pygame.event.get():        
        if event.type == pygame.KEYDOWN:
            if event.key == K_UP:
                dmy = -1 * speedy
                if pygame.event.poll() == K_RIGHT:
                    dmx = 1 * speedx
                elif pygame.event.poll() == K_LEFT:
                    dmx = -1 * speedx
            if event.key == K_DOWN:
                dmy = 1 * speedy
                if event.key == K_RIGHT:
                    dmx = 1 * speedx
                elif event.key == K_LEFT:
                    dmx = -1 * speedx
            if event.key == K_ESCAPE:
                sys.exit(0) #quits the game
    
    x += dmx
    y += dmy
    
    windowSurface.blit(player, (x,y))
    dmx = 0
    dmy = 0
    pygame.display.update()
    
    fpsClock.tick(30)
"""    
    
"""
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
         if event.key == K_RIGHT and position[0] < (WIDTH - 20): new_position = (position[0] + 10, position[1])
         elif event.key == K_LEFT and position[0] > 20: new_position = (position[0] - 10, position[1])
         elif event.key == K_UP and position[1] > (20):
            if event.key == K_RIGHT:
                new_position = (position[0] + 10, position[1] - 10)
            else:
                new_position = (position[0], position[1] -10)
         elif event.key == K_DOWN and position [1] < (HEIGHT -20): new_position = (position[0], position[1] + 10)
         elif event.key == K_ESCAPE: sys.exit(0) # quit the game
    position = new_position
    windowSurface.blit(player, position)
    pygame.display.update()
        
                
    fpsClock.tick(30)
"""
    
    
