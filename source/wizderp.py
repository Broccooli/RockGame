import os, pygame, sys, helpers, math
from pygame.locals import *
from attack import *
from dialogHandle import *
from animation import Animation
class Wizderp(pygame.sprite.Sprite):


 def __init__(self, screen):
		pygame.sprite.Sprite.__init__(self)
		
		self.left_w = Animation( [pygame.image.load('../images/wiz_left_still.png'),
								  pygame.image.load('../images/wiz_left_walk1.png'),
								  pygame.image.load('../images/wiz_left_walk2.png')] )

		self.right_w = Animation( [pygame.image.load('../images/wiz_right_still.png'),
								   pygame.image.load('../images/wiz_right_walk1.png'),
								   pygame.image.load('../images/wiz_right_walk2.png')] )

		self.down_w = Animation( [pygame.image.load('../images/wiz_front_still.png'),
								  pygame.image.load('../images/wiz_front_walk1.png'),
								  pygame.image.load('../images/wiz_front_walk2.png')] )

		self.up_w = Animation( [pygame.image.load('../images/wiz_back_still.png'),
								pygame.image.load('../images/wiz_back_walk1.png'),
								pygame.image.load('../images/wiz_back_walk2.png')] )
								
		self.tele1 = pygame.image.load('../images/wiztele1.png')
		self.tele2 = pygame.image.load('../images/wiztele2.png')
		self.tele3 = pygame.image.load('../images/wiztele3.png')
		self.tele4 = pygame.image.load('../images/wiztele4.png')
		self.tele5 = pygame.image.load('../images/wiztele5.png')

		self.image = self.left_w.update()
		self.walking_timer = 0
		self.rect = self.image.get_rect()
		self.rect.topleft = 50, 80
		
		self.attack_group = pygame.sprite.RenderPlain()
		self.attack_timer = 2
		self.screen = screen
		
		
		self.immortal_timer = 2
		self.health = 5
		self.tele_spots = [(100, 50), (300, 100), (400, 200), (500, 50)]
		self.tele_loc = 0
		
		self.decided = False
		self.will_fight = True
		self.tele_done = True
		self.tele_tick = 1
		self.tele_wait = 0
		

 def update(self, player, rocks):
 	
 	if self.decided and self.tele_done:
		self.direction =  direction = helpers.checkOrient(player, self)
		if self.attack_timer <= 0:
			self.__loadShot(player)
			self.attack_timer = 130
		elif self.attack_timer <15:
			self.attack_timer -=1
			self.image = self.tele1
		else:
			self.__move(player)
			self.attack_timer -=1
		if self.immortal_timer > 0:
			self.immortal_timer -=1
			self.attack_timer -= 1
 	elif self.decided and (not self.tele_done):
 		self.__teleport()
 	
 	elif (not self.decided) and (helpers.distance(player.rect.topleft, self.rect.topleft) < 12):
 		self.__decide()
 	
 	self.attack_group.update(player, rocks)
 	self.attack_group.draw(self.screen)
 	hit_player = pygame.sprite.spritecollide(player, self.attack_group, False)
 	if hit_player:
 		player.getHit("none", 1)
 		hit_player[0].kill()
 	
 	
 def __loadShot(self, player):
 	self.immortal_timer = 2
	attack = Fire_Attack((self.rect.center[0], self.rect.center[1]), player.rect.center, helpers.checkOrient(player, self))
	self.attack_group.add(attack)


 def __decide(self):
 	self.dialogHandle = HandleDialog(self.screen, DialogBox((440, 51), 
 		(255, 255, 204),(102, 0, 0), pygame.font.SysFont('Verdana', 15)))
 	self.will_fight = self.dialogHandle.wizardChoice(self.screen)
 	self.decided = True


 def __move(self, player):
 	if self.walking_timer <= 0:
 		self.__walk()
 		self.walking_timer = 5
 	else:
 		self.walking_timer -= 1
 	
 	
 	x = player.rect.topleft[0]
	y = player.rect.topleft[1]
	my_x = self.rect.topleft[0]
	my_y = self.rect.topleft[1]
 	
 	if x+10 > self.rect.topleft[0]:
		my_x -= 1
	if x-10 < self.rect.topleft[0]:
		my_x += 1
	if y+10 > self.rect.topleft[1]:
		my_y -= 1
	if y-10 < self.rect.topleft[1]:
		my_y += 1
	self.rect.topleft = helpers.checkBoundry((my_x, my_y))

 def __walk(self):
 	if self.direction == "left":
 		self.image = self.left_w.update()
 	if self.direction == "right":
 		self.image = self.right_w.update()
	if self.direction == "up":
		self.image = self.up_w.update()
	if self.direction == "down":
		self.image = self.down_w.update()
		  
		  
 def get_hit(self, direction, damage):
 	if self.immortal_timer <= 0: 
 		self.health -= damage
 		self.immortal_timer = 50
 		self.__teleport()
 	if self.health <0:
 		self.kill()
 
 
 def __teleport(self):
	 if self.tele_done:
	 	self.image = self.tele1
	 	self.tele_done = False
	 	self.tele_tick = 10
	 else:
	 	if self.tele_tick <= 0:
	 		if self.image == self.tele1:
	 			self.image = self.tele2
	 		elif self.image == self.tele2:
	 			self.image = self.tele3
	 		elif self.image == self.tele3:
	 			self.image = self.tele4
	 		elif self.image == self.tele4:
	 			self.image = self.tele5
	 			self.tele_loc += 1
	 			if self.tele_loc >= len(self.tele_spots):
	 				self.tele_loc = 0
	 			self.rect.topleft = self.tele_spots[self.tele_loc]
	 			
	 			self.tele_done = True
	 		self.tele_tick = 10
	 	else:
	 		self.tele_tick -= 1
 