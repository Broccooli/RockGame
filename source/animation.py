import os, pygame,sys
from pygame.locals import *

class Animation():

    def __init__(self, frames):
        self.frame = 0
        self.anim = frames
        self.anim_length = len(frames) - 1

    def update(self):
        if (self.frame == self.anim_length):
            self.frame = 0
            return self.anim[self.anim_length]
        else:
            self.frame += 1
            return self.anim[self.frame - 1]
        
