import os, pygame, sys, helpers, math
from pygame.locals import *

class PressurePlate(pygame.sprite.Sprite):


 def __init__(self, position):
       pygame.sprite.Sprite.__init__(self)
       self.image = pygame.image.load('../images/plate.png')
       self.rect = self.image.get_rect()
       self.rect.center = position[0], position[1]
       
 def locked(self, rocks):
       collide = pygame.sprite.spritecollide(self, rocks, False) 
       if collide:
          return True
       else:
          return False  