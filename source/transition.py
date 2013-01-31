import os, pygame, sys, helpers
from pygame.locals import *

class Transition():    
    
    def __init__(self, surface, speed = 40):
        self.surface = pygame.Surface((surface.get_width(), surface.get_height()))
        self.speed = speed
        self.state = 0
        self.curr_alpha = 10
        self.done = False
        self.btw = 0

    def do(self):
        if self.state == 0:
            self.done = False
            self.surface.set_alpha(self.curr_alpha)
            self.surface.fill( (0,0,0) )
            self.curr_alpha += 10

            if self.curr_alpha >= 250:
                self.state = 1
                self.curr_alpha = 0

            return self.surface

        if self.state == 1:
            self.black = False
            self.surface.fill( (self.btw,self.btw,self.btw) )
            self.btw += 10
            
            if self.btw >= 250:
                self.state = 2
                self.curr_alpha = 255

            return self.surface

        if self.state == 2:
            self.surface.set_alpha(self.curr_alpha)
            self.surface.fill( (255,255,255) )
            self.curr_alpha -= 10
            
            if self.curr_alpha <= 10:
                self.done = True
                self.__reset()
                

            return self.surface

    def is_done(self):
        return self.done

    def __reset(self):
        self.curr_alpha = 10
        self.state = 0
        self.btw = 0
