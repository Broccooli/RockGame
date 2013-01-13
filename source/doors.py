import os, pygame, sys
from pygame.locals import *

class Door(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
    	self.image = pygame.image.load('../images/door.png')
    	self.rect = self.image.get_rect()
    	self.rect.topleft = [5,5]