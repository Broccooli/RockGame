import os, pygame, sys, speechConstants
from pygame.locals import *
from levels import Levels


WHITE = pygame.Color(255,255,255)
BLACK = pygame.Color(0,0,0)
speech_by_level = Levels().dialogSelect()
fpsClock = pygame.time.Clock()
class HandleDialog(object):
	
    def __init__(self, screen, dialogBox):
	   self.handeled = False
	   self.dialogBox = dialogBox
	   self.screen = screen

    def update(self, current_level, enemyGroup, windowSurface):
        if self.handeled == False:
        	if speech_by_level[current_level][0] == "1":
        	   if enemyGroup:
        	      return "nothing"
        	   else:
        	      speech_by_level[current_level].remove("1")
        	else:
        	   while not self.dialogBox.over():
        	      if not speech_by_level[current_level] == "0":
        	         if speech_by_level[current_level] == "1":
        	             self.dialogBox.set_dialog(speech_by_level[current_level][1:last])
        	             speech_by_level[current_level] = "0"
        	         else:
        	             self.dialogBox.set_dialog(speech_by_level[current_level])
	                     speech_by_level[current_level] = "0"
	              for event in pygame.event.get():
	                 if event.type ==KEYUP:
	                    if event.key == K_RETURN:
	                        self.dialogBox.progress()
	              self.dialogBox.draw(windowSurface, (50, 400))
	              pygame.display.update()
	              fpsClock.tick(30)
	           self.handeled = True
    
    def levelChange(self):
        self.handeled = False
        
    def doorLocked(self, windowSurface):
	    self.dialogBox.set_dialog(speechConstants.DOOR_LOCKED)
	    while not self.dialogBox.over():
	        for event in pygame.event.get():
	            if event.type ==KEYUP:
	                if event.key == K_RETURN:
	                    self.dialogBox.progress()
	        self.dialogBox.draw(windowSurface, (50, 400))
	        pygame.display.update()
	        fpsClock.tick(30)
	        
    def enemyAlive(self, windowSurface):
	    self.dialogBox.set_dialog(speechConstants.ENEMY_ALIVE)
	    while not self.dialogBox.over():
	        for event in pygame.event.get():
	            if event.type ==KEYUP:
	                if event.key == K_RETURN:
	                    self.dialogBox.progress()
	        self.dialogBox.draw(windowSurface, (50, 400))
	        pygame.display.update()
	        fpsClock.tick(30)
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
