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
            
    def attack(self, player):
        
        if not self.ready:
            self.done = False
            self.pcx = player.rect.centerx
            self.pcy = player.rect.centery
            
            tempradius = (player.rect.width / 2) + 10
            tempt1 = player.rect.height / 2
            self.radius = float(tempradius)
            self.t1 = float(tempt1)
            self.starting_angle = math.degrees(math.asin((self.t1 / self.radius))) - .7
            #self.ending_angle = self.starting_angle - 180
            self.ending_angle = 35.0
            self.angle = self.starting_angle
            self.ready = True
        else:
            if (self.angle >= self.ending_angle):
                print self.angle
                x = (self.pcx + (self.radius * math.cos(self.angle)))
                y = (self.pcy + (self.radius * math.sin(self.angle)))
                
                self.rect.topleft = x - 5, y - 5
                
                self.angle -= .4
            else:
                self.ready = False
                self.done = True
                
                
    def is_done(self):
        return self.done
        