import os, pygame, sys, math
from pygame.locals import *

class Attack(pygame.sprite.Sprite):
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('../images/attack.png')
        self.rect = self.image.get_rect()
        self.position = None
        self.ready = False
        
        self.pcx = None
        self.pcy = None
        self.radius = None
        self.t1 = None
        self.starting_angle = None
        self.ending_angle = None
        self.angle = None
        
        self.done = True
            
    def use(self, player, direction):
        
        if not self.ready:
            self.__prepare(player, direction)
        else:
            self.__swing()
                
                
    def is_done(self):
        return self.done
    
    # Prepares all the self variables to swing
    def __prepare(self, player, direction): # The double underscore makes a method private
        self.done = False
        self.pcx = player.rect.centerx
        self.pcy = player.rect.centery
            
        tempradius = (player.rect.width / 2) + 10
        tempt1 = player.rect.height / 2
        self.radius = float(tempradius)
        self.t1 = float(tempt1)
        if direction == "up": #This one is good
                starting_x = player.rect.topleft[0] + 40
                starting_y = player.rect.topright[1] + 13
        	self.starting_angle = math.degrees(math.asin((self.t1 / self.radius))) - .7
        	self.ending_angle = 34.5
        elif direction == "down":#correct
                starting_x = player.rect.topleft[0] - 8
                starting_y = player.rect.bottomleft[1]
        	self.starting_angle = 34.5 #math.degrees(math.asin((self.t1 / self.radius))) + 1.4
        	self.ending_angle = 31.5
        elif direction == "left":#correct
                starting_x = player.rect.topleft[0]
                starting_y = player.rect.topleft[1] + 8

        	self.starting_angle = 181 #math.degrees(math.asin((self.t1 / self.radius))) + 1.4
        	self.ending_angle = 177.5

        	self.starting_angle = 180.5 #math.degrees(math.asin((self.t1 / self.radius))) + 1.4
        	self.ending_angle = 178

        elif direction == "right": #Good
                starting_x = player.rect.topright[0]
                starting_y = player.rect.topright[1] + 8
        	self.starting_angle = 39 #math.degrees(math.asin((self.t1 / self.radius))) + .7 
        	self.ending_angle = 36.5
        #self.ending_angle = self.starting_angle - 180
        #self.ending_angle = 34.5
        self.angle = self.starting_angle
        self.ready = True
        
        #This is used so that the attack sprite doesnt appear where it ended for a split second
        #after the next attack is called
        #starting_x = player.rect.topleft[0] + 40
        #starting_y = player.rect.topright[1] + 13
        self.rect.topleft = starting_x, starting_y 
    
    # Peforms this iteration of the actual swing    
    def __swing(self):
        if (self.angle >= self.ending_angle):

            print self.angle

            #print self.angle

            x = (self.pcx + (self.radius * math.cos(self.angle)))
            y = (self.pcy + (self.radius * math.sin(self.angle)))
            
            self.rect.topleft = x - 4, y - 4
            
            self.angle -= .4
        else:
            self.ready = False
            self.done = True