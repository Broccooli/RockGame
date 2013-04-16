import os, pygame, sys, speechConstants
from pygame.locals import *

from doors import Door
from rocks import *
from enemy import *
from grunk import Grunk
from squik import Squik
from plates import PressurePlate
from random import randint
from tahzi import TahZi

class Levels():
	"X< 672, Y < 512"
	
	def createLevels_Rock(self):
		rocks_by_level = []
		#setting up rocks for this room. This is how it will be done for puzzles. 
		#Long yes, but it matters where we put it
		rocks_by_level.append(pygame.sprite.RenderPlain(Rock((100, 25)), Boulder((200, 205)), Rock((400, 300)))) #0
		#this is how to make a group to represent the level, then add it to the level array
		
		#First room, rocks
		rocks_by_level.append(pygame.sprite.RenderPlain(Rock((500, 25)), Boulder((300, 300)), Rock((110, 100)))) #1
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
			Rock((400, 75)), Rock((300, 75)), Boulder((255, 120)), Boulder((445, 120))))
		#Squik traps	
		rocks_by_level.append(pygame.sprite.RenderPlain(Rock((530, 375)), Rock((430, 375)), 
		    Rock((70, 375)), Rock((170, 375)), Rock((70, 70)), Rock((170, 70)), 
		    Rock((430, 70)), Rock((530, 70)), Rock((430, 225)), Rock((530, 225)), 
			Rock((70, 225)), Rock((170, 225)), Rock((300, 320)), Rock((300, 200)), 
		))
		
		#Flower
		rocks_by_level.append(pygame.sprite.RenderPlain(Rock((525, 375)), Rock((430, 375)),
		Rock((475, 415)), Rock((475, 335)), Rock((525, 335)), Rock((430, 335)),
		Rock((565, 375)), Rock((390, 375)), Rock((475, 300)), Rock((475, 450)),
		Rock((525, 415)), Rock((435, 415)),
		Boulder((525, 450)), Boulder((430, 450)), Boulder((430, 300)), Boulder((525, 300)),
		Boulder((570, 415)), Boulder((570, 340)), Boulder((395, 415)), Boulder((395, 340))
		))
		
		#Ninth
		rocks_by_level.append(pygame.sprite.RenderPlain(Boulder((20, 180)), Boulder((85, 180)), Boulder((150, 180)), Rock((215, 180)),Boulder((280, 180)), Boulder((345, 180)), Boulder((410, 180)),
			Boulder((20, 275)), Boulder((85, 275)), Boulder((150, 275)), Boulder((215, 275)),Boulder((280, 275)), Boulder((345, 275)), Boulder((410, 275)), #the two ross
			Boulder((500, 100)), Boulder((450, 140)), Boulder((500, 360)), Boulder((450, 310))))
		
		
		#Tahzi, these ones need to line up perfectly as he merely jumps to where he needs to be
		#and is invulnerable when touching a rock
		rocks_by_level.append(pygame.sprite.RenderPlain(Boulder((320, 240)), Boulder((55, 240)), Boulder((400, 310)), 
		Boulder((120, 240)), Boulder((205, 240)), Boulder((250, 170)), Boulder((510, 240)),
		Boulder((320, 140)), Boulder((320, 55)), Boulder((400, 170)), Boulder((425, 240)), Boulder((575, 240)), 
		Boulder((245, 310)), Boulder((320, 360)),Boulder((320, 445)) ))
		
		#First of the real dung. Trying to look like these boulders weren't placed
		rocks_by_level.append(pygame.sprite.RenderPlain(Boulder((165, 340)), Boulder((305, 235)),
		Boulder((150, 115)), Boulder((600, 70))
		))
		
		#Second, Only one in the top as if it had also fallen due to shaking
		rocks_by_level.append(pygame.sprite.RenderPlain(Boulder((25, 30))))
		
		#Third, slight puzzle
		rocks_by_level.append(pygame.sprite.RenderPlain(Boulder((460, 195)), Boulder((460, 150)),
		Boulder((500, 115)), Boulder((550, 150)),
		Boulder((500, 150)), Boulder((325, 105)),
		Boulder((170, 195)), Boulder((125, 150)),
		Boulder((125, 115)), Boulder((85, 150)),
		Boulder((80, 195)), Boulder((550, 195)), Rock((325, 300))
		))
		
		#Fourth, Grid pattern
		rocks_by_level.append(pygame.sprite.RenderPlain(Rock((105, 85)), Rock((50, 165)),
		Rock((255, 85)), Rock((180, 165)), Rock((440, 85)), Rock((340, 165)), Rock((590, 85)), Rock((525, 165)),
		#First two rows, going to copy the pattern completely. Difference in Y = 80
		Rock((105, 245)), Rock((50, 325)), Rock((255, 245)), Rock((180, 325)), 
		Rock((440, 245)), Rock((340, 325)), Rock((590, 245)), Rock((525, 325))
		
		))
		
		#Boss spawns rocks
		rocks_by_level.append(pygame.sprite.RenderPlain())
		
		
		return rocks_by_level
		
	def createLevels_Door(self):
		doors_by_level = []
		#0
		doors_by_level.append(pygame.sprite.RenderPlain(Door((0, 255), False)))
		#1
		doors_by_level.append(pygame.sprite.RenderPlain(Door((0, 255), False)))
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
		#Squick
		doors_by_level.append(pygame.sprite.RenderPlain(Door((600, 0), False)))
		#Flowers
		doors_by_level.append(pygame.sprite.RenderPlain(Door((640, 255), True)))
		#Ninth
		doors_by_level.append(pygame.sprite.RenderPlain(Door((640, 255), True)))
		#No door here, covered by a rock
		doors_by_level.append(pygame.sprite.RenderPlain(Door((640, 50), False)))
		#companion room, start of real dungeon.
		doors_by_level.append(pygame.sprite.RenderPlain(Door((325, 480), False)))
		#Second of real levels
		doors_by_level.append(pygame.sprite.RenderPlain(Door((325, 480), False)))
		#Third
		doors_by_level.append(pygame.sprite.RenderPlain(Door((325, 480), True)))
		#Fourth
		doors_by_level.append(pygame.sprite.RenderPlain(Door((325, 480), True)))
		#No door for the last boss
		doors_by_level.append(pygame.sprite.RenderPlain())
		
		return doors_by_level
		
	def playerStartPositions(self): #going to be one behind doors, opposite of previous exit
		player_entrance = []
		player_entrance.append((600, 255))
		player_entrance.append((600, 255))
		player_entrance.append((100, 430))
		player_entrance.append((50, 25))
		player_entrance.append((50, 255))
		player_entrance.append((545, 435))
		player_entrance.append((200, 435))
		player_entrance.append((600, 435))
		player_entrance.append((15, 225))
		player_entrance.append((15, 225))
		player_entrance.append((20, 50))
		player_entrance.append((325, 20))
		player_entrance.append((325, 20))
		player_entrance.append((325, 20))
		player_entrance.append((325, 20))
		return player_entrance
		
	def createLevels_enemies(self, windowSurface):
		enemies_by_level = []
		enemies_by_level.append(pygame.sprite.RenderPlain(M_Enemy((100, 350), 3)))

		enemies_by_level.append(pygame.sprite.RenderPlain(R_Enemy((400, 300), windowSurface)))
		
		enemies_by_level.append(pygame.sprite.RenderPlain(R_Enemy((50, 450), windowSurface), M_Enemy((500, 50), 1)))
		
		enemies_by_level.append(pygame.sprite.RenderPlain(Grunk()))
		
		enemies_by_level.append(pygame.sprite.RenderPlain(R_Enemy((175, 100), windowSurface)))
		enemies_by_level.append(pygame.sprite.RenderPlain(M_Enemy((379,440), 1), R_Enemy((190, 25), windowSurface)))
		enemies_by_level.append(pygame.sprite.RenderPlain(R_Enemy((345, 90), windowSurface)))
		enemies_by_level.append(pygame.sprite.RenderPlain(Squik()))
		enemies_by_level.append(pygame.sprite.RenderPlain())
		enemies_by_level.append(pygame.sprite.RenderPlain(M_Enemy((550,230), 2), R_Enemy((115, 75), windowSurface), R_Enemy((115, 385), windowSurface)))
		enemies_by_level.append(pygame.sprite.RenderPlain(TahZi()))
		#enemies of the First part of dung
		enemies_by_level.append(pygame.sprite.RenderPlain())
		#Second room, standing in rows
		enemies_by_level.append(pygame.sprite.RenderPlain(M_Enemy((220,260), 3), M_Enemy((390, 260), 3),
	    R_Enemy((95, 370), windowSurface), R_Enemy((325, 370), windowSurface), R_Enemy((520, 370), windowSurface)))
		#Only ranger turret
		enemies_by_level.append(pygame.sprite.RenderPlain(R_Enemy((505,195), windowSurface), R_Enemy((125, 195), windowSurface)))
		#Spread through grid
		enemies_by_level.append(pygame.sprite.RenderPlain(R_Enemy((110, 160), windowSurface), 
		   R_Enemy((110, 320), windowSurface), R_Enemy((440, 325), windowSurface),
		   R_Enemy((440, 165), windowSurface), M_Enemy((525,440), 3), M_Enemy((170,440), 3)))
		#Last Bawwss
		enemies_by_level.append(pygame.sprite.RenderPlain())
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
		speech_by_level.append(speechConstants.KILL_SQUIK)
		speech_by_level.append(speechConstants.FLOWERS)
		speech_by_level.append(speechConstants.NINTH_ROOM)
		speech_by_level.append(speechConstants.FIGHT_TAHZI)
		speech_by_level.append(speechConstants.PART2_ROOM1)
		speech_by_level.append(speechConstants.PART2_ROOM2)
		speech_by_level.append(speechConstants.PART2_ROOM3)
		speech_by_level.append(speechConstants.PART2_ROOM4)
		speech_by_level.append(speechConstants.FINAL_ROOM)
		return speech_by_level
		
	def placePlate(self):
		plates_by_level = ["1", "1", "1", "1"]
		plates_by_level.append(pygame.sprite.RenderPlain(PressurePlate((300, 300))))
		#5th
		plates_by_level.append(pygame.sprite.RenderPlain(PressurePlate((310, 40))))
		plates_by_level.append("1")
		plates_by_level.append("1")
		plates_by_level.append(pygame.sprite.RenderPlain(PressurePlate((485, 400))))
		plates_by_level.append(pygame.sprite.RenderPlain(PressurePlate((580, 450))))
		plates_by_level.append("1")
		#Start of real dung
		plates_by_level.append("1")
		plates_by_level.append("1")
		plates_by_level.append(pygame.sprite.RenderPlain(PressurePlate((140, 210))))
		plates_by_level.append(pygame.sprite.RenderPlain(PressurePlate((40, 450))))
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
	
	
	def getSingleEnemy(object, level):
		return Levels.enemies_by_level[level]
	def getSingleRocks(object, level):
		return Levels.rocks_by_level[level]	