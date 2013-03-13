import os, pygame, sys, helpers, math
from pygame.locals import *
from math import *
from attack import *
from random import randint

"This is the melee enemy. They patrol and when the player is close they attack"
class M_Enemy(pygame.sprite.Sprite):


 def __init__(self, position, id):
       pygame.sprite.Sprite.__init__(self)
       if id == 1:
         self.front_still = pygame.image.load('../images/arms_front_still.png')
         self.image = self.front_still
         self.front_walk = pygame.image.load('../images/arms_front_walk.png')
         self.front_walk2 = pygame.image.load('../images/arms_front_walk2.png')
         self.left_walk = pygame.image.load('../images/arms_left_walk.png')
         self.left_still = pygame.image.load('../images/arms_left_still.png')
         self.left_walk2 = self.left_walk
         self.back_still = pygame.image.load('../images/arms_back_still.png')
         self.back_walk = pygame.image.load('../images/arms_back_walk.png')
         self.back_walk2 = pygame.image.load('../images/arms_back_walk2.png')
         self.right_still = pygame.image.load('../images/arms_right_still.png')
         self.right_walk = pygame.image.load('../images/arms_right_walk.png')
         self.right_walk2 = self.right_walk
       else:
         self.front_still = pygame.image.load('../images/headless_front_still.png')
         self.image = self.front_still
         self.front_walk = pygame.image.load('../images/headless_front_walk.png')
         self.front_walk2 = pygame.image.load('../images/headless_front_walk2.png')
         self.left_walk = pygame.image.load('../images/headless_left_walk.png')
         self.left_walk2 = pygame.image.load('../images/headless_left_walk2.png')
         self.left_still = pygame.image.load('../images/headless_left_still.png')
         self.back_still = pygame.image.load('../images/headless_back_still.png')
         self.back_walk = pygame.image.load('../images/headless_back_walk.png')
         self.back_walk2 = pygame.image.load('../images/headless_back_walk2.png')
         self.right_still = pygame.image.load('../images/headless_right_still.png')
         self.right_walk = pygame.image.load('../images/headless_right_walk.png')
         self.right_walk2 = pygame.image.load('../images/headless_right_walk2.png')   
       self.rect = self.image.get_rect()
       self.position = position
       self.rect.topleft = position[0], position[1]
       self.health = 1 #FOR TESTING
       self.clock = 0
       self.follow = False
       self.pat_directions = ["right", "down", "left", "up"]
       self.pat_index = 0
       self.follow_direction = "right"
       self.pat_counter = 0;
       self.walking = 0
       self.walking_timer = 0
       self.blocked_direction = "nope"

 def update(self, player, rocks):
    	
       distance = abs(helpers.distance(player.rect.topleft, self.rect.topleft))
       old_position = self.rect.topleft
       """
		Above checks the distance from enemy to player, according to that,
		the enemy either chases directly or patrols
		"""      
       if distance < 15:
              self.follow = True
       else:
              self.follow = False
       if self.follow:
            if self.clock == 0:
			  self.__chase(player.rect.topleft)
			  if self.walking_timer <=0:
			     self.__walk(player)
			     self.walking_timer = 5
			  else:
			     self.walking_timer -= 1
            else:
               self.clock -= 1
       else:
              self.__patrol()
       
       if not self.__check_collision(rocks, player, old_position):
          self.blocked_direction = "nope" 
       
 """
    Knocks the enemy back after a hit, because that makes sense.
 """
 def get_hit(self, direction, damage):
       self.health -= damage
       self.clock = 15
       knocked_position = (0,0)
       if direction == "right":
               knocked_position = self.position[0] + 40, self.position[1]
       elif direction == "left":
               knocked_position = self.position[0] - 40, self.position[1]
       elif direction == "down":
               knocked_position = self.position[0], self.position[1] +40
       elif direction == "up":
               knocked_position = self.position[0], self.position[1] -40
       if self.health <= 0:
               self.kill()
       self.rect.topleft = helpers.checkBoundry(knocked_position)
       self.position = self.rect.topleft
        
 """
    Patrol for this enemy is COMPLETELY RANDOM. That is because this enemy is
    to look dumb. The large middle part changes the picture to be the correct direction
    and also to walk.
    Including all of that in here might not have been the smartest, but the other method
    does its thing by checking the orientation in comparison to player
    
    TODO: Maybe clean this to use another method? Maybe its best to leave it.
    Commit before trying anything
 """              
 def __patrol(self):
       x = self.rect.topleft[0]
       y = self.rect.topleft[1]
       
       self.pat_counter += 1
       
       if self.pat_counter >= 41:
              self.pat_index = randint(0,3)
              self.pat_counter = 0
       
       direction = self.pat_directions[self.pat_index]
       
       patrol_position = (0,0)
       if direction == "right":
        patrol_position = x + 2, y
        if self.walking_timer <=0:
           self.walking_timer = 10
           if self.walking == 0:
              self.image = self.right_walk
              self.walking = 1
           elif self.walking == 2:
              self.image = self.right_walk2
              self.walking = -1
           else:
              self.image = self.right_still
              self.walking +=1
        else:
           self.walking_timer -= 1
              
       elif direction == "left":
        patrol_position = x - 2, y
        if self.walking_timer <=0:
           self.walking_timer = 10
           if self.walking == 0:
              self.image = self.left_walk
              self.walking = 1
           elif self.walking == 2:
              self.image = self.left_walk2
              self.walking = -1
           else:
              self.image = self.left_still
              self.walking +=1
        else:
           self.walking_timer -= 1
       elif direction == "up":
          patrol_position = x, y - 2
          if self.walking_timer <=0:
             self.walking_timer = 10
             if self.walking == 0:
                self.image = self.back_walk
                self.walking = 1
             elif self.walking == 2:
              self.image = self.back_walk2
              self.walking = -1
             else:
                self.image = self.back_still
                self.walking += 1
          else:
             self.walking_timer -= 1
       elif direction == "down":
          patrol_position = x, y + 2
          if self.walking_timer <=0:
             self.walking_timer = 10
             if self.walking == 0:
                self.image = self.front_walk
                self.walking = 1
             elif self.walking == 2:
              self.image = self.front_walk2
              self.walking = -1
             else:
                self.image = self.front_still
                self.walking +=1
          else:
             self.walking_timer -= 1
       self.rect.topleft = helpers.checkBoundry(patrol_position)

 """
    All collision with enemy is checked here.
    
    TODO: add a collision with two rocks, result in death
 """
       
 def __check_collision(self, rocks, player, old_position):
       
       hit_rock = pygame.sprite.spritecollide(self, rocks, False)
       if hit_rock:         
              self.rect.topleft = old_position[0], old_position[1]
              self.position = self.rect.topleft
              self.blocked_direction = self.follow_direction
              return True
       hit_player = pygame.sprite.collide_rect(self, player)
       if hit_player:
              player.getHit(self.follow_direction, 2)
              self.clock = 15
              
 def __chase(self, spot):
	x = spot[0]
	y = spot[1]
	my_x = self.rect.topleft[0]
	my_y = self.rect.topleft[1]
	"""
	working right here to make the enemy move out of the straight chase line of chasing player
	"""
	
	if (y < self.rect.topleft[1] +50 and y > self.rect.topleft[1] - 50) and ((self.blocked_direction == "left") or (self.blocked_direction == "right")):
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

 """
    The following two methods handle keeping the sprite facing the player and walking
    in accordance to its current image
 """
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




