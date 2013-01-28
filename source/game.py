#!/usr/bin/env python

#!/usr/bin/env python

import os, pygame, sys, time
from pygame.locals import *
from doors import Door
from player import Player
from rocks import Rock
from levels import Levels
from HUB import HUB
from dimmer import Dimmer

pygame.init()




WIDTH = 672
HEIGHT = 512
"Window 672 x 512"
windowSurface = pygame.display.set_mode((WIDTH,HEIGHT))
x = WIDTH / 2
y = HEIGHT / 2
# new_position = (x,y)

player = Player((x,y))
playerGroup = pygame.sprite.RenderPlain(player)
HUB = HUB()

level_maker = Levels()

rocks_by_level = level_maker.createLevels_Rock()
doors_by_level = level_maker.createLevels_Door()
enemies_by_level = level_maker.createLevels_enemies(windowSurface)
level_background = level_maker.drawBackground(windowSurface)
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
    
    for y in range(nrows):
    	for x in range(ncols):
    		background_rect.topleft = (x * background_rect.width, y* background_rect.height)
    		windowSurface.blit(level_background[y][x], background_rect)
    levelChange = pygame.sprite.spritecollide(player, doors_by_level[current_level],True)
    
    if levelChange:
        current_level = 1
        Dimmer().dim()
        time.sleep(.1)
        level_background = level_maker.drawBackground(windowSurface)
        player.getBelt()

    player.update_position(rocks_by_level[current_level], playerGroup, enemies_by_level[current_level])
    playerGroup.draw(windowSurface)
    enemies_by_level[current_level].update(player, rocks_by_level[current_level])
    enemies_by_level[current_level].draw(windowSurface)    
    doors_by_level[current_level].draw(windowSurface)
    rocks_by_level[current_level].draw(windowSurface)
    HUB.drawHealth(player, windowSurface)
    
    pygame.display.update()
    fpsClock.tick(30)
    
