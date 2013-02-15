import os, pygame, sys, helpers
from pygame.locals import *

"These are the blocks that can be pushed around by giants belt and destroyed by knucks"
class Rock(pygame.sprite.Sprite):
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
    	self.image = pygame.image.load('../images/rock.png')
    	self.rect = self.image.get_rect()
    	self.position = position
    	self.rect.topleft = position[0], position [1]
    
    "This one is only for Grunk."
    def getMoved(self, rocks, direction, player):
    	old_position = self.rect.topleft
    	other_rocks = pygame.sprite.RenderPlain(rocks)
    	other_rocks.remove(self)
	
    	if direction == "right":
    		self.rect.topleft = self.position[0] + 10, self.position[1]
    	elif direction == "left":
    		self.rect.topleft = self.position[0] - 10, self.position[1]
    	elif direction == "down":
    		self.rect.topleft = self.position[0], self.position[1] +10
    	elif direction == "up":	
    		self.rect.topleft = self.position[0], self.position[1] -10
    		
    	self.position = self.rect.topleft
    	hit_rock = pygame.sprite.spritecollide(self, other_rocks, False)
    	"""Checks to make sure there is no rock in the way/its in bounds"""
    	if (hit_rock) or (self.position [0] < 25) or (self.position [0] > 620) or (self.position [1] < 25) or (self.position [1] > 460):
    		self.rect.topleft = old_position[0], old_position[1]
    		self.position = old_position
    	"""Checks to see if Grunk smashed a player witha  rock. It will probably kill player"""
    	if pygame.sprite.collide_rect(self, player):
    	    player.getHit(direction, 1)

    
    
    """Moved by player, makes things have to be straight"""	       
    def getMovedP(self, rocks, direction, player, enemyGroup):
    	old_position = self.rect.topleft
    	other_rocks = pygame.sprite.RenderPlain(rocks)
    	other_rocks.remove(self)
    	"I did this while very sick, this might be too much to make sure its straight"
    	if (player.rect.topleft[0] < self.position[0]) and direction =="right":
    		self.rect.topleft = self.position[0] + 10, self.position[1]
    	elif (player.rect.topleft[0] > self.position[0]) and direction =="left":
    		self.rect.topleft = self.position[0] - 10, self.position[1]
    	elif (player.rect.topleft[1] < self.position[1]) and direction =="down":
    		self.rect.topleft = self.position[0], self.position[1] +10
    	elif (player.rect.topleft[1] > self.position[1]) and direction =="up":	
    		self.rect.topleft = self.position[0], self.position[1] -10
    	self.position = self.rect.topleft
    	hit_rock = pygame.sprite.spritecollide(self, other_rocks, False)
    	"""Checks to make sure there is no rock in the way/its in bounds"""
    	if (hit_rock) or (self.position [0] < 25) or (self.position [0] > 620) or (self.position [1] < 25) or (self.position [1] > 460):
    		self.rect.topleft = old_position[0], old_position[1]
    		self.position = old_position
    	    
    	"""Check to see if an enemy is between two rocks. if so, DEAD"""    
    	hit_enemy = pygame.sprite.spritecollide(self, enemyGroup, False)
    	if hit_enemy:
    	    "Checks to make sure the rock is moving at the enemy, not just rolling a foot"
    	    if (hit_enemy[0].position[0] > self.position[0] and direction == "right") or (hit_enemy[0].position[0] < self.position[0] and direction == "left") or (hit_enemy[0].position[1] > self.position[1] and direction == "down") or (hit_enemy[0].position[1] < self.position[1] and direction == "up"):
    	       squash_enemy = pygame.sprite.spritecollide(hit_enemy[0], other_rocks, False)
    	       if (squash_enemy) or (hit_enemy[0].position[0] <= 20) or (hit_enemy[0].position[0] >= 590) or (hit_enemy[0].position[1] <= 20) or (hit_enemy[0].position[0] >= 420):
    	          hit_enemy[0].get_hit(direction, 10)
    	       else:
    	       	  hit_enemy[0].get_hit(direction, 0)
    	
"These are immovable, indestructable objects to make puzzles hard"	
class Boulder(pygame.sprite.Sprite):
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
    	self.image = pygame.image.load('../images/Boulder.png')
    	self.rect = self.image.get_rect()
    	self.position = position
    	self.rect.topleft = position[0], position [1]
    	
    def getMoved(self, rocks, direction, player):
		i = 1 #filler, im going to do something with this later. but i means nothing
    def getMovedP(self, rocks, direction, player, enemyGroup):
		i = 1
		
"so puzzles arent so boring with what is going on"

"""I CANNOT GET THE REXT RIGHT WHEN DOING THE TOP. 
The rect always goes to the topleft, as thats the argument, so when the topleft
is the empty/passable part, I dont know how to move it down. rect.move seems to
move the whole thing. Scrapped till fixed.
""" 
class Stalagmite(pygame.sprite.Sprite):
	def __init__(self, position):
		pygame.sprite.Sprite.__init__(self)
		if position[1] > 300:
			self.image = pygame.image.load('../images/stalag.png')
			self.rect = pygame.Rect(position[0], position[1], 45, 5)
			self.rect.center = position[0], position [1]
		else:
			self.image = pygame.image.load('../images/stalagup.png')
			self.rect = pygame.Rect((position[0]), position[1], 30, 30)
			
			
	def getMoved(self, rocks, direction):
		i = 1 #filler, im going to do something with this later. but i means nothing