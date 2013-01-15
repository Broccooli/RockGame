#!/usr/bin/env python

#!/usr/bin/env python

import os, pygame, sys
from pygame.locals import *
from doors import Door
from player import Player
from rocks import Rock
from levels import Levels

pygame.init()




WIDTH = 675
HEIGHT = 500
"Window 675 x 500"
windowSurface = pygame.display.set_mode((WIDTH,HEIGHT))
x = WIDTH / 2
y = HEIGHT / 2
# new_position = (x,y)

door = Door((5,15))
door_group = pygame.sprite.RenderPlain(door)
player = Player((x,y))
playerGroup = pygame.sprite.RenderPlain(player)

rocks_by_level = Levels().createLevels_Rock()


BLACK = pygame.Color(255,255,255) #Temp background
fpsClock = pygame.time.Clock()

current_level =0
pygame.key.set_repeat(1, 10)
while True:
    windowSurface.fill(BLACK)

    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit(0) # Clicking the x now closes the game, not ESC
    

    
    if pygame.sprite.collide_rect(player, door) == True:
    	current_level = 1
     

    player.update_position(rocks_by_level[current_level])
    playerGroup.draw(windowSurface)
    door_group.draw(windowSurface)
    rocks_by_level[current_level].draw(windowSurface)
    pygame.display.update()
    fpsClock.tick(30)

    
