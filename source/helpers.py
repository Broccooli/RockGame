import os, pygame, sys, math
from pygame.locals import *

def distance(player, enemy):
    distance = math.sqrt( (abs(player[0] - enemy[0])) + (abs(player[1] - enemy[1])) )
    return distance
    
def checkOrient(player, enemy):
	pX = player.rect.topleft[0]
	pY = player.rect.topleft[1]
	eX = enemy.rect.topleft[0]
	eY = enemy.rect.topleft[1]
	if pX < eX:
		
		if -100 < (pX - eX) <100:
			if pY < eY:
				return "up"
			if pY > eY:
				return "down"
		return "left"
	if pX > eX:
		
		if -100 < (pX - eX) <100:
			if pY < eY:
				return "up"
			if pY > eY:
				return "down"
		return "right"