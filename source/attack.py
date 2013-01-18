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
            
    def use(self, player):
        
        if not self.ready:
            self.__prepare(player)
        else:
            self.__swing()
                
                
    def is_done(self):
        return self.done
    
    # Prepares all the self variables to swing
    def __prepare(self, player): # The double underscore makes a method private
        self.done = False
        self.pcx = player.rect.centerx
        self.pcy = player.rect.centery
            
        tempradius = (player.rect.width / 2) + 10
        tempt1 = player.rect.height / 2
        self.radius = float(tempradius)
        self.t1 = float(tempt1)
        self.starting_angle = math.degrees(math.asin((self.t1 / self.radius))) - .7
        #self.ending_angle = self.starting_angle - 180
        self.ending_angle = 34.5
        self.angle = self.starting_angle
        self.ready = True
        
        #This is used so that the attack sprite doesnt appear where it ended for a split second
        #after the next attack is called
        starting_x = player.rect.topleft[0] + 40
        starting_y = player.rect.topright[1] + 13
        self.rect.topleft = starting_x, starting_y 
    
    # Peforms this iteration of the actual swing    
    def __swing(self):
        if (self.angle >= self.ending_angle):
            x = (self.pcx + (self.radius * math.cos(self.angle)))
            y = (self.pcy + (self.radius * math.sin(self.angle)))
            
            self.rect.topleft = x - 4, y - 4
            
            self.angle -= .4
        else:
            self.ready = False
            self.done = True