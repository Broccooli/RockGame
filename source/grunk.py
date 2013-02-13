import os, pygame, sys, helpers, math
from pygame.locals import *
from math import *
from attack import *

class Grunk(pygame.sprite.Sprite):

   def __init__(self):
      pygame.sprite.Sprite.__init__(self)
      self.position = (325, 50)
      self.left = pygame.image.load('../images/hero_placeholder_left.png')
      self.right = pygame.image.load('../images/hero_placeholder_right.png')
      self.down = pygame.image.load('../images/hero_placeholder_down.png')
      self.up = pygame.image.load('../images/hero_placeholder.png')
      self.image = self.up
      self.rect = self.image.get_rect()
      self.stun_timer = 0
      self.attacking = False
      self.follow_direction = "down"
      self.old_position = self.position
      self.rect.center = self.position[0], self.position[1]
      self.to_be_moved_rock = 0
      self.health = 5
      self.hit_distance = 5
    	
   def update(self, player, rocks):
      self.old_position = self.rect.center
      if self.stun_timer == 0:
         self.__spin()
         self.__chase(player)
         self.__check_collision(rocks, player, self.old_position)
      else:
         self.stun_timer -= 1
         if self.hit_distance >0 and not self.to_be_moved_rock == 0:
            self.to_be_moved_rock.getMoved(rocks, self.follow_direction, player)
            self.hit_distance -=1
      
   
   
   def __spin(self):
      if self.image == self.left:
         self.image = self.up
      elif self.image == self.up:
         self.image = self.right
      elif self.image == self.right:
         self.image = self.down
      else:
         self.image = self.left


   def __check_collision(self, rocks, player, old_position):
       
      hit_rock = pygame.sprite.spritecollide(self, rocks, False)
      if hit_rock:
         self.rect.topleft = old_position[0], old_position[1]
         self.position = self.rect.topleft
         self.stun_timer = 60
         self.to_be_moved_rock = hit_rock[0]
         self.hit_distance = 15
      hit_player = pygame.sprite.collide_rect(self, player)
      if hit_player:
         player.getHit(self.follow_direction, 2)
         self.stun_timer = 15
   
   
   def __chase(self, player):
      x = player.rect.topleft[0]
      y = player.rect.topleft[1]
      my_x = self.rect.topleft[0]
      my_y = self.rect.topleft[1]
      if abs(my_x - x) >= abs(my_y- y):
         if x+2 > self.rect.topleft[0]:
            self.follow_direction = "right"
            my_x += 2
         if x-2 < self.rect.topleft[0]:
            self.follow_direction = "left"
            my_x -= 2
      else:
         if y+2 > self.rect.topleft[1]:
            self.follow_direction = "down"
            my_y += 2
         if y-2 < self.rect.topleft[1]:
            self.follow_direction = "up"
            my_y -= 2
      self.rect.topleft = helpers.checkBoundry((my_x, my_y))
      self.position = self.rect.topleft 
      
      
   def get_hit(self, direction, damage):
      if self.stun_timer > 0:
         self.health -= damage
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