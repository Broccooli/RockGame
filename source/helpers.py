import os, pygame, sys, math, random
from pygame.locals import *
from dimmer import Dimmer

dimmer = Dimmer()

"""
I LOVE THIS THEROM TOO MUCH TO NOT MAKE IT A METHOD
""" 

def distance(player, enemy):
    distance = math.sqrt( (abs(player[0] - enemy[0])) + (abs(player[1] - enemy[1])) )
    return distance


"""
Used for enemies to face the player
"""    
   
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
"""
Shakes for damage or if a boss is big and stompy
""" 		
		
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
    
"""
Makes sure no ones going through any walls
"""     
    
def checkBoundry(position):
	new_x = position[0]
	new_y = position[1]
	if position[0] <= 15:
		new_x = 15
	if position [0] >= 600:
		new_x = 600
	if position [1] <= 15:
		new_y = 15
	if position[1] >= 430:
		new_y = 430
	return (new_x, new_y)
	
def pauseBalls(windowSurface): #by going up stairs, pauseballs, by going down stairs
    paused = True
    dimmer.dim()
    while (paused == True):
       for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit(0) # Clicking the x now closes the game, not ESC
        if event.type ==KEYUP:
        	if event.key == K_TAB:
        	   paused = False
    dimmer.undim()    