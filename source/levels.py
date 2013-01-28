import os, pygame, sys
from pygame.locals import *

from doors import Door
from rocks import *
from enemy import *
from random import randint

class Levels():
	def createLevels_Rock(self):
		rocks_by_level = []
		#setting up rocks for this room. This is how it will be done for puzzles. 
		#Long yes, but it matters where we put it
		test_room_rocks = [Rock((100, 25)), Boulder((200, 205)), Rock((400, 300))]
		test_room_rocks_group = pygame.sprite.RenderPlain(test_room_rocks)
		rocks_by_level.append(test_room_rocks_group) #0
		#this is how to make a group to represent the level, then add it to the level array
		
		#First room, rocks
		s1r1_rocks = [Rock((500, 25)), Boulder((300, 300)), Rock((110, 100))]
		s1r1_rocks_group = pygame.sprite.RenderPlain(s1r1_rocks)
		rocks_by_level.append(s1r1_rocks_group) #1
		return rocks_by_level
		
	def createLevels_Door(self):
		doors_by_level = []
		door_r0 = pygame.sprite.RenderPlain(Door((5, 20)))
		doors_by_level.append(door_r0)
		#room 0
		
		door_r1 = pygame.sprite.RenderPlain(Door((300, 25)))
		doors_by_level.append(door_r1)
		
		return doors_by_level
		
	def createLevels_enemies(self, windowSurface):
		enemies_by_level = []
		enemies_r0 = pygame.sprite.RenderPlain(M_Enemy((350, 350)))
		enemies_by_level.append(enemies_r0)
		
		enemies_r1 = pygame.sprite.RenderPlain(R_Enemy((400, 300), windowSurface))
		enemies_by_level.append(enemies_r1)
		return enemies_by_level
		
	def drawBackground(self, screen):
		#rando = random.seed()
		dirt4 = pygame.image.load('../images/dirttile4.png')
		dirt3 = pygame.image.load('../images/dirttile3.png')
		dirt2 = pygame.image.load('../images/dirttile2.png')
		dirt1 = pygame.image.load('../images/dirttile.png')
		dirts = []
		dirts.append(dirt1)
		dirts.append(dirt2)
		dirts.append(dirt3)
		dirts.append(dirt4)
		top = pygame.image.load('../images/cavewalltile2.png')
		bottom = pygame.image.load('../images/cavewalltile4.png')
		left = pygame.image.load('../images/cavewalltile3.png')
		right = pygame.image.load('../images/cavewalltile1.png')
		topleft = pygame.image.load('../images/topleft.png')
		bottomleft = pygame.image.load('../images/bottomleft.png')
		topright = pygame.image.load('../images/topright.png')
		bottomright = pygame.image.load('../images/bottomright.png')
		img_rect = dirt4.get_rect()
		nrows = int(screen.get_height() / img_rect.height) + 1
		ncols = int(screen.get_width() / img_rect.width) + 1
		
		final_background = []
		for y in range(nrows):
			final_background.append([])
			for x in range(ncols):
				i = randint(0, 3)
				#img_rect.topleft = (x * img_rect.width,y * img_rect.height)
				if x == 0:
					if y == 0:
						final_background[y].append(topleft)
					elif y == nrows -2:
						final_background[y].append(bottomleft)
					else:
						final_background[y].append(left)
				elif x == 20:
					if y == 0:
						final_background[y].append(topright)
					elif y == nrows -2:
						final_background[y].append(bottomright)
					else:	
						final_background[y].append(right)
				elif y == 0:
					final_background[y].append(top)
				elif y == nrows -2:
					final_background[y].append(bottom)
				else:
					final_background[y].append(dirts[i])
				
		return final_background
		