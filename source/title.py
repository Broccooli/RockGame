#from HUB import Menu
import pygame, sys
from pygame.locals import *
WHITE = pygame.Color(255,255,255)
BLACK = pygame.Color(0,0,0)
class TitleScreen():

    def __init__(self, surface):
        self.s = surface
        self.background = pygame.image.load('../images/title.png')
        self.menu = StartMenu(self.background, pygame.font.SysFont('Verdana', 15, True),
                         ["Start", "Exit"])

    def start(self):
        self.s.blit(self.background, (0,0))
        while(True):
            self.menu.update_box()
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == KEYUP:
                    if event.key == K_DOWN:
                        self.menu.next_down()
                    if event.key == K_UP:
                        self.menu.next_up()
                    if event.key == K_RETURN:
                        option = self.menu.get_position()
                        if option == 0:
                            return
                        if option == 1:
                            sys.exit(0)

class StartMenu():

    def __init__(self, background, font, options):
        self.screen = pygame.display.get_surface()
        self.cursor = pygame.image.load('../images/slash.png')
        
        self.font = font
        self.background= background
        self.cursor_position = 350
        self.cursor_option = 0
        self.shown = False
        #self.origin = spot #this will be used as an origin 
        self.options = len(options)
        self.option_choices = options
        
        self.update_box()
        
        
    def update_box(self):
        
        spot = 350
       
        self.screen.blit(self.background, (0,0))
        
        self.screen.blit(self.cursor, (45, self.cursor_position))
        
        for i in range(self.options):
        	self.screen.blit(self.font.render(self.option_choices[i], True, WHITE), (95, spot))
        	spot += 50
        
    def next_down(self):
    	if self.cursor_option < len(self.option_choices) - 1:
    	    self.cursor_position += 50
    	    self.cursor_option += 1
    def next_up(self): 
    	if self.cursor_option >= 1:
    		self.cursor_position -= 50
    		self.cursor_option -= 1
    def get_position(self):
    	return self.cursor_option
    
