import os, pygame, sys, helpers
from pygame.locals import *
from attack import Attack

class Player(pygame.sprite.Sprite):

    
    def __init__(self, position, screen):
        pygame.sprite.Sprite.__init__(self)
    	self.left_still = pygame.image.load('../images/hero_left_still.png')
    	self.left_walk1 = pygame.image.load('../images/hero_left_walk1.png')
    	self.left_walk2 = pygame.image.load('../images/hero_left_walk2.png')
    	self.right_still = pygame.image.load('../images/hero_right_still.png')
    	self.right_walk1 = pygame.image.load('../images/hero_right_walk1.png')
    	self.right_walk2 = pygame.image.load('../images/hero_right_walk2.png')
    	self.down_still = pygame.image.load('../images/hero_front_still.png')
    	self.down_walk1 = pygame.image.load('../images/hero_front_walk1.png')
    	self.down_walk2 = pygame.image.load('../images/hero_front_walk2.png')
    	self.up_still = pygame.image.load('../images/hero_back_still.png')
    	self.up_walk1 = pygame.image.load('../images/hero_back_walk1.png')
    	self.up_walk2 = pygame.image.load('../images/hero_back_walk2.png')
    	self.image = self.left_still
    	self.rect = self.image.get_rect()
    	self.position = position
    	self.rect.topleft = position[0], position[1]
    	self.alive = True
    	self.has_belt = False
    	self.has_gaunt = False
    	self.attacking = False
    	self.attack = Attack()
    	self.clock = 0
    	self.direction = "left"
    	self.health = 5
    	self.invul = 0 #typical invulnerable period
    	self.screen = screen
    	self.push_timer = 0 #slows rocks down
    	self.momentum = "up" #makes sure rocks only move in a singular direction
    	self.old_position = position
    	self.walking = 1
    	self.walking_timer = 0
    	
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
		if self.walking_timer <=0:
			self.__walk()
			self.walking_timer = 5
		else:
			self.walking_timer -= 1
		if x <= 15:
			x = 15
	if keys[K_RIGHT] and not self.attacking:
		x += 5
		self.direction = "right"
		if self.push_timer == 0:
			self.momentum = self.direction
		if self.walking_timer <=0:
			self.__walk()
			self.walking_timer = 5
		else:
			self.walking_timer -= 1
		if x >= 620:
			x = 620
	if keys[K_DOWN] and not self.attacking:
		y += 5
		self.direction = "down"
		if self.push_timer == 0:
			self.momentum = self.direction
		if self.walking_timer <=0:
			self.__walk()
			self.walking_timer = 5
		else:
			self.walking_timer -= 1
		if y >= 460:
			y = 460
			
	if keys[K_UP] and not self.attacking and self.alive:
		y -= 5
		self.direction = "up"
		if self.push_timer == 0:
			self.momentum = self.direction
		if self.walking_timer <=0:
			self.__walk()
			self.walking_timer = 5
		else:
			self.walking_timer -= 1
		if y <= 15:
			y = 15
	if keys[K_SPACE] and not self.attacking:

		self.attacking = True
		playerGroup.add(self.attack)
	if keys[K_p]:
		print self.rect.topleft
	
	if self.health < 0:
		self.kill()
		self.alive = False
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
			hit_enemy[0].get_hit(self.direction, 2)
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
			if keys[K_TAB]:
			    hit_rock[0].getHit()
			    self.push_timer = 8	
	if self.invul > 0:
		self.invul -= 1

    def getBelt(self): #belt will be dropped by first boss, allows pushing rocks
    	self.has_belt = True
    	
    def getHealth(self):
    	return str(self.health)
    def getGaunt(self): #for breaking rocks, dropped by squik
        self.has_gaunt = True	
    def getHit(self, direction, damage):
    	helpers.shake(self.screen, 40)
    	self.old_position = self.rect.topleft
    	if self.invul == 0:
           if direction == "right":
              self.old_position = self.position[0] + 40, self.position[1]
           elif direction == "left":
              self.old_position = self.position[0] - 40, self.position[1]
           elif direction == "down":
              self.old_position = self.position[0], self.position[1] +40
           elif direction == "up":
              self.old_position = self.position[0], self.position[1] -40
           if self.health <= 0:
              self.kill()
           self.rect.topleft = helpers.checkBoundry(self.old_position)
           self.health -= damage
           self.invul = 80
        self.position = self.rect.topleft
    	if self.health < 0:
			self.kill()
			self.alive = False
        
    def startRoom(self, spot):
    	self.rect.topleft = spot[0], spot[1]
    	self.position = self.rect.topleft
    def backUp(self):
    	if self.direction == "left":
    	    self.rect.topleft = self.rect.topleft[0] +5, self.rect.topleft[1]
    	if self.direction == "right":
    	    self.rect.topleft = self.rect.topleft[0] -5, self.rect.topleft[1]
    	if self.direction == "up":
    	    self.rect.topleft = self.rect.topleft[0] , self.rect.topleft[1] +5
    	if self.direction == "down":
    	    self.rect.topleft = self.rect.topleft[0], self.rect.topleft[1] -5
    	    
    def __walk(self):
       if self.walking == 0:
          if self.image == self.down_still:
             self.image = self.down_walk1
             self.walking = 1
          elif self.image == self.left_still:
             self.image = self.left_walk1
             self.walking = 1
          elif self.image == self.up_still:
             self.image = self.up_walk1
             self.walking = 1
          elif self.image == self.right_still:
             self.image = self.right_walk1
             self.walking = 1
          else:
             self.walking = 1
       elif self.walking == 2:
    	  if self.image == self.down_still:
             self.image = self.down_walk2
             self.walking = -1
          elif self.image == self.left_still:
             self.image = self.left_walk2
             self.walking = -1
          elif self.image == self.up_still:
             self.image = self.up_walk2
             self.walking = -1
          elif self.image == self.right_still:
             self.image = self.right_walk2
             self.walking = -1
          else:
             self.walking = -1
       else:
		  if self.direction == "left":
		     self.image = self.left_still
		  if self.direction == "right":
		     self.image = self.right_still
		  if self.direction == "up":
		     self.image = self.up_still
		  if self.direction == "down":
		     self.image = self.down_still
		  self.walking += 1