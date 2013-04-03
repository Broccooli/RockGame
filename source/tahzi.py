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
      self.front_still = pygame.image.load('../images/tahzi_front_stillNG.png')
      self.front_walk = pygame.image.load('../images/tahzi_front_walk.png')
      self.front_walk2 = pygame.image.load('../images/tahzi_front_walk2.png')
      self.left_walk = pygame.image.load('../images/tahzi_left_walk.png')
      self.left_walk2 = pygame.image.load('../images/tahzi_left_walk2.png')
      self.left_still = pygame.image.load('../images/tahzi_left_stillNG.png')
      self.back_still = pygame.image.load('../images/tahzi_back_stillNG.png')
      self.back_walk = pygame.image.load('../images/tahzi_back_walk.png')
      self.back_walk2 = pygame.image.load('../images/tahzi_back_walk2.png')
      self.right_still = pygame.image.load('../images/tahzi_right_stillNG.png')
      self.right_walk = pygame.image.load('../images/tahzi_right_walk.png')
      self.right_walk2 = pygame.image.load('../images/tahzi_right_walk2.png')
      self.right_still_gun = pygame.image.load('../images/tahzi_right_still.png')
      self.left_still_gun = pygame.image.load('../images/tahzi_left_still.png')
      self.front_still_gun = pygame.image.load('../images/tahzi_front_still.png')
      self.back_still_gun = pygame.image.load('../images/tahzi_back_still.png')  
      self.image = self.front_still_gun
      self.rect = self.image.get_rect()
      self.direction = "down"
      self.rect.topleft = ((320, 240))
      self.stranded = 0 
      """Stranded, if 0 then hes on a rock. If 1 he is transitioning, if 2 then he is on the floor   """
      self.stun_timer = 0
      self.next_rock = ((320, 240))
      self.cool_down = 1
      #This is going just for test run
      self.move_period = 0
      self.screen = pygame.display.get_surface()
      self.attack_group = pygame.sprite.RenderPlain()
      self.crack_group = pygame.sprite.RenderPlain(WallCrack())
      self.current_rock = None
      self.health = 5
      self.position = self.rect.topleft
      self.walking = 0
      
	  
	  
   def update(self, player, rocks):
      #cover that door up with our crack
      self.crack_group.draw(self.screen)
      
      #if stunned, take care of it
      if self.stun_timer > 0:
         self.stun_timer -=1  
      
      #after having hit the ground, stunned, wait till stun is over and then run away
      if self.stun_timer <= 0 and self.stranded == 2:
         self.next_rock = self.rock_tops[randint(0,15)]
         self.stranded = 1
      #just found a target rock, run to it
      if self.stranded== 1:
         self.__runAway(rocks, player)

	  #what rocks are we on
      hit_rock = pygame.sprite.spritecollide(self, rocks, False)
      #define the current rock we're on and get on it
      if hit_rock:
         self.current_rock = hit_rock[0]
         hit_rock[0].getOn()
      if not self.current_rock == None:
         if self.current_rock.isShaken():
            self.rect.topleft = self.position[0] + 40, self.position[1]
            self.position = self.rect.topleft  
            self.stun_timer = 45
            self.stranded = 2
            hit_rock[0].stable()
      	    hit_rock[0].getOff()
      	    self.current_rock = None
      #If perched on a rock, shoot
      if self.stranded == 0:
         self.__face(player)
         if self.cool_down == 0:
            attack = R_Attack(self.rect.center, player.rect.center, helpers.checkOrient(player, self))
            self.attack_group.add(attack)
            self.cool_down = 80
         else:
            self.cool_down -= 1
      self.attack_group.update()
      self.attack_group.draw(self.screen)
      
      
      hit_player = pygame.sprite.spritecollide(player, self.attack_group, False)
      if hit_player:
        player.getHit("none", 1)
        hit_player[0].kill()
   """   
      if self.move_period < 150:
         self.move_period += 1
      else:
         self.move_period = 0
         self.stranded = 2
         self.stun_timer = 10
   """   
   def __runAway(self, rocks, player):
      x = self.next_rock[0]
      y = self.next_rock[1]
      my_y = self.rect.topleft[1]
      my_x = self.rect.topleft[0]
      if abs(self.rect.topleft[0] - self.next_rock[0]) < 8 and abs(self.rect.topleft[1] - self.next_rock[1]) <8 :
         self.stranded = 0
         hit_rock = pygame.sprite.spritecollide(self, rocks, False)
         hit_rock[0].getOn()
         self.__face(player)
         if self.direction == "up":
             self.image = self.back_still_gun
         if self.direction == "down":
             self.image = self.front_still_gun
         if self.direction == "left":
             self.image = self.left_still_gun
         if self.direction == "right":
             self.image = self.right_still_gun
      else:
         self.__walk(player)
         if x+5 > self.rect.topleft[0]:
		    my_x += 6
         if x-5 < self.rect.topleft[0]:
		    my_x -= 6
         if y+5 > self.rect.topleft[1]:
		    my_y += 6
         if y-5 < self.rect.topleft[1]:
		    my_y -= 6
         self.rect.topleft = (my_x, my_y)
      self.position = self.rect.topleft  
   
   def get_hit(self, direction, damage):
       if self.stranded == 2:
          self.health -= damage
          self.stranded = 1
          if direction == "right":
               self.rect.topleft = self.position[0] + 40, self.position[1]
          elif direction == "left":
               self.rect.topleft = self.position[0] - 40, self.position[1]
          elif direction == "down":
               self.rect.topleft = self.position[0], self.position[1] +40
          elif direction == "up":
               self.rect.topleft = self.position[0], self.position[1] -40
          self.stun_timer = 0
       if self.health <= 0:
               self.kill()
       self.position = self.rect.topleft
   """
    This method makes the turret ranger follow the player around the room
     by looking at him
   """             
   def __face(self, player):
       self.direction = helpers.checkOrient(player, self)
       if self.direction == "down":
			self.image = self.front_still_gun
       if self.direction == "up":
			self.image = self.back_still_gun       
	   
       if self.direction == "right":
			self.image = self.right_still_gun
       if self.direction == "left":
			self.image = self.left_still_gun
# 		   
#        else:	   
# 		   if self.direction == "down":
# 				self.image = self.face_down
# 		   if self.direction == "up":
# 				self.image = self.face_up       
# 		   
# 		   if self.direction == "right":
# 				self.image = self.face_right
# 		   if self.direction == "left":
# 				self.image = self.face_left

        	
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
		  self.walking += 1
		  if self.image == self.front_walk2 or self.image == self.front_walk:
		      self.image = self.front_still
		  elif self.image == self.left_walk2 or self.image == self.left_walk:
		      self.image = self.left_still
		  elif self.image == self.back_walk2 or self.image == self.back_walk:
		      self.image = self.back_still
		  elif self.image == self.right_walk2 or self.image == self.right_walk:
		      self.image = self.right_still


"""
This is to cover a door up. Shaking the room so much causes it to break and then bam, new room
"""       
class WallCrack(pygame.sprite.Sprite):

   def __init__(self):
      pygame.sprite.Sprite.__init__(self)
      self.image = pygame.image.load('../images/hero_placeholder_left.png')
      self.rect = self.image.get_rect()
      self.rect.topleft = ((640, 50))