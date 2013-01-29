import os, pygame, sys, math, random
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
		
		
def shake(screen, amplitude):
    amplitude = min(amplitude -1, 100)
    nx = random.randint(-10,10)
    ny = random.randint(-10,10)
    nx *= amplitude/20.0
    ny *= amplitude/20.0
    screen.blit(screen, (nx,ny))
    return amplitude
    
    
def fadeOut(screen, amplitude):
    amplitude = min(amplitude-1, 100)
    surf = pygame.Surface(screen.get_size())
    surf.set_alpha(amplitude*10)
    screen.blit(surf, (0, 0))
    return amplitude