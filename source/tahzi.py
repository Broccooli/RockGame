import os, pygame, sys, helpers, math
from pygame.locals import *
from math import *
from attack import *
from random import randint

class TahZi(pygame.sprite.Sprite):

   def __init__(self):
      pygame.sprite.Sprite.__init__(self)
      self.rock_tops = [((320, 240)), ((55, 240)), ((400, 310)), 
		((240, 170)), ((120, 240)), ((205, 240)), ((250, 170)), ((510, 240)),
		((320, 140)), ((320, 55)), ((400, 170)), ((425, 240)), ((575, 240)), 
		((245, 310)), ((320, 360)),((320, 445))]
		
      self.image = pygame.image.load('../images/hero_placeholder_left.png')
      self.rect = self.image.get_rect()
      self.rect.topleft = ((320, 240))
      self.stranded = 0 
      """Stranded, if 0 then hes on a rock. If 1 he is transitioning, if 2 then he is on the floor   """
      self.stun_timer = 0
      self.next_rock = ((320, 240))
      
      #This is going just for test run
      self.move_period = 0
	  
   def update(self, player, rocks):
      if self.stun_timer <= 0 and self.stranded == 2:
         self.next_rock = self.rock_tops[randint(0,15)]
         self.stranded = 1
      if self.stranded== 1:
         self.__runAway()
      if self.stun_timer > 0:
         self.stun_timer -=1  
         
      if self.move_period < 150:
         self.move_period += 1
      else:
         self.move_period = 0
         self.stranded = 2
         self.stun_timer = 10
         
   def __runAway(self):
      x = self.next_rock[0]
      y = self.next_rock[1]
      my_y = self.rect.topleft[1]
      my_x = self.rect.topleft[0]
      if self.rect.topleft == self.next_rock:
         self.stranded = 0
      else:
         if x+10 > self.rect.topleft[0]:
		    my_x += 6
         if x-10 < self.rect.topleft[0]:
		    my_x -= 6
         if y+10 > self.rect.topleft[1]:
		    my_y += 6
         if y-10 < self.rect.topleft[1]:
		    my_y -= 6
         self.rect.topleft = (my_x, my_y)