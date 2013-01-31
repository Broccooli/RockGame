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

player = Player((x,y), windowSurface)
playerGroup = pygame.sprite.RenderPlain(player)
HUB = HUB()
transition = Transition(windowSurface)

my_font = pygame.font.SysFont('Verdana', 15)
dialogbox = DialogBox((440, 51), (255, 255, 204), 
    (102, 0, 0), my_font)


level_maker = Levels()

rocks_by_level = level_maker.createLevels_Rock()
doors_by_level = level_maker.createLevels_Door()
enemies_by_level = level_maker.createLevels_enemies(windowSurface)
level_background = level_maker.drawBackground(windowSurface)
speech_by_level = level_maker.dialogSelect()
fpsClock = pygame.time.Clock()

nrows = int(windowSurface.get_height() / 32) + 1
ncols = int(windowSurface.get_width() / 32) + 1
background_rect = level_background[0][0].get_rect()
WHITE = pygame.image.load('../images/fade.png')
WHITE_Rect = WHITE.get_rect()


current_level =0
pygame.key.set_repeat(1, 10)
while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit(0) # Clicking the x now closes the game, not ESC
        if event.type ==KEYUP:
        	if event.key == K_RETURN:
        		dialogbox.progress()
    
    for y in range(nrows):
    	for x in range(ncols):
    		background_rect.topleft = (x * background_rect.width, y* background_rect.height)
    		windowSurface.blit(level_background[y][x], background_rect)
    levelChange = pygame.sprite.spritecollide(player, doors_by_level[current_level],True)
    
    if not speech_by_level[current_level] == "0":
    	dialogbox.set_dialog(speech_by_level[current_level])
    	speech_by_level[current_level] = "0"
    
    
    
    if levelChange:
        current_level = 1
        #helpers.fadeOut(windowSurface, 50)
        #time.sleep(.1)
        level_background = level_maker.drawBackground(windowSurface)
        player.getBelt()
        transitioning = True

    if not transitioning:
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
    
