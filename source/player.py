import os, pygame, sys
from pygame.locals import *
from attack import Attack

class Player(pygame.sprite.Sprite):

    
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
    	self.image = pygame.image.load('../images/hero_placeholder.png')
    	self.rect = self.image.get_rect()
    	self.position = position
    	self.rect.topleft = position[0], position[1]
    	self.has_belt = False
    	self.attacking = False
    	self.attack = Attack()
    	self.clock = 0
    	self.direction = "up"
    	
    def update_position(self, rocks, playerGroup, enemyGroup):
		keys = pygame.key.get_pressed()
		x = self.rect.topleft[0]
		y = self.rect.topleft[1]
		old_position = self.rect.topleft
		if keys[K_LEFT] and not self.attacking:
			x -= 10
			self.direction = "left"
			if x <= 0:
				x = 0
		if keys[K_RIGHT] and not self.attacking:
			x += 10
			self.direction = "right"
			if x >= 643:
				x = 643
		if keys[K_DOWN] and not self.attacking:
			y += 10
			self.direction = "down"
			if y >= 468:
				y = 468
				
		if keys[K_UP] and not self.attacking:
			y -= 10
			self.direction = "up"
			if y <= 0:
				y = 0
		if keys[K_SPACE] and not self.attacking:
			self.attacking = True
			playerGroup.add(self.attack)
		
		
		self.rect.topleft = x, y
			
		if self.attacking:
			self.attack.use(self)
		if self.attack.is_done():
			self.attacking = False
			self.attack.kill()
			
		hit_enemy = pygame.sprite.spritecollide(self.attack, enemyGroup, False)
		if hit_enemy:
			if self.clock == 0:
				hit_enemy[0].get_hit(self.direction)
				self.clock = 30
		else:
			if self.clock > 0:
				self.clock -= 1
			
		hit_rock = pygame.sprite.spritecollide(self, rocks, False)
		if hit_rock:
			self.rect.topleft = old_position[0], old_position[1]
			if self.has_belt:
				if keys[K_RSHIFT]:
					hit_rock[0].getMoved(rocks, self.direction)

    def getBelt(self):
    	self.has_belt = True