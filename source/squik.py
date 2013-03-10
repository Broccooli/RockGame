import os, pygame, sys, helpers, math
from pygame.locals import *
from math import *
from attack import *
from rocks import Rock
from enemy import M_Enemy

class Squik(pygame.sprite.Sprite):

   def __init__(self):
      pygame.sprite.Sprite.__init__(self)
      self.position = (290, 250)
      self.front_still = pygame.image.load('../images/squik_front_still.png')
      self.image = self.front_still
      self.front_walk = pygame.image.load('../images/squik_front_walk.png')
      self.front_walk2 = pygame.image.load('../images/squik_front_walk2.png')
      self.left_walk = pygame.image.load('../images/squik_left_walk.png')
      self.left_still = pygame.image.load('../images/squik_left_still.png')
      self.left_walk2 = self.left_walk
      self.right_still = pygame.image.load('../images/squik_right_still.png')
      self.right_walk = pygame.image.load('../images/squik_right_walk.png')
      self.right_walk2 = self.right_walk
      self.image = self.front_still
      self.rect = self.image.get_rect()
      self.player = pygame.sprite.RenderPlain()
      self.gel = 30
      self.handle_hit = 0 
      self.hit_rock_timer = 100
      self.stuck = True
      self.vulnerable = False
      self.touched_rocks = pygame.sprite.RenderPlain(Rock((0, 0)), Rock ((0, -1)))
      self.knocked_position = self.position
      self.rocks = pygame.sprite.RenderPlain()
      self.wake = False
      self.walking = 0
   
   def update(self, player, rocks):
      
      self.rocks = rocks
      self.old_position = self.rect.topleft
      self.__check_collision(rocks, player, self.old_position)
      if self.gel <= 0:
         my_group = self.groups()
         my_group[0].add(pygame.sprite.RenderPlain(M_Enemy(self.old_position, 2)))
         self.kill()
      if self.stuck == True and len(self.touched_rocks.sprites()) >1:
         self.vulnerable = True
      else:
         self.vulnerable = False
      if self.wake == True:
         if self.stuck == False:
            self.__chase(player)
            self.touched_rocks.empty()
         else:
            self.breakRock(rocks)
   
      
   def breakRock(self, rocks):
       if self.hit_rock_timer > 0:
          self.hit_rock_timer -=1   
       else:
          hit_rock = pygame.sprite.spritecollide(self, rocks, False)
          if hit_rock:
             helpers.shake(pygame.display.get_surface(), 100)
             hit_rock[0].kill()
          self.stuck = False
      	  self.hit_rock_timer = 100
   
   
   
   def __chase(self, player):
	self.__walk(player)
	x = player.rect.topleft[0]
	y = player.rect.topleft[1]
	my_x = self.rect.topleft[0]
	my_y = self.rect.topleft[1]
	if x+2 > self.rect.topleft[0]:
		self.follow_direction = "right"
		my_x += 2
	if x-2 < self.rect.topleft[0]:
		self.follow_direction = "left"
		my_x -= 2
	if y+2 > self.rect.topleft[1]:
		self.follow_direction = "down"
		my_y += 2
	if y-2 < self.rect.topleft[1]:
		self.follow_direction = "up"
		my_y -= 2
	
	self.rect.topleft = helpers.checkBoundry((my_x, my_y))
	self.position = self.rect.topleft 
   
   
   def __check_collision(self, rocks, player, old_position):
       
      hit_rock = pygame.sprite.spritecollide(self, rocks, False, pygame.sprite.collide_rect_ratio(.6))
      if hit_rock:
         self.rect.topleft = old_position[0], old_position[1]
         self.position = self.rect.topleft
         self.stuck = True
         self.touched_rocks.add(hit_rock)
      playerGroup = player.groups()
      hit_player = pygame.sprite.spritecollide(self, playerGroup[0], False, pygame.sprite.collide_rect_ratio(.6))
      if hit_player:
         player.getHit(helpers.checkOrient(player,self), 2)
   

   
   def get_hit(self, direction, damage):
      if self.vulnerable == True:
         self.gel -= damage
         #print self.gel
         if self.wake:
            self.breakRock(self.rocks)
         self.wake = True
         self.touched_rocks.empty()
      if len(self.touched_rocks.sprites()) < 2:
         if direction == "right":
            self.knocked_position = self.position[0] + 10, self.position[1]
         elif direction == "left":
            self.knocked_position = self.position[0] - 10, self.position[1]
         elif direction == "down":
            self.knocked_position = self.position[0], self.position[1] +10
         elif direction == "up":
            self.knocked_position = self.position[0], self.position[1] -10
      self.rect.topleft = helpers.checkBoundry(self.knocked_position)
      self.position = self.rect.topleft
         #might do a screen shake or some animation here
         
   def __face(self, player):
       direction = helpers.checkOrient(player, self)
       if direction == "down":
            self.image = self.front_still
       if direction == "up":
			self.image = self.front_still              
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
          elif self.image == self.right_still:
             self.image = self.right_walk2
             self.walking = -1
          else:
             self.walking = -1
	else:
		self.__face(player)
		self.walking += 1

