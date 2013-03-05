import os, pygame, sys, helpers
from pygame.locals import *
from attack import *

class Companion(pygame.sprite.Sprite):

    
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
    	self.image = pygame.image.load('../images/hero_left_still.png')
    	self.rect = self.image.get_rect()
    	self.windowSurface = pygame.display.get_surface()
    	self.position = position
    	self.rect.topleft = position[0], position[1]
    	self.alive = True
    	self.attacking = False
    	self.attack = Attack()
    	self.clock = 0
    	self.direction = "left"
    	self.follow_direction = "right"
    	self.blocked_direction = "nope"
    	self.health = 5
    	self.invul = 0 #typical invulnerable period
    	self.stun_timer = 0
    	self.old_position = position
    	self.attack_group = pygame.sprite.RenderPlain()
    	self.lazor_group = pygame.sprite.RenderPlain()
    	self.weapon = 1 #one is for sword, 0 is for bow
    	self.defensive = False #is he running up to attack whoever or trying to defend player.
    	self.cool_down = 0

    def startUp(self, weapon, defensive): #called by dialog menu thing
    	self. weapon = weapon
    	self.defensive = defensive
    """
    checks what weapon is carried, does things based off that
    """ 	
    def update(self, player, rocks, enemyGroup):
    	old_position = self.rect.topleft
    	if len(enemyGroup) > 0:
    	
			if self.weapon == 0:
				if self.defensive == True:
					self.bowFightD(player, rocks, enemyGroup)
				else:
					self.bowFightA(player, rocks, enemyGroup)
			else:
				if self.defensive == True:
					self.swordFightD(player, rocks, enemyGroup)
				else:
					self.swordFightA(player, rocks, enemyGroup)
        else:
           # print helpers.distance(self.rect.topleft, player.rect.topleft)
            if helpers.distance(self.rect.topleft, player.rect.topleft) > 6:
			    self.__chase(player.rect.topleft)		
    	self.rect.topleft = helpers.checkBoundry(self.rect.topleft)
    	if not self.__check_collision(rocks, player, old_position):
          self.blocked_direction = "nope" 
    
    """
    This is aggressive bow fighting, only difference is if the player is in the way
    This one will strafe and shoot
    """
    
    def bowFightA(self, player, rocks, enemyGroup): 
        enemy = enemyGroup.sprites()
        lazor_sight = Lazor(self.rect.center, enemy[0].rect.center)
        self.lazor_group.add(lazor_sight)
        self.lazor_group.update()
        lazor_player = pygame.sprite.spritecollide(player, self.lazor_group, False)
        if lazor_player: #STRAFE
            if self.clock > 0:
                self.clock -= 1
            if self.cool_down >0:
                self.cool_down -=1 
            position = self.rect.topleft[1]
            position += 2
            self.rect.topleft = self.rect.topleft[0], position
        if self.clock == 0:
            if self.cool_down == 0:
                attack = R_Attack(self.rect.center, enemy[0].rect.center, self.direction)
                self.attack_group.add(attack)
                self.cool_down = 80
            else:
                self.cool_down -= 1
        else:
            self.clock -= 1
            
            
        hit_player = pygame.sprite.spritecollide(player, self.attack_group, False)
        if hit_player:
               player.getHit("none", 1)
               hit_player[0].kill()
        
        hit_enemy = pygame.sprite.spritecollide(enemy[0], self.attack_group, False)
        if hit_enemy:
               enemy[0].get_hit("none", 1)
               hit_enemy[0].kill()
        
        self.attack_group.update()
        self.attack_group.draw(self.windowSurface)
     

    """
    This is defensive bow fighting, only difference is if the player is in the way
    This one will hold and wait for the player to move
    """
    def bowFightD(self, player, rocks, enemyGroup):
        enemy = enemyGroup.sprites()
        lazor_sight = Lazor(self.rect.center, enemy[0].rect.center)
        self.lazor_group.add(lazor_sight)
        self.lazor_group.update()
        lazor_player = pygame.sprite.spritecollide(player, self.lazor_group, False)
        if lazor_player:
            if self.clock > 0:
                self.clock -= 1
            if self.cool_down >0:
                self.cool_down -=1 
            
        else:
         if self.clock == 0:
            if self.cool_down == 0:
                attack = R_Attack(self.rect.center, enemy[0].rect.center, self.direction)
                self.attack_group.add(attack)
                self.cool_down = 80
            else:
                self.cool_down -= 1
         else:
            self.clock -= 1
        
        hit_player = pygame.sprite.spritecollide(player, self.attack_group, False)
        if hit_player:
               player.getHit("none", 1)
               hit_player[0].kill()
        
        hit_enemy = pygame.sprite.spritecollide(enemy[0], self.attack_group, False)
        if hit_enemy:
               enemy[0].get_hit("none", 1)
               hit_enemy[0].kill()
        
        self.attack_group.update()
        self.attack_group.draw(self.windowSurface)

    """
    This is defensive sword fighting. The goal is to stay between the player and the enemy
    """
    
    def swordFightD(self, player, rocks, enemyGroup):
		enemy = enemyGroup.sprites()
		if helpers.distance(self.rect.topleft, player.rect.topleft) < 10:
			    self.__chase(enemy[0].rect.topleft)
		elif helpers.distance(self.rect.topleft,player.rect.topleft) > 9 and helpers.distance(self.rect.topleft,player.rect.topleft) < 11:
				i = 1
		else:
		        self.__chase(player.rect.topleft)
		if helpers.distance(self.rect.topleft, enemy[0].rect.topleft) < 10:		
		    self.attacking = True
		    self.attack_group.add(self.attack)
		if self.attacking:
		    self.attack.use(self, self.direction)
		if self.attack.is_done():
		    self.attacking = False
		    self.attack.kill()
		hit_enemy = pygame.sprite.spritecollide(enemy[0], self.attack_group, False)
		if hit_enemy:
		    enemy[0].get_hit("none", 1)
		self.attack_group.update()
		self.attack_group.draw(self.windowSurface)   

    
    """
    This is aggressive sword fighting. The goal is basically to be like an enemy and just run
    in an attack another bad guy.
    MIGHT make it so that he attacks the ones farther from the player
    """    
    def swordFightA(self, player, rocks, enemyGroup):
        enemy = enemyGroup.sprites()
        if self.clock == 0:
            self.__chase(enemy[0].rect.topleft)
        if helpers.distance(self.rect.topleft, enemy[0].rect.topleft) < 10:
            self.attacking = True
            self.attack_group.add(self.attack)
        if self.attacking:
		    self.attack.use(self, self.direction)
    	if self.attack.is_done():
	    	self.attacking = False
	    	self.attack.kill()
        hit_enemy = pygame.sprite.spritecollide(enemy[0], self.attack_group, False)
        if hit_enemy:
               enemy[0].get_hit("none", 1)
        self.attack_group.update()
        self.attack_group.draw(self.windowSurface)    
        
        
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
			
    def __check_collision(self, rocks, player, old_position):
       
       hit_rock = pygame.sprite.spritecollide(self, rocks, False)
       if hit_rock:         
              self.rect.topleft = old_position[0], old_position[1]
              self.position = self.rect.topleft
              self.blocked_direction = self.follow_direction
              return True
    	
    def __chase(self, spot):
		x = spot[0]
		y = spot[1]
		my_x = self.rect.topleft[0]
		my_y = self.rect.topleft[1]
		"""
		working right here to make the enemy move out of the straight chase line of chasing player
		"""
		
		if (y < self.rect.topleft[1] +50 and y > self.rect.topleft[1] - 50) and ((self.blocked_direction == "left") or (self.blocked_direction == "right")):
			print "here"
			self.__chase((spot[0], spot[1]+ 20))
		if x == self.rect.topleft[0] and ((self.blocked_direction == "up") or (self.blocked_direction == "down")):
			self.__patrol()
		
		
		if x+10 > self.rect.topleft[0] and not self.blocked_direction == "right":
			self.follow_direction = "right"
			my_x += 2
			if not self.blocked_direction == "nope":
			   my_x += 2
		if x-10 < self.rect.topleft[0]and not self.blocked_direction == "left":
			self.follow_direction = "left"
			my_x -= 2
			if not self.blocked_direction == "nope":
			   my_x -= 2
		if y+10 > self.rect.topleft[1]and not self.blocked_direction == "down":
			self.follow_direction = "down"
			my_y += 2
			if not self.blocked_direction == "nope":
			   my_y += 2
		if y-10 < self.rect.topleft[1]and not self.blocked_direction == "up":
			self.follow_direction = "up"
			my_y -= 2
			if not self.blocked_direction == "nope":
			   my_y -= 2
		"""
		also working right here to make the enemy move out of the straight chase line of chasing player
		"""
		
		self.rect.topleft = helpers.checkBoundry((my_x, my_y))
		self.position = self.rect.topleft      
