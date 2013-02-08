import os, pygame, sys, helpers
from pygame.locals import *
from attack import Attack

class Player(pygame.sprite.Sprite):

    
    def __init__(self, position, screen):
        pygame.sprite.Sprite.__init__(self)
    	self.left = pygame.image.load('../images/hero_placeholder_left.png')
    	self.right = pygame.image.load('../images/hero_placeholder_right.png')
    	self.down = pygame.image.load('../images/hero_placeholder_down.png')
    	self.up = pygame.image.load('../images/hero_placeholder.png')
    	self.image = self.up
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
    	self.screen = screen
    	self.push_timer = 0 #slows rocks down
    	self.momentum = "up" #makes sure rocks only move in a singular direction
    	
    def update_position(self, rocks, playerGroup, enemyGroup):
	keys = pygame.key.get_pressed()
	x = self.rect.topleft[0]
	y = self.rect.topleft[1]
	old_position = self.rect.topleft
	if keys[K_LEFT] and not self.attacking and self.alive:
		x -= 5
		self.direction = "left"
		if self.push_timer == 0:
			self.momentum = self.direction
		self.image = self.left
		if x <= 15:
			x = 15
	if keys[K_RIGHT] and not self.attacking:
		x += 5
		self.direction = "right"
		if self.push_timer == 0:
			self.momentum = self.direction
		self.image = self.right
		if x >= 620:
			x = 620
	if keys[K_DOWN] and not self.attacking:
		y += 5
		self.direction = "down"
		if self.push_timer == 0:
			self.momentum = self.direction
		self.image = self.down
		if y >= 460:
			y = 460
			
	if keys[K_UP] and not self.attacking and self.alive:
		y -= 5
		self.direction = "up"
		if self.push_timer == 0:
			self.momentum = self.direction
		self.image = self.up
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
	if self.push_timer > 0:
		self.push_timer -=1
	
		
	hit_rock = pygame.sprite.spritecollide(self, rocks, False)
	if hit_rock:
		self.rect.topleft = old_position[0], old_position[1]
		if self.has_belt and self.push_timer <= 0:
			if keys[K_LSHIFT]:
				hit_rock[0].getMovedP(rocks, self.momentum, self, enemyGroup)
				self.push_timer = 8 #to make rocks move slower
				
	if self.invul > 0:
		self.invul -= 1

    def getBelt(self): #belt will be dropped by first boss, allows pushing rocks
    	self.has_belt = True
    	
    def getHealth(self):
    	return str(self.health)
    	
    def getHit(self, move_direction):
    	self.health -= 1
    	helpers.shake(self.screen, 40)
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
        
    def startRoom(self, spot):
    	self.rect.topleft = spot[0], spot[1]
    	self.position = self.rect.topleft