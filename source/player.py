import os, pygame, sys
from pygame.locals import *

class Player(pygame.sprite.Sprite):
    
    
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
    	self.image = pygame.image.load('../images/hero_placeholder.png')
    	self.rect = self.image.get_rect()
    	self.position = position
    	self.rect.topleft = position[0], position[1]
    	self.has_belt = False
	self.attacking = False
    	
    def update_position(self, rocks, attack):
    	keys = pygame.key.get_pressed()
    	x = self.rect.topleft[0]
    	y = self.rect.topleft[1]
    	old_position = self.rect.topleft
    	direction = "still"
	
    	if keys[K_LEFT] and not self.attacking:
        	x -= 10
        	direction = "left"
        	if x <= 0:
        		x = 0
    	if keys[K_RIGHT] and not self.attacking:
        	x += 10
        	direction = "right"
        	if x >= 643:
        		x = 643        
    	if keys[K_DOWN] and not self.attacking:
        	y += 10
        	direction = "down"
        	if y >= 468:
        		y = 468
    	if keys[K_UP] and not self.attacking:
        	y -= 10
        	direction = "up"
        	if y <= 0:
        		y = 0
	if keys[K_SPACE] and not self.attacking:
	    self.attacking = True
	    
    	self.rect.topleft = x, y
	
	if self.attacking:
	    attack.attack(self)
	if attack.is_done():
	    self.attacking = False
	
    	hit_rock = pygame.sprite.spritecollide(self, rocks, False)
    	
    	if hit_rock:
    		self.rect.topleft = old_position[0], old_position[1]
    		if self.has_belt:
<<<<<<< HEAD
    			if keys[K_RSHIFT]:
    				hit_rock[0].getMoved(rocks, direction)
=======
    		    if keys[K_RSHIFT]:
			hit_rock[0].getMoved(rocks, direction)
>>>>>>> Attack Animiation (Kinda)
    			
    def getBelt(self):
    	self.has_belt = True