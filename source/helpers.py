import os, pygame, sys, math
from pygame.locals import *

def distance(player, enemy):
    distance = math.sqrt( (abs(player.rect.topleft[0] - enemy.rect.topleft[0])) + (abs(player.rect.topleft[1] - enemy.rect.topleft[1])) )
    return distance