import os, pygame, sys
from pygame.locals import *

from doors import Door
from rocks import Rock
from enemy import Enemy

class Levels():
	def createLevels_Rock(self):
		rocks_by_level = []
		#setting up rocks for this room. This is how it will be done for puzzles. 
		#Long yes, but it matters where we put it
		test_room_rocks = [Rock((100, 10)), Rock((200, 205)), Rock((400, 300))]
		test_room_rocks_group = pygame.sprite.RenderPlain(test_room_rocks)
		rocks_by_level.append(test_room_rocks_group) #0
		#this is how to make a group to represent the level, then add it to the level array
		
		#First room, rocks
		s1r1_rocks = [Rock((500, 10)), Rock((300, 300)), Rock((110, 100))]
		s1r1_rocks_group = pygame.sprite.RenderPlain(s1r1_rocks)
		rocks_by_level.append(s1r1_rocks_group) #1
		return rocks_by_level
		
	def createLevels_Door(self):
		doors_by_level = []
		door_r0 = pygame.sprite.RenderPlain(Door((5, 20)))
		doors_by_level.append(door_r0)
		#room 0
		
		door_r1 = pygame.sprite.RenderPlain(Door((50, 25)))
		doors_by_level.append(door_r1)
		
		return doors_by_level
		
	def createLevels_enemies(self):
		enemies_by_level = []
		enemies_r0 = pygame.sprite.RenderPlain(Enemy((350, 350)))
		enemies_by_level.append(enemies_r0)
		
		enemies_r1 = pygame.sprite.RenderPlain()
		enemies_by_level.append(enemies_r1)
		return enemies_by_level