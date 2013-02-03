#!/usr/bin/env python

#!/usr/bin/env python

import os, pygame, sys, time, helpers, speechConstants
from pygame.locals import *
from doors import Door
from player import Player
from rocks import Rock
from levels import Levels
from HUB import *
from dimmer import Dimmer
from transition import Transition

pygame.init()


WIDTH = 672
HEIGHT = 512
"Window 672 x 512"
windowSurface = pygame.display.set_mode((WIDTH,HEIGHT))
x = WIDTH / 2
y = HEIGHT / 2
transitioning = False
# new_position = (x,y)

player = Player((560,250), windowSurface)
playerGroup = pygame.sprite.RenderPlain(player)


HUB = HUB()
transition = Transition(windowSurface)

my_font = pygame.font.SysFont('Verdana', 15)
dialogbox = DialogBox((440, 51), (255, 255, 204), 
    (102, 0, 0), my_font)


level_maker = Levels()
"""
Level maker is used below to generate all the array of sprites of enemies, rocks, 
doors, and dialog    
"""

rocks_by_level = level_maker.createLevels_Rock()
doors_by_level = level_maker.createLevels_Door()
enemies_by_level = level_maker.createLevels_enemies(windowSurface)
level_background = level_maker.drawBackground(windowSurface)
speech_by_level = level_maker.dialogSelect()
player_entrance = level_maker.playerStartPositions()
plates_by_level = level_maker.placePlate()
fpsClock = pygame.time.Clock()
"""
Sets up how big the background should be     
"""
nrows = int(windowSurface.get_height() / 32) + 1
ncols = int(windowSurface.get_width() / 32) + 1
background_rect = level_background[0][0].get_rect()


current_level =0
pygame.key.set_repeat(1, 10)
while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit(0) # Clicking the x now closes the game, not ESC
        if event.type ==KEYUP:
        	if event.key == K_RETURN:
        		dialogbox.progress() #Moves the dialog box along
        	if event.key == K_k:
        		current_level = len(doors_by_level)-1#to jump to last room
        		player.getBelt()
    
    """
    This is for background things, need it to keep it there
    """
    
    for y in range(nrows):
    	for x in range(ncols):
    		background_rect.topleft = (x * background_rect.width, y* background_rect.height)
    		windowSurface.blit(level_background[y][x], background_rect)    
    """
    This calls the dialog box, it has to reset back to 0 or it will keep calling the box, which is bad
    The "1" is for special conditions, where there is dialog after the level
    """
    
    if not speech_by_level[current_level] == "0":
    	if speech_by_level[current_level][0] == "1": #Using this for dialog that wont start till a condition is met
    		if not enemies_by_level[current_level]:
    			last = len(speech_by_level[current_level])
    			dialogbox.set_dialog(speech_by_level[current_level][1:last])
    			speech_by_level[current_level] = "0"
    	else:	
    		dialogbox.set_dialog(speech_by_level[current_level])
    		speech_by_level[current_level] = "0"
    
    """
    Called when the player hits the door, starts transition
    """
    levelChange = pygame.sprite.spritecollide(player, doors_by_level[current_level],False)
    
    if levelChange:#PROBLEM, standing on the door keeps calling set_dialog. Stuck on first letter unles you back off
    	if enemies_by_level[current_level]: #makes sure all enemies are dead before proceeding
    		dialogbox.set_dialog(speechConstants.ENEMY_ALIVE)
    		#Might make this an array and call a random KILL_ENEMY dialog. For style.
    	elif not plates_by_level[current_level] =="1":
    	   plate_list = plates_by_level[current_level].sprites()
    	   if not plate_list[0].locked(rocks_by_level[current_level]):
    	      dialogbox.set_dialog(speechConstants.DOOR_LOCKED)
           else:
              plates_by_level[current_level] = "1"
    	else:	
        	player.startRoom(player_entrance[current_level])
        	current_level += 1
        	if current_level >= 4:
        	   player.getBelt() 	
        	level_background = level_maker.drawBackground(windowSurface)
        	transitioning = True
        
    """
    This is what, unless there is a transition, draws everything but the background to the
    screen.
    """

    if not transitioning:
        if not plates_by_level[current_level] == "1":
        	plates_by_level[current_level].draw(windowSurface)
        player.update_position(rocks_by_level[current_level], playerGroup, enemies_by_level[current_level])
        playerGroup.draw(windowSurface)
        enemies_by_level[current_level].update(player, rocks_by_level[current_level])
        enemies_by_level[current_level].draw(windowSurface)    
        doors_by_level[current_level].draw(windowSurface)
        rocks_by_level[current_level].draw(windowSurface)
        HUB.drawHealth(player, windowSurface)
        dialogbox.draw(windowSurface, (50, 400))
    else:
        trans_surface = transition.do()
        windowSurface.blit(trans_surface,(0,0))
        if transition.is_done():
            transitioning = False        
    
    pygame.display.update()
    fpsClock.tick(30)
    
