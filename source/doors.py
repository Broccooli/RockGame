import os, pygame, sys
from pygame.locals import *

class Door(pygame.sprite.Sprite):
    def __init__(self, position, locked):
        pygame.sprite.Sprite.__init__(self)
        if locked:
			if position[0] == 0:
			    self.image = pygame.image.load('../images/leftdoorL.png')
			if position[0] == 640:
			    self.image = pygame.image.load('../images/rightdoorL.png')
			if position[1] == 0:
			    self.image = pygame.image.load('../images/doorL.png')
			if position[1] == 480:
			    self.image = pygame.image.load('../images/bottomdoorL.png')
    	else:
    	    if position[0] == 0:
    	        self.image = pygame.image.load('../images/leftdoor.png')
    	    if position[0] == 640:
    	        self.image = pygame.image.load('../images/rightdoor.png')
    	    if position[1] == 0:
    	        self.image = pygame.image.load('../images/door.png')
    	    if position[1] == 480:
    	        self.image = pygame.image.load('../images/bottomdoor.png')
    	self.rect = self.image.get_rect()
    	self.rect.topleft = position[0], position [1]
    def unlock(self):
        if self.rect.topleft[0] == 0:
    	    self.image = pygame.image.load('../images/leftdoor.png')
    	if self.rect.topleft[0] == 640:
    	    self.image = pygame.image.load('../images/rightdoor.png')
    	if self.rect.topleft[1] == 0:
    	    self.image = pygame.image.load('../images/door.png')
    	if self.rect.topleft[1] == 480:
    	    self.image = pygame.image.load('../images/bottomdoor.png')