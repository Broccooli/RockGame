import os, pygame, sys, speechConstants
from pygame.locals import *

from doors import Door
from rocks import *
from enemy import *
from grunk import Grunk
from plates import PressurePlate
from random import randint

class Levels():
	"X< 672, Y < 512"
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
		#2
		rocks_by_level.append(pygame.sprite.RenderPlain(Rock((300, 400)),
			Boulder((150, 50)), Boulder((50, 50))))
		#Grunk Rocks	
		rocks_by_level.append(pygame.sprite.RenderPlain(Rock((100, 100)),
			Rock((550, 100)), Rock((550, 390,)), Rock((100, 390)),
			Boulder((40, 250)), Boulder((600, 250)),
			Rock((200, 245)), Rock((440,245))))	
		#4
		rocks_by_level.append(pygame.sprite.RenderPlain(Rock((140, 100)),
			Boulder((300, 400)), Rock((220, 100)), 
			Rock((90, 375)), Rock((400,290))))
		#5, my first attempt at something to be solved, can become unsolvable	
		rocks_by_level.append(pygame.sprite.RenderPlain(Rock((155, 25)),
			Boulder((260,20)), Boulder((335, 20)), #top
			Boulder((345, 460)), Boulder((415, 460)), #bottom
			Rock((379,425)), Boulder((255, 255)), Boulder((500, 190))))	
			
		#6th, this ones gonna be long
		#65 seems to be just the right spacing
		rocks_by_level.append(pygame.sprite.RenderPlain(Rock((350, 375)),
			Boulder((530, 375)), Boulder((465, 375)), Boulder((400, 375)), Boulder((175, 375)),		
			Boulder((110, 375)), Boulder((595, 375)), Boulder((45, 375)), Boulder((240, 375)),
			Boulder((300, 375)), #All that, thats just the first row. Hot damn
			Boulder((400, 275)), Boulder((300,275)), Boulder((255, 320)), Boulder((445, 320)),
			Boulder((400, 175)), Boulder((300, 175)), Boulder((255, 220)), Boulder((445, 220)),
			Boulder((400, 75)), Boulder((300, 75)), Boulder((255, 120)), Boulder((445, 120))))
		return rocks_by_level
		
	def createLevels_Door(self):
		doors_by_level = []
		door_r0 = pygame.sprite.RenderPlain(Door((0, 255), False))
		doors_by_level.append(door_r0)
		#room 0
		
		door_r1 = pygame.sprite.RenderPlain(Door((0, 255), False))
		doors_by_level.append(door_r1)
		#2
		doors_by_level.append(pygame.sprite.RenderPlain(Door((100, 0), False)))
		#3
		doors_by_level.append(pygame.sprite.RenderPlain(Door((640, 50), False)))
		#4
		doors_by_level.append(pygame.sprite.RenderPlain(Door((640, 255), True)))
		#5
		doors_by_level.append(pygame.sprite.RenderPlain(Door((550, 0), True)))
		#6
		doors_by_level.append(pygame.sprite.RenderPlain(Door((200, 0), False)))
		
		return doors_by_level
		
	def playerStartPositions(self): #going to be one behind doors, opposite of previous exit
		player_entrance = []
		player_entrance.append((600, 255))
		player_entrance.append((600, 255))
		player_entrance.append((100, 430))
		player_entrance.append((50, 25))
		player_entrance.append((50, 255))
		player_entrance.append((545, 420))
		return player_entrance
		
	def createLevels_enemies(self, windowSurface):
		enemies_by_level = []
		enemies_r0 = pygame.sprite.RenderPlain(M_Enemy((100, 350), 2))
		enemies_by_level.append(enemies_r0)
		
		enemies_r1 = pygame.sprite.RenderPlain(R_Enemy((400, 300), windowSurface))
		enemies_by_level.append(enemies_r1)
		
		
		enemies_r2 = [R_Enemy((50, 450), windowSurface), M_Enemy((500, 50), 1)]
		enemies_r2_group = pygame.sprite.RenderPlain(enemies_r2)
		enemies_by_level.append(enemies_r2_group)
		
		enemies_by_level.append(pygame.sprite.RenderPlain(Grunk()))
		
		enemies_by_level.append(pygame.sprite.RenderPlain(R_Enemy((175, 100), windowSurface)))
		enemies_by_level.append(pygame.sprite.RenderPlain(M_Enemy((379,440), 1), R_Enemy((190, 25), windowSurface)))
		enemies_by_level.append(pygame.sprite.RenderPlain(R_Enemy((345, 90), windowSurface)))
		return enemies_by_level
		
	def dialogSelect(self):
		speech_by_level = []
		speech_by_level.append(speechConstants.INTRO_MESSAGE)
		speech_by_level.append(speechConstants.SECOND_ROOM)
		speech_by_level.append(speechConstants.THIRD_ROOM)
		speech_by_level.append(speechConstants.KILL_GRUNK)
		speech_by_level.append(speechConstants.FOURTH_ROOM)
		speech_by_level.append(speechConstants.FIFTH_ROOM)
		speech_by_level.append(speechConstants.SIXTH_ROOM)
		return speech_by_level
		
	def placePlate(self):
		plates_by_level = ["1", "1", "1", "1"]
		plates_by_level.append(pygame.sprite.RenderPlain(PressurePlate((300, 300))))
		#5th
		plates_by_level.append(pygame.sprite.RenderPlain(PressurePlate((310, 40))))
		plates_by_level.append("1")
		return plates_by_level
		
		
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
		