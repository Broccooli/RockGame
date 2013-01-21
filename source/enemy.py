import os, pygame, sys
from pygame.locals import *
from attack import Attack

class Enemy(pygame.sprite.Sprite):


 def __init__(self, position):
    	pygame.sprite.Sprite.__init__(self)
    	self.image = pygame.image.load('../images/mad.png')
    	self.rect = self.image.get_rect()
    	self.position = position
    	self.rect.topleft = position[0], position[1]
    	self.health = 3 #for 1 shot testing
    	self.clock = 0
    	self.follow_direction = "right"
    	
    	
 def update(self, player, rocks):
		if self.clock == 0:
			old_position = self.rect.topleft
			x = player.rect.topleft[0]
			y = player.rect.topleft[1]
			my_x = self.rect.topleft[0]
			my_y = self.rect.topleft[1]
			if x > self.rect.topleft[0]:
				self.follow_direction = "right"
				my_x += 2
			if x < self.rect.topleft[0]:
				self.follow_direction = "left"
				my_x -= 2
			if y > self.rect.topleft[1]:
				self.follow_direction = "down"
				my_y += 2
			if y < self.rect.topleft[1]:
				self.follow_direction = "up"
				my_y -= 2
			self.rect.topleft = my_x, my_y
		else:
			self.clock -= 1
		hit_rock = pygame.sprite.spritecollide(self, rocks, False)
		if hit_rock:
			self.rect.topleft = old_position[0], old_position[1]
		self.position = self.rect.topleft
		hit_player = pygame.sprite.collide_rect(self, player)
		if hit_player:
			player.getHit(self.follow_direction)
			self.clock = 15
			
 def get_hit(self, direction):
		self.health -= 1
		self.clock = 15
		if direction == "right":
			self.rect.topleft = self.position[0] + 40, self.position[1]
		elif direction == "left":
			self.rect.topleft = self.position[0] - 40, self.position[1]
		elif direction == "down":
			self.rect.topleft = self.position[0], self.position[1] +40
		elif direction == "up":
			self.rect.topleft = self.position[0], self.position[1] -40
		if self.health == 0:
			self.kill()