#!/usr/bin/env python

#!/usr/bin/env python

import os, pygame, sys
from pygame.locals import *
from doors import Door
from player import Player
from rocks import Rock

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

rocks_by_level = []
#setting up rocks for this room. This is how it will be done for puzzles. 
#Long yes, but it matters where we put it
test_room_rocks = [Rock((100, 10)), Rock((200, 205)), Rock((400, 300))]
test_room_rocks_group = pygame.sprite.RenderPlain(test_room_rocks)
rocks_by_level.append(test_room_rocks_group) #0
#this is how to make a group to represent the level, then add it to the level array

#First room, rocks
s1r1_rocks = [Rock((500, 10)), Rock((300, 300)), Rock((110, 100))]
s1r1_rocks_group = pygame.sprite.RenderPlain(s1r1_rocks)
rocks_by_level.append(s1r1_rocks_group) #1

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

    
