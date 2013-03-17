import os, pygame, sys, helpers
from pygame.locals import *
from attack import *
from companion import Companion
from dialogHandle import *

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
    	self.hasFriend = False
    	self.companion_group = pygame.sprite.RenderPlain()
    	self.dialogbox = DialogBox((440, 51), (255, 255, 204), 
             (102, 0, 0), pygame.font.SysFont('Verdana', 15))
        self.dialog_handle = HandleDialog(screen, self.dialogbox)
        #these are for bow attacks
        self.weapon = 0 #0 for sword, 1 for bow
        self.aiming = False
        self.targetX = 0
        self.targetY = 0
        self.target_main = False
        self.attack_group = pygame.sprite.RenderPlain()
        self.lazor_group = pygame.sprite.RenderPlain()
        self.lazor_sight = False
    	
    def update_position(self, rocks, playerGroup, enemyGroup, plates):
		keys = pygame.key.get_pressed()
		x = self.rect.topleft[0]
		y = self.rect.topleft[1]
		interact_flag = False
		old_position = self.rect.topleft
		if keys[K_a] and not self.attacking and self.alive:
			
			if not self.aiming:
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
			else:
				if not self.direction == "right":
				    self.targetX -= 2
		if keys[K_d] and not self.attacking:
			
			if not self.aiming:
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
			else:
				if not self.direction == "left":
				    self.targetX += 2
		if keys[K_s] and not self.attacking:
			
			if not self.aiming:
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
			else:
				if not self.direction == "up":
				    self.targetY += 2
				
		if keys[K_w] and not self.attacking and self.alive:
			
			if not self.aiming:
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
			else:
				if not self.direction == "down":
				    self.targetY -= 2
		
		if keys[K_q] and self.weapon == 1 and self.alive:
		    self.aiming=True
		    self.targetX = self.rect.center[0]
		    self.targetY = self.rect.center[1]
		    self.lazor_sight = True
		    self.main_target = True
		lazor_sight = PlayerTarget(self.rect.center)    
		if self.lazor_sight == True:
		    lazor_sight.move((self.targetX, self.targetY), self.screen)
		
		
		if keys[K_SPACE] and not self.attacking:
	
			if self.weapon == 0:
			   self.attacking = True
			   playerGroup.add(self.attack)
			else:
			    if self.aiming==True:
			       self.aiming = False
			       attack = R_Attack(self.rect.center, (self.targetX, self.targetY), self.direction)
			       self.attack_group.add(attack)
			       self.target_main = False
			       self.lazor_sight = False
			       self.lazor_group.empty()
			       print self.targetX, self.targetY
		
		
		if keys[K_RSHIFT]:
			interact_flag = True	
		#These two keys are simply for testing (position finding and spawning comp)
		if keys[K_p]:
			print self.rect.topleft
		if keys[K_v]:
			if self.hasFriend == False:
			   self.hasFriend = True
			   friend = Companion((self.position[0] +10, self.position[1]))
			   if friend.isAlive():
				   self.companion_group.add(friend)
		if keys[K_b]:
		    self.getBow()
		
		
		if self.hasFriend == True:
			self.companion_group.update(self, rocks, enemyGroup)
			self.companion_group.draw(self.screen)
		
		
		if self.health < 0:
			self.alive = False
		self.rect.topleft = x, y
		self.position = self.rect.topleft	
		if self.attacking:
			self.attack.use(self, self.direction)
		if self.attack.is_done():
			self.attacking = False
			self.attack.kill()
			
		
		self.attack_group.update()
		self.attack_group.draw(self.screen)
		
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
		
		if not plates == "1":
			hit_plate = pygame.sprite.spritecollide(self, plates, False)
			if hit_plate:
				if interact_flag:
					self.dialog_handle.examinePlate(self.screen)
		
			
		hit_rock = pygame.sprite.spritecollide(self, rocks, False)
		if hit_rock:
			if interact_flag:
				self.dialog_handle.examineRock(self.screen, hit_rock[0].ID)
			
			self.rect.topleft = old_position[0], old_position[1]
			if self.has_belt and self.push_timer <= 0:
				if keys[K_LSHIFT]:
					hit_rock[0].getMovedP(rocks, self.momentum, self, enemyGroup)
					self.push_timer = 8 #to make rocks move slower
				if keys[K_TAB]:
					hit_rock[0].getHit()
					self.push_timer = 8	
				if keys[K_p]:
					print "Oi, dis rock at ", hit_rock[0].rect.topleft
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
           self.rect.topleft = helpers.checkBoundry(self.old_position)
           self.health -= damage
           self.invul = 80
        self.position = self.rect.topleft
    	if self.health < 0:
			self.alive = False
        
    def startRoom(self, spot):
    	self.rect.topleft = spot[0], spot[1]
    	self.position = self.rect.topleft
    	if self.hasFriend:
    	    self.companion_group.sprites()[0].rect.topleft = spot
    def backUp(self):
    	if self.direction == "left":
    	    self.rect.topleft = self.rect.topleft[0] +5, self.rect.topleft[1]
    	if self.direction == "right":
    	    self.rect.topleft = self.rect.topleft[0] -5, self.rect.topleft[1]
    	if self.direction == "up":
    	    self.rect.topleft = self.rect.topleft[0] , self.rect.topleft[1] +5
    	if self.direction == "down":
    	    self.rect.topleft = self.rect.topleft[0], self.rect.topleft[1] -5
    	    
    def getFriend(self):
        if self.hasFriend == False:
			   self.hasFriend = True
			   friend = Companion((self.position[0] +10, self.position[1]))
			   if friend.isAlive():
				   self.companion_group.add(friend)
    
    def getBow(self):
    	self.weapon = 1
    
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
		  
		  
class PlayerTarget(pygame.sprite.Sprite):

    
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
    	self.image = pygame.image.load('../images/lazor.png')
    	self.rect = self.image.get_rect()
    	self.rect.topleft = position
    def move(self, position, screen):
        self.rect.topleft = position
        screen.blit(self.image, position)
    	