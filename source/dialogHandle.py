import os, pygame, sys, speechConstants
from pygame.locals import *
from levels import Levels
from HUB import Menu


WHITE = pygame.Color(255,255,255)
BLACK = pygame.Color(0,0,0)
speech_by_level = Levels().dialogSelect()
fpsClock = pygame.time.Clock()
class HandleDialog(object):
	
    def __init__(self, screen, dialogBox):
	   self.handeled = False
	   self.dialogBox = dialogBox
	   self.screen = screen
	   self.checked = False

    def update(self, current_level, enemyGroup, windowSurface, player):
    	if current_level == 15 and self.checked == False:
    		if not player.hasFriend:
    			speech_by_level[current_level] = speechConstants.COMPANIONLESS_THRONE
    			self.checked = True
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


    def examineRock(self, windowSurface, ID):
	    self.dialogBox.set_dialog(speechConstants.EXAMINE_ROCK)
	    if ID == 2:
	       image = pygame.image.load('../images/Boulder.png')
	    else:
	       image = pygame.image.load('../images/Rock.png')
	    image = pygame.transform.scale(image, (100, 100))
	    while not self.dialogBox.over():
	        for event in pygame.event.get():
	            if event.type ==KEYUP:
	                if event.key == K_RETURN:
	                    self.dialogBox.progress()
	        self.dialogBox.draw(windowSurface, (50, 400))
	        windowSurface.blit(image, (275, 200))
	        pygame.display.update()
	        fpsClock.tick(30)

    def examinePlate(self, windowSurface):
	    self.dialogBox.set_dialog(speechConstants.EXAMINE_PLATE)
	    image = pygame.image.load('../images/plate.png')
	    image = pygame.transform.scale(image, (100, 100))
	    while not self.dialogBox.over():
	        for event in pygame.event.get():
	            if event.type ==KEYUP:
	                if event.key == K_RETURN:
	                    self.dialogBox.progress()
	        self.dialogBox.draw(windowSurface, (50, 400))
	        windowSurface.blit(image, (275, 200))
	        pygame.display.update()
	        fpsClock.tick(30)

	
    def wizardChoice(self, windowSurface):
    	option = 5
    	menu = Menu((480, 51), (255, 255, 204), 
        (102, 0, 0), pygame.font.SysFont('Verdana', 15), ["Accept", "Fight"])
    	while (option == 5):
    		menu.update_box()
	        pygame.display.update()
	        for event in pygame.event.get():
	            if event.type == QUIT:
	                sys.exit(0) # Clicking the x now closes the game, not ESC
	            if event.type ==KEYUP:
	                if event.key == K_DOWN:
	                    menu.next_down()
	                if event.key == K_UP:
	                    menu.next_up()
	                if event.key == K_RETURN:
	                    option = menu.get_position()
     	dialog_done = False
     	if option == 1:
	    	self.dialogBox.set_dialog(speechConstants.FIGHT_WIZARD)
	    	while not dialog_done:
				for event in pygame.event.get():
					if event.type ==KEYUP:
						if event.key == K_RETURN:
							self.dialogBox.progress()
				self.dialogBox.draw(windowSurface, (50, 400))
				pygame.display.update()
				fpsClock.tick(30)
				dialog_done = self.dialogBox.over()
	    	return True
     	if option == 0:
	    	self.dialogBox.set_dialog(speechConstants.ACCEPT_WIZARD)
	    	while not dialog_done:
				for event in pygame.event.get():
					if event.type ==KEYUP:
						if event.key == K_RETURN:
							self.dialogBox.progress()
				self.dialogBox.draw(windowSurface, (50, 400))
				pygame.display.update()
				fpsClock.tick(30)
				dialog_done = self.dialogBox.over()
	    	return False
    
    def ending(self, windowSurface, id):
		dialog_done = False
		if id == 1:
	    		self.dialogBox.set_dialog(speechConstants.MASTER_END)
	    		while not dialog_done:
					for event in pygame.event.get():
						if event.type ==KEYUP:
							if event.key == K_RETURN:
								self.dialogBox.progress()
					self.dialogBox.draw(windowSurface, (50, 400), WHITE)
					pygame.display.update()
					fpsClock.tick(30)
					dialog_done = self.dialogBox.over()
		if id == 0:
	    		self.dialogBox.set_dialog(speechConstants.FREEDOM_END)
	    		while not dialog_done:
					for event in pygame.event.get():
						if event.type ==KEYUP:
							if event.key == K_RETURN:
								self.dialogBox.progress()
					self.dialogBox.draw(windowSurface, (50, 400), WHITE)
					pygame.display.update()
					fpsClock.tick(30)
					dialog_done = self.dialogBox.over()
    
    def companionDeath(self, windowSurface, companion):
	    
	    self.dialogBox.set_dialog(speechConstants.COMPANION_DEATH)
	    dialog_done = False
	    #Dialog Loop
	    while not dialog_done:
	        for event in pygame.event.get():
	            if event.type ==KEYUP:
	                if event.key == K_RETURN:
	                    self.dialogBox.progress()
	        self.dialogBox.draw(windowSurface, (50, 400))
	        pygame.display.update()
	        fpsClock.tick(30)
	        dialog_done = self.dialogBox.over()

    def companionOpening(self, windowSurface, companion):
	    
	    self.dialogBox.set_dialog(speechConstants.COMPANION_OPEN)
	    dialog_done = False
	    #Dialog Loop
	    while not dialog_done:
	        for event in pygame.event.get():
	            if event.type ==KEYUP:
	                if event.key == K_RETURN:
	                    self.dialogBox.progress()
	        self.dialogBox.draw(windowSurface, (50, 400))
	        pygame.display.update()
	        fpsClock.tick(30)
	        dialog_done = self.dialogBox.over()
	    option = 5
	    option2 = 5
	    menu = Menu((480, 51), (255, 255, 204), 
        (102, 0, 0), pygame.font.SysFont('Verdana', 15), ["Give Sword", "Give Bow", "Kill"])
	    #Menu Loop
	    while (option == 5):
	        menu.update_box()
	        pygame.display.update()
	        for event in pygame.event.get():
	            if event.type == QUIT:
	                sys.exit(0) # Clicking the x now closes the game, not ESC
	            if event.type ==KEYUP:
	                if event.key == K_DOWN:
	                    menu.next_down()
	                if event.key == K_UP:
	                    menu.next_up()
	                if event.key == K_RETURN:
	                    option = menu.get_position()
		
		
	    if option == 2:
	        companion.startAlive(False)
		#Second menu for Agressive or Defensive 
	    if option == 0 or option == 1:
	        menu = Menu((440, 51), (255, 255, 204),(102, 0, 0), pygame.font.SysFont('Verdana', 15), ["Be Aggressive", "Be Defensive"])
	        while (option2 == 5):
	           menu.update_box()
	           pygame.display.update()
	           for event in pygame.event.get():
	            if event.type == QUIT:
	                sys.exit(0) # Clicking the x now closes the game, not ESC
	            if event.type ==KEYUP:
	                if event.key == K_DOWN:
	                    menu.next_down()
	                if event.key == K_UP:
	                    menu.next_up()
	                if event.key == K_RETURN:
	                    option2 = menu.get_position()
	    
	    if option == 0:
	        if option2 == 0:
	            self.dialogBox.set_dialog(speechConstants.COMPANION_SWORD_A)
	        else:
	            self.dialogBox.set_dialog(speechConstants.COMPANION_SWORD_D)
	    if option == 1:
	        if option2 == 0:
	            self.dialogBox.set_dialog(speechConstants.COMPANION_BOW_A)
	        else:
	            self.dialogBox.set_dialog(speechConstants.COMPANION_BOW_D)
	    if option == 2:
	        self.dialogBox.set_dialog(speechConstants.COMPANION_KILL)
	    #Dialog Loop
	    while not self.dialogBox.over():
	        for event in pygame.event.get():
	            if event.type ==KEYUP:
	                if event.key == K_RETURN:
	                    self.dialogBox.progress()
	        self.dialogBox.draw(windowSurface, (50, 400))
	        pygame.display.update()
	        fpsClock.tick(30)
        
        
	    if not option == 2:
	        companion.startUp(option, option2)
	        
        	   
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
        self.screen = pygame.display.get_surface()
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
        self.player_avatar = pygame.transform.scale(pygame.image.load('../images/hero_avatar.png'), (140, 150))
        self.comp_avatar = pygame.transform.scale(pygame.image.load('../images/compa_avatar.png'), (140, 150))
        self.wiz_avatar = pygame.transform.scale(pygame.image.load('../images/wizderp_avatar.png'), (140, 150))
        self.imageA = 0
    
    def set_scrolldelay(self, delay):
        self.scroll_delay = delay
    
    def set_dialog(self, dialog_list):
        self.page = 0
        self.pages = len(dialog_list)
        self.dialog = dialog_list
        self.shown = True
        self.text_pos = 0
        #if dialog_list[0] == '*':
           #self.imageA = self.comp_avatar
        
    
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
    
    def draw(self, surface, pos, color= BLACK):
        
        if self.shown and self.page < self.pages:
            my_font = pygame.font.SysFont('verdana', 15)
            self.screen.fill(self.border_color, pygame.Rect(505, 335, 150, 160))
            self.update_box()
            self.curr_dialog = self.dialog[self.page]
            if not self.curr_dialog.count("\"", 0, len(self.curr_dialog)) == 0:
            	surface.blit(self.comp_avatar, (510, 340))
            elif not self.curr_dialog.count("-", 0, len(self.curr_dialog)) == 0:
            	surface.blit(self.wiz_avatar, (510, 340))
            else:
            	surface.blit(self.player_avatar, (510,340))
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
                ren = my_font.render("  "+ word, True, color)
                w = ren.get_width()
                if xpos > self.image.get_width()-w:
                    ypos += ren.get_height()+3
                    xpos = 4
                    ren = my_font.render("  " + word, True, color)
                self.image.blit(ren, (xpos, ypos))
                xpos += w
            surface.blit(self.image, pos)
    
    def over(self):
        return self.shown != True
        
    def close(self):
       self.shown = False
       self.page = self.pages
