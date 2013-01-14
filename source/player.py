import os, pygame, sys
from pygame.locals import *

class Player(pygame.sprite.Sprite):
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
    	self.image = pygame.image.load('../images/hero_placeholder.png')
    	self.rect = self.image.get_rect()
    	self.position = position
    	self.rect.topleft = position[0], position[1]
    	
    def update_position(self, rocks):
    	keys = pygame.key.get_pressed()
    	x = self.rect.topleft[0]
    	y = self.rect.topleft[1]
    	old_position = self.rect.topleft
    	if keys[K_LEFT]:
        	x -= 10
        	if x <= 0:
        		x = 0
    	if keys[K_RIGHT]:
        	x += 10
        	if x >= 643:
        		x = 643        
    	if keys[K_DOWN]:
        	y += 10
        	if y >= 468:
        		y = 468
    	if keys[K_UP]:
        	y -= 10
        	if y <= 0:
        		y = 0
     
    	self.rect.topleft = x, y
    	hit_rock = pygame.sprite.spritecollide(self, rocks, False)
    	
    	if hit_rock:
    		self.rect.topleft = old_position[0], old_position[1]