"This is the ranged enemy, they are stationary and just shoot"       


class R_Enemy(pygame.sprite.Sprite):


 def __init__(self, position, windowSurface):
    	pygame.sprite.Sprite.__init__(self)
    	self.face_left = pygame.image.load('../images/legless_left.png')
    	self.face_up = pygame.image.load('../images/legless_back.png')
    	self.face_right = pygame.image.load('../images/legless_right.png')
    	self.face_down = pygame.image.load('../images/legless_front.png')
    	self.image = self.face_left
    	self.rect = self.image.get_rect()
    	self.position = position
    	self.rect.topleft = position[0], position[1]
    	self.health = 1 #for 1 shot testing
    	self.clock = 0
    	self.follow_direction = "right"
    	self.attack_group = pygame.sprite.RenderPlain()
    	self.windowSurface = windowSurface
    	self.cool_down = 0
    	
    	
 def update(self, player, rocks):
       old_position = self.rect.topleft
       x = player.rect.topleft[0]
       y = player.rect.topleft[1]
       if self.clock == 0:
               if self.cool_down == 0:
                       attack = R_Attack(self.rect.center, player.rect.center, helpers.checkOrient(player, self))
                       self.attack_group.add(attack)
                       self.cool_down = 80
               else:
                       self.cool_down -= 1
       else:
               self.clock -= 1
       self.attack_group.update()
       self.attack_group.draw(self.windowSurface)

       self.__face(player)
       
       hit_player = pygame.sprite.spritecollide(player, self.attack_group, False)
       if hit_player:
               player.getHit("none", 1)
               hit_player[0].kill()
       self.__check_collision(rocks, player, old_position)

 def get_hit(self, direction, damage):
       self.health -= damage
       self.clock = 15
       if direction == "right":
               self.rect.topleft = self.position[0] + 40, self.position[1]
       elif direction == "left":
               self.rect.topleft = self.position[0] - 40, self.position[1]
       elif direction == "down":
               self.rect.topleft = self.position[0], self.position[1] +40
       elif direction == "up":
               self.rect.topleft = self.position[0], self.position[1] -40
       if self.health <= 0:
               self.kill()
       self.position = self.rect.topleft
 """
    All collision with enemy is checked here.
    
    TODO: add a collision with two rocks, result in death
 """
       
 def __check_collision(self, rocks, player, old_position):
       
       hit_rock = pygame.sprite.spritecollide(self, rocks, False)
       if hit_rock:         
              self.get_hit(player.direction, 10)
       hit_player = pygame.sprite.collide_rect(self, player)
       if hit_player:
              #player.getHit(self.follow_direction)
              self.clock = 15
 """
 This method makes the turret ranger follow the player around the room
 by looking at him
 """             
 def __face(self, player):
       direction = helpers.checkOrient(player, self)
       if direction == "down":
            self.image = self.face_down
       if direction == "up":
			self.image = self.face_up       
       
       if direction == "right":
            self.image = self.face_right
       if direction == "left":
        	self.image = self.face_left