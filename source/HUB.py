import os, pygame, sys
from pygame.locals import *


WHITE = pygame.Color(255,255,255)
BLACK = pygame.Color(0,0,0)
"""
Makes the text at the top showing health. Want to make it better. Maybe even
make it into having a small portrait of the character in the bottom left
and the only way to tell damage is to see how damaged the picture looks
THATS REMOVES NUMBERS, BITCHES HATE NUMBERS.
""" 

class HUB():
	def drawHealth(self, player, windowSurface):
		
		my_font = pygame.font.SysFont('impact', 15)
		if int(player.getHealth()) >= 0:
			health_message = my_font.render("Health: " + player.getHealth(), True, WHITE)
		else:
			health_message = my_font.render("DEAD", True, WHITE)
		windowSurface.blit(health_message, (300, 10))

"""
Little method making the "Next" arrow
""" 

def arrow_image(color):
    img = pygame.Surface((7, 6))
    img.fill((226, 59, 252))
    img.set_colorkey((226, 59, 252), pygame.RLEACCEL)
    pygame.draw.polygon(img, color, ((0, 0), (3, 3), (6, 0)))
    return img
		
		
		
#modified from http://www.pygame.org/project-Retro+Game+Library-1065-.html
#open source under 
class DialogBox(object):
    
    def __init__(self, size, background_color, border_color, font):
        self.dialog = []
        self.image = pygame.Surface(size)
        self.font = font
        self.size = size
        self.background_color = background_color
        self.border_color = border_color
        self.update_box()
        self.text_pos = 0
        self.shown = False
        self.scroll_delay = 1
        self.frame = 0
        self.down_arrow = arrow_image(pygame.Color(0,0,0))
    
    def set_scrolldelay(self, delay):
        self.scroll_delay = delay
    
    def set_dialog(self, dialog_list):
        self.page = 0
        self.pages = len(dialog_list)
        self.dialog = dialog_list
        self.shown = True
        self.text_pos = 0
    
    def update_box(self):
        self.image.fill(self.background_color)
        pygame.draw.rect(self.image, self.border_color, 
            (0, 0, self.size[0], self.size[1]), 1)
    
    def progress(self):
        if self.text_pos >= len(self.curr_dialog):
            if self.page < self.pages-1:
                self.page += 1
                self.text_pos = 0
            else:
                self.shown = False
        else:
            self.text_pos = len(self.curr_dialog)
    
    def draw(self, surface, pos):
        
        if self.shown and self.page < self.pages:
            my_font = pygame.font.SysFont('verdana', 15)
            self.update_box()
            self.curr_dialog = self.dialog[self.page]
            xpos = 4
            ypos = 4
            if self.text_pos < len(self.curr_dialog):
                self.frame -= 1
                if self.frame <= 0:
                    self.text_pos += 1
                    self.frame = self.scroll_delay
            else:
                self.image.blit(self.down_arrow, 
                    (self.image.get_width()-12, 
                    self.image.get_height()-8))
            dialog = self.curr_dialog[:self.text_pos]
            for word in dialog.split(" "):
                ren = my_font.render("  "+ word, True, BLACK)
                w = ren.get_width()
                if xpos > self.image.get_width()-w:
                    ypos += ren.get_height()+3
                    xpos = 4
                    ren = my_font.render("  " + word, True, BLACK)
                self.image.blit(ren, (xpos, ypos))
                xpos += w
            surface.blit(self.image, pos)
    
    def over(self):
        return self.shown != True
    
    def close(self):
        self.shown = False
        self.page = self.pages

class Menu():

    def __init__(self, size, background_color, border_color, font, options):
        self.screen = pygame.display.get_surface()
        self.cursor = pygame.image.load('../images/slash.png')
        self.image = pygame.Surface(size)
        self.size = size
        self.font = font
        self.background_color = background_color
        self.border_color = border_color
        self.cursor_position = 150
        self.cursor_option = 0
        self.shown = False
        self.options = len(options)
        self.option_choices = options
        self.update_box()
        
    def update_box(self):
        self.image.fill(self.background_color)
        spot = 150
        self.screen.fill(self.border_color, pygame.Rect(240, 120, 185, 150))
        self.screen.fill(self.background_color, pygame.Rect(245, 125, 175, 200))
        self.screen.blit(self.cursor, (245, self.cursor_position))
        for i in range(self.options):
        	self.screen.blit(self.font.render(self.option_choices[i], True, BLACK), (295, spot))
        	spot += 50
        
#         pygame.draw.rect(self.image, self.border_color, 
#             (0, 0, self.size[0], self.size[1]), 1)
            
    def close(self):
        self.shown = False
        self.page = self.pages
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
    
