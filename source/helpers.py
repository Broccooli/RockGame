import os, pygame, sys, math
from pygame.locals import *

def distance(player, enemy):
    distance = math.sqrt( (abs(player[0] - enemy[0])) + (abs(player[1] - enemy[1])) )
    return distance
    
