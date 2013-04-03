import os, pygame, sys, helpers
from pygame.locals import *
from attack import *
from dialogHandle import *

class Companion(pygame.sprite.Sprite):

    
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
    	self.left_still = pygame.image.load('../images/comp_left_still.png')
    	self.left_walk = pygame.image.load('../images/comp_left_walk.png')
    	self.left_walk2 = pygame.image.load('../images/comp_left_walk2.png')
    	self.right_still = pygame.image.load('../images/comp_right_still.png')
    	self.right_walk = pygame.image.load('../images/comp_right_walk.png')
    	self.right_walk2 = pygame.image.load('../images/comp_right_walk2.png')
    	self.front_still = pygame.image.load('../images/comp_front_still.png')
    	self.front_walk = pygame.image.load('../images/comp_front_walk.png')
    	self.front_walk2 = pygame.image.load('../images/comp_front_walk2.png')
    	self.back_still = pygame.image.load('../images/comp_back_still.png')
    	self.back_walk = pygame.image.load('../images/comp_back_walk.png')
    	self.back_walk2 = pygame.image.load('../images/comp_back_walk2.png')
    	self.image = self.front_still
    	self.rect = self.image.get_rect()
    	self.windowSurface = pygame.display.get_surface()
    	self.walking = 0
    	self.walking_timer = 0
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
    	self.alive = True
    	self.attack_group = pygame.sprite.RenderPlain()
    	self.lazor_group = pygame.sprite.RenderPlain()
    	self.weapon = 1 #one is for bow, 0 is sword
    	self.defensive = False #is he running up to attack whoever or trying to defend player.
    	self.cool_down = 0
    	self.dialogHandle = HandleDialog(self.windowSurface, DialogBox((440, 51), (255, 255, 204), 
             (102, 0, 0), pygame.font.SysFont('Verdana', 15)))
    	self.dialogHandle.companionOpening(self.windowSurface, self)
    	self.sway = 0
    	self.collide = False
    	self.back_track_timer = 0
    	self.click_target = position


    def startUp(self, weapon, defensive): #called by dialog menu thing
    	self.weapon = weapon
    	if defensive == 0:
    	   self.defensive = False
    	else:
    	   self.defensive = True
    def startAlive(self, alive):
        self.alive = alive
    def isAlive(self):
        return self.alive
    """
    checks what weapon is carried, does things based off that
    """ 	
    def update(self, player, rocks, enemyGroup):
    	old_position = self.rect.topleft
    	if len(enemyGroup) > 0:
    	
			if self.weapon == 1:
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
            if helpers.distance(self.rect.topleft, player.rect.topleft) > 6                            :
			    self.__chase(player.rect.topleft, rocks, player)
			    if self.walking_timer <=0:
			     self.__walk(player)
			     self.walking_timer = 5
			    else:
			     self.walking_timer -= 1		
    	if not self.__check_collision(rocks, player, old_position):
          self.blocked_direction = "nope" 
          self.collide = True
    	self.rect.topleft = helpers.checkBoundry(self.rect.topleft)
    	
    
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
		target = enemy[0]
		print len(enemy)
		for x in range(len(enemy)):
		    if helpers.distance(self.rect.topleft, enemy[x].rect.topleft) < helpers.distance(self.rect.topleft, target.rect.topleft):
		        target = enemy[x]
		        
		
		
		if helpers.distance(self.rect.topleft, player.rect.topleft) < 10:
			    self.__chase(target.rect.topleft, rocks, target)
			    if self.walking_timer <=0:
			     self.__walk(target)
			     self.walking_timer = 5
			    else:
			     self.walking_timer -= 1
		elif helpers.distance(self.rect.topleft,player.rect.topleft) > 9 and helpers.distance(self.rect.topleft,player.rect.topleft) < 11:
				i = 1
		else:
		        self.__chase(player.rect.topleft, rocks, player)
		        if self.walking_timer <=0:
			     self.__walk(player)
			     self.walking_timer = 5
		        else:
			     self.walking_timer -= 1
		if helpers.distance(self.rect.topleft, target.rect.topleft) < 5 and self.collide == False:		
		    self.attacking = True
		    self.attack_group.add(self.attack)
		else:
			self.collide = True
		if self.attacking:
		    self.attack.use(self, self.follow_direction)
		if self.attack.is_done():
		    self.attacking = False
		    self.attack.kill()
		hit_enemy = pygame.sprite.spritecollide(target, self.attack_group, False)
		if hit_enemy:
		    target.get_hit("none", 1)
		self.attack_group.update()
		self.attack_group.draw(self.windowSurface)   

    
    """
    This is aggressive sword fighting. The goal is basically to be like an enemy and just run
    in an attack another bad guy.
    MIGHT make it so that he attacks the ones farther from the player
    """    
    def swordFightA(self, player, rocks, enemyGroup):
        enemy = enemyGroup.sprites()
        target = enemy[0]
        for x in range(len(enemy)):
		    if helpers.distance(self.rect.topleft, enemy[x].rect.topleft) < helpers.distance(self.rect.topleft, target.rect.topleft):
		        target = enemy[x]
		       
        
        
        if self.clock == 0:
            self.__chase(target.rect.topleft, rocks, target)
            if self.walking_timer <=0:
			     self.__walk(target)
			     self.walking_timer = 5
            else:
			     self.walking_timer -= 1
        if helpers.distance(self.rect.topleft, target.rect.topleft) < 5 and self.cool_down <= 0:
            self.attacking = True
            self.attack_group.add(self.attack)
            self.cool_down = 50
        elif self.cool_down > 0:
        	self.cool_down -=1
        if self.attacking:
		    self.attack.use(self, self.follow_direction)
    	if self.attack.is_done():
	    	self.attacking = False
	    	self.attack.kill()
        hit_enemy = pygame.sprite.spritecollide(target, self.attack_group, False)
        if hit_enemy:
               target.get_hit("none", 1)
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
    	
    def __chase(self, spot, rocks, target):
        old_position = self.rect.topleft
        my_x = self.rect.topleft[0]
        my_y = self.rect.topleft[1]
        self.follow_direction = helpers.checkOrient(target, self)
        lazor_sight = Lazor(self.rect.center, spot)
        self.lazor_group.add(lazor_sight)
        self.lazor_group.add(Lazor(self.rect.topleft, spot))
        self.lazor_group.update()
        self.lazor_group.draw(pygame.display.get_surface())
        first_shot = self.lazor_group.sprites()
        if len(first_shot) > 50:
        	self.lazor_group.empty()
        lazor_rock = pygame.sprite.groupcollide(self.lazor_group, rocks, False, False)
        if lazor_rock:
            for rock in pygame.sprite.groupcollide(self.lazor_group, rocks, True, False).keys():
				if self.back_track_timer == 0:
					if self.follow_direction == "up":
						self.click_target = (my_x - 50, my_y -25)
					elif self.follow_direction == "down":
						self.click_target = (my_x + 50, my_y +25)
					elif self.follow_direction == "right":
						self.click_target = (my_x +25, my_y +50)
					else:
						self.click_target = (my_x -25, my_y -50)
					self.back_track_timer = 40
				   
        if self.back_track_timer > 0:
            spot = self.click_target
            self.back_track_timer -=1
            
        x = spot[0]
        y = spot[1]
        """
        working right here to make the enemy move out of the straight chase line of chasing player
        """
		
        if helpers.distance(spot, self.rect.topleft) > 10 and not self.defensive and not lazor_rock:
			if self.sway > 0:			
			   y -= self.sway *2
			   if x < my_x +30 and x > my_x -30:
			       x -= self.sway *2  
			if self.sway > 30:
			   self.sway -= 80
			else:
			   y += self.sway *4
			   if x < my_x +30 and x > my_x -30:
			       x -= self.sway *4    
			self.sway +=1
		
		

        if x+10 > self.rect.topleft[0] and not self.blocked_direction == "left":
			#self.follow_direction = "right"
			my_x += 2
			if not self.blocked_direction == "nope":
			   my_x += 2
        if x-10 < self.rect.topleft[0]and not self.blocked_direction == "right":
			#self.follow_direction = "left"
			my_x -= 2
			if not self.blocked_direction == "nope":
			   my_x -= 2
        if y+10 > self.rect.topleft[1]and not self.blocked_direction == "down":
			#self.follow_direction = "down"
			my_y += 2
			if not self.blocked_direction == "nope":
			   my_y += 2
        if y-10 < self.rect.topleft[1]and not self.blocked_direction == "up":
			#self.follow_direction = "up"
			my_y -= 2
			if not self.blocked_direction == "nope":
			   my_y -= 2
        """
		also working right here to make the enemy move out of the straight chase line of chasing player
		"""
		
        self.rect.topleft = helpers.checkBoundry((my_x, my_y))
        if self.rect.topleft == old_position:
        	direction = helpers.checkOrient(target, self)
        	if direction == "down":
        		my_y +=4
        	elif direction == "up":
        		my_y -=4
        	elif direction == "right":
        		my_x +=4
        	else: 
        		my_x -=4
        	self.rect.topleft = helpers.checkBoundry((my_x, my_y))
        self.position = self.rect.topleft
		
    def __face(self, player):
       direction = helpers.checkOrient(player, self)
       if direction == "down":
            self.image = self.front_still
       if direction == "up":
			self.image = self.back_still              
       if direction == "right":
            self.image = self.right_still
       if direction == "left":
        	self.image = self.left_still
       self.follow_direction = direction
        	
    def __walk(self, player):
       if self.walking == 0:
          if self.image == self.front_still:
             self.image = self.front_walk
             self.walking = 1
          elif self.image == self.left_still:
             self.image = self.left_walk
             self.walking = 1
          elif self.image == self.back_still:
             self.image = self.back_walk
             self.walking = 1
          elif self.image == self.right_still:
             self.image = self.right_walk
             self.walking = 1
          else:
             self.walking = 1
       elif self.walking == 2:
    	  if self.image == self.front_still:
             self.image = self.front_walk2
             self.walking = -1
          elif self.image == self.left_still:
             self.image = self.left_walk2
             self.walking = -1
          elif self.image == self.back_still:
             self.image = self.back_walk2
             self.walking = -1
          elif self.image == self.right_still:
             self.image = self.right_walk2
             self.walking = -1
          else:
             self.walking = -1
       else:
		self.__face(player)
		self.walking += 1

class DownedComp(pygame.sprite.Sprite):

    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
    	self.image = pygame.image.load('../images/comp_down.png')
    	self.rect = self.image.get_rect()
    	self.rect.topleft = (600,100)
    	self.shown = True
    	
    def showUp(self, windowSurface):
        if self.shown:
           windowSurface.blit(self.image ,(600, 100))
    def leave(self):
        self.shown = False