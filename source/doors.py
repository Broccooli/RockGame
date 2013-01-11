import os, pygame, sys
from pygame.locals import *

class Door(pygame.sprite.Sprite):
    def _init_(self):
        pygame.sprite.Sprite._init_(self)
    image = pygame.image.load('../images/door.png')
    rect = image.get_rect()
    rect.topleft = [5,5]