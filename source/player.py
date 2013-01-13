import os, pygame, sys
from pygame.locals import *

class Player(pygame.sprite.Sprite):
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
    	self.image = pygame.image.load('../images/hero_placeholder.png')
    	self.rect = self.image.get_rect()
    	self.position = position
    	self.rect.topleft = position[0], position[1]
    	
    def update_position(self, position):
    	self.rect.topleft = position[0], position[1]