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
from dialogHandle import *
from companion import DownedComp

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
downedComp = DownedComp()
fpsClock = pygame.time.Clock()
"""
Sets up how big the background should be     
"""
nrows = int(windowSurface.get_height() / 32) + 1
ncols = int(windowSurface.get_width() / 32) + 1
background_rect = level_background[0][0].get_rect()
dialog_handle = HandleDialog(windowSurface, dialogbox)
reset = 0
interact_flag = False

current_level =0
#helpers.set(current_level, (560, 250))
pygame.key.set_repeat(1, 10)
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit(0) # Clicking the x now closes the game, not ESC
        if event.type ==KEYUP:
        	if event.key == K_RETURN:
        		dialogbox.progress() #Moves the dialog box along
        	if event.key == K_RSHIFT:
        	    interact_flag = True
        	if event.key == K_k:
        		current_level = len(doors_by_level)-6
        		player.startRoom(player_entrance[current_level -5])
        		#to jump to last room
        		player.getBelt()
        		player.getGaunt()
        	if event.key == K_ESCAPE:
        		reset = helpers.pauseBalls(windowSurface)
        	if event.key == K_o:
        		enemies_by_level[current_level].empty()
        	if event.key == K_1:
        		rocks_by_level[current_level].add(pygame.sprite.RenderPlain(Rock((player.rect.topleft[0] + 40, player.rect.topleft[1]))))

    
    """
    Death and resetting taken care of here
    """
    if not player.alive:
        reset = helpers.dead(windowSurface)
        player.health = 1
        player.alive = True
        reset +=1
        print reset
    
    if reset == 6:
        player.health = 5
        current_level = 0
        reset =1
    
    if reset == 1:
       if current_level < 4:
          current_level = 0
       elif current_level < 7:
          current_level = 4
       elif current_level < 11:
          current_level = 7
       else:
          current_level = 11
       
       
       returns = helpers.reset(current_level, windowSurface)
       enemies_by_level = returns[0]
       rocks_by_level = returns[1]
       if current_level ==0:
          player.startRoom((560, 250))
       else:
          player.startRoom(player_entrance[current_level-1])
       reset = 0
    
    
    """
    This is just for the companionDead thing to start up the comp
    """
    if pygame.sprite.collide_rect(player, downedComp) and interact_flag == True:
         player.getFriend()
         downedComp.leave()
    
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
    			dialogbox.set_dialog(speech_by_level[current_level][2:last])
    			speech_by_level[current_level] = "0"
    	elif speech_by_level[current_level][0] == "5":
    	    i = 1 #5 means do nothing 
    	else:	
    		dialogbox.set_dialog(speech_by_level[current_level])
    		speech_by_level[current_level] = "0"

    
        
    """
    This is what, unless there is a transition, draws everything but the background to the
    screen.
    """

    if not transitioning:
        if not plates_by_level[current_level] == "1":
        	plates_by_level[current_level].draw(windowSurface)
        player.update_position(rocks_by_level[current_level], playerGroup, enemies_by_level[current_level], plates_by_level[current_level])
        doors_by_level[current_level].draw(windowSurface)
        if current_level == 11: #For the downed comp sprite
            downedComp.showUp(windowSurface)
        playerGroup.draw(windowSurface)
        enemies_by_level[current_level].update(player, rocks_by_level[current_level])
        rocks_by_level[current_level].draw(windowSurface)   
        enemies_by_level[current_level].draw(windowSurface)
        HUB.drawHealth(player, windowSurface)
        dialogbox.draw(windowSurface, (50, 400))
        dialog_handle.update(current_level, enemies_by_level[current_level], windowSurface)
    else:
        trans_surface = transition.do()
        windowSurface.blit(trans_surface,(0,0))
        if transition.is_done():
            transitioning = False        

    if not plates_by_level[current_level] =="1":
    	plate_list = plates_by_level[current_level].sprites()
    	if plate_list[0].isLocked(rocks_by_level[current_level]):
    		current_door = doors_by_level[current_level].sprites()
    		current_door[0].unlock()

    
    
    """
    Called when the player hits the door, starts transition.
    Below everything so if the door is locked the screen is drawn
    fully before going into dialog loop
    """
    levelChange = pygame.sprite.spritecollide(player, doors_by_level[current_level],False)
        
    
    if levelChange and interact_flag:
    	if enemies_by_level[current_level]: #makes sure all enemies are dead before proceeding
    		dialog_handle.enemyAlive(windowSurface)
    		player.backUp()
    		#Might make this an array and call a random KILL_ENEMY dialog. For style.
    	elif not plates_by_level[current_level] =="1":
    	   if not plate_list[0].isLocked(rocks_by_level[current_level]):
    	      dialog_handle.doorLocked(windowSurface)
    	      player.backUp()
           else:
              plates_by_level[current_level] = "1"
    	else:	
        	player.startRoom(player_entrance[current_level])
        	current_level += 1
        	if current_level >= 4:
        	   player.getBelt() 
        	if current_level >= 8:
        	   player.getGaunt()	
        	#helpers.set(current_level, player_entrance[current_level-1])
        	level_background = level_maker.drawBackground(windowSurface)
        	transitioning = True
        	dialog_handle.levelChange()
    
    interact_flag = False
    pygame.display.update()
    fpsClock.tick(30)
    
