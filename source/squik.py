import os, pygame, sys, helpers, math
from pygame.locals import *
from math import *
from attack import *
from rocks import Rock
from enemy import M_Enemy

class Squik(pygame.sprite.Sprite):

   def __init__(self):
      pygame.sprite.Sprite.__init__(self)
      self.position = (300, 270)
      self.left = pygame.image.load('../images/hero_placeholder_left.png')
      self.right = pygame.image.load('../images/hero_placeholder_right.png')
      self.down = pygame.image.load('../images/hero_placeholder_down.png')
      self.up = pygame.image.load('../images/hero_placeholder.png')
      self.image = self.up
      self.rect = self.image.get_rect()
      self.player = pygame.sprite.RenderPlain()
      self.gel = 50
      self.handle_hit = 0 
      self.hit_rock_timer = 100
      self.stuck = True
      self.vulnerable = False
      self.touched_rocks = pygame.sprite.RenderPlain(Rock((0, 0)), Rock ((0, -1)))
      self.knocked_position = self.position
      self.rocks = pygame.sprite.RenderPlain()
      self.wake = False
   
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
             hit_rock[0].kill()
          self.stuck = False
      	  self.hit_rock_timer = 100
   
   
   
   def __chase(self, player):
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
       
      hit_rock = pygame.sprite.spritecollide(self, rocks, False)
      if hit_rock:
         self.rect.topleft = old_position[0], old_position[1]
         self.position = self.rect.topleft
         self.stuck = True
         self.touched_rocks.add(hit_rock)
      hit_player = pygame.sprite.collide_rect(self, player)
      if hit_player:
         player.getHit(helpers.checkOrient(player,self), 2)
   
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
   
   
   def get_hit(self, direction, damage):
      if self.vulnerable == True:
         self.gel -= damage
         print self.gel
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