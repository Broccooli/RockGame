import os, pygame, sys
from pygame.locals import *

class Rock(pygame.sprite.Sprite):
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
    	self.image = pygame.image.load('../images/rock.png')
    	self.rect = self.image.get_rect()
    	self.rect.topleft = position[0], position [1]