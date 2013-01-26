import os, pygame, sys
from pygame.locals import *

class HUB():


	def drawHealth(self, player, windowSurface):
		WHITE = pygame.Color(255,255,255)
		my_font = pygame.font.SysFont('impact', 15)
		if int(player.getHealth()) >= 0:
			health_message = my_font.render("Health: " + player.getHealth(), True, WHITE)
		else:
			health_message = my_font.render("DEAD", True, WHITE)
		windowSurface.blit(health_message, (300, 10))