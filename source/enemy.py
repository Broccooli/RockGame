import os, pygame, sys, helpers, math
from pygame.locals import *
from math import *
from attack import *
from random import randint

"This is the melee enemy. They patrol and when the player is close they attack"
class M_Enemy(pygame.sprite.Sprite):


 def __init__(self, position):
       pygame.sprite.Sprite.__init__(self)
       self.image = pygame.image.load('../images/enemy1.png')
       self.rect = self.image.get_rect()
       self.position = position
       self.rect.topleft = position[0], position[1]
       self.health = 4
       self.clock = 0
       self.follow = False
       self.pat_directions = ["right", "down", "left", "up"]
       self.pat_index = 0
       self.follow_direction = "right"
       self.pat_counter = 0;

 def update(self, player, rocks):
       
       distance = abs(helpers.distance(player.rect.topleft, self.rect.topleft))
       old_position = self.rect.topleft
       
       if distance < 15:
              self.follow = True
       else:
              self.follow = False
              
       if self.follow:
              if self.clock == 0:
				 self.__chase(player)
              else:
                     self.clock -= 1
       else:
              self.__patrol()
       
       self.__check_collision(rocks, player, old_position)
       

 def get_hit(self, direction):
       self.health -= 1
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
       if self.health == 0:
               self.kill()
       self.rect.topleft = helpers.checkBoundry(knocked_position)
       self.position = self.rect.topleft
        
               
 def __patrol(self):
       x = self.rect.topleft[0]
       y = self.rect.topleft[1]
       
       self.pat_counter += 1
       
       if self.pat_counter >= 41:
              old = self.pat_index
              while (self.pat_index == old):
                     self.pat_index = randint(0,3)
              self.pat_counter = 0
       
       direction = self.pat_directions[self.pat_index]
       
       patrol_position = (0,0)
       if direction == "right":
              patrol_position = x + 2, y
       elif direction == "left":
              patrol_position = x - 2, y
       elif direction == "up":
              patrol_position = x, y - 2
       elif direction == "down":
              patrol_position = x, y + 2
       self.rect.topleft = helpers.checkBoundry(patrol_position)
       
 def __check_collision(self, rocks, player, old_position):
       
       hit_rock = pygame.sprite.spritecollide(self, rocks, False)
       if hit_rock:         
              self.rect.topleft = old_position[0], old_position[1]
              self.position = self.rect.topleft
       hit_player = pygame.sprite.collide_rect(self, player)
       if hit_player:
              player.getHit(self.follow_direction)
              self.clock = 15
              
 def __chase(self, player):
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
	self.rect.topleft = helpers.checkBoundry((my_x, my_y))
	self.position = self.rect.topleft       







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
    	self.health = 2 #for 1 shot testing
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
                       attack = R_Attack(self.rect.center, player.rect.center)
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
               player.getHit("none")
               hit_player[0].kill()
       self.__check_collision(rocks, player, old_position)

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
       self.position = self.rect.topleft
       
 def __check_collision(self, rocks, player, old_position):
       
       hit_rock = pygame.sprite.spritecollide(self, rocks, False)
       if hit_rock:         
              self.rect.topleft = old_position[0], old_position[1]
              self.position = self.rect.topleft
       hit_player = pygame.sprite.collide_rect(self, player)
       if hit_player:
              player.getHit(self.follow_direction)
              self.clock = 15
              
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