import os, pygame, sys, helpers
from pygame.locals import *
from attack import Attack

class Player(pygame.sprite.Sprite):

    
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
    	self.image = pygame.image.load('../images/hero_placeholder.png')
    	self.rect = self.image.get_rect()
    	self.position = position
    	self.rect.topleft = position[0], position[1]
	self.alive = True
    	self.has_belt = False
    	self.attacking = False
    	self.attack = Attack()
    	self.clock = 0
    	self.direction = "up"
    	self.health = 5
    	self.invul = 0 #typical invulnerable period
    	
    def update_position(self, rocks, playerGroup, enemyGroup):
	keys = pygame.key.get_pressed()
	x = self.rect.topleft[0]
	y = self.rect.topleft[1]
	old_position = self.rect.topleft
	if keys[K_LEFT] and not self.attacking and self.alive:
		x -= 5
		self.direction = "left"
		self.image = pygame.image.load('../images/hero_placeholder_left.png')

		if x <= 0:
			x = 0
	if keys[K_RIGHT] and not self.attacking and self.alive:
		x += 5
		self.direction = "right"
		self.image = pygame.image.load('../images/hero_placeholder_right.png')
		if x >= 643:
			x = 643
	if keys[K_DOWN] and not self.attacking and self.alive:

		if x <= 15:
			x = 15
	if keys[K_RIGHT] and not self.attacking:
		x += 5
		self.direction = "right"
		self.image = pygame.image.load('../images/hero_placeholder_right.png')
		if x >= 620:
			x = 620
	if keys[K_DOWN] and not self.attacking:

		y += 5
		self.direction = "down"
		self.image = pygame.image.load('../images/hero_placeholder_down.png')
		if y >= 460:
			y = 460
			
	if keys[K_UP] and not self.attacking and self.alive:
		y -= 5
		self.direction = "up"
		self.image = pygame.image.load('../images/hero_placeholder.png')

		if y <= 0:
			y = 0
	if keys[K_SPACE] and not self.attacking and self.alive:

		if y <= 15:
			y = 15
	if keys[K_SPACE] and not self.attacking:

		self.attacking = True
		playerGroup.add(self.attack)
	
	
	self.rect.topleft = x, y
	self.position = self.rect.topleft	
	if self.attacking:
		self.attack.use(self, self.direction)
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
			if keys[K_LSHIFT]:
				hit_rock[0].getMoved(rocks, self.direction)
				
	if self.invul > 0:
		self.invul -= 1

    def getBelt(self):
    	self.has_belt = True
    	
    def getHealth(self):
    	return str(self.health)
    	
    def getHit(self, move_direction):
    	self.health -= 1
    	if self.invul == 0:
    	 if move_direction == "right":
    		self.rect.topleft = self.position[0] + 40, self.position[1]
    	 elif move_direction == "left":
    		self.rect.topleft = self.position[0] - 40, self.position[1]
    	 elif move_direction == "down":
    		self.rect.topleft = self.position[0], self.position[1] +40
    	 elif move_direction == "up":
    		self.rect.topleft = self.position[0], self.position[1] -40
    	 
    	 self.position = self.rect.topleft
    	 if self.health < 0:
			self.kill()
			self.alive = False;
        self.invul = 15