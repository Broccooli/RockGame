import os, pygame, sys
from pygame.locals import *

class HUB():


	def drawHealth(self, player, windowSurface):
		BLACK = pygame.Color(0,0,0)
		my_font = pygame.font.SysFont('impact', 15)
		if int(player.getHealth()) >= 0:
			health_message = my_font.render("Health: " + player.getHealth(), True, BLACK)
		else:
			health_message = my_font.render("DEAD", True, BLACK)
		windowSurface.blit(health_message, (300, 10))