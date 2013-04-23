import os, pygame, sys, math, helpers
from pygame.locals import *

class Attack(pygame.sprite.Sprite):
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('../images/slash.png')
        self.original_image = self.image
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
        self.rot_inc = 0
        
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
            self.rot_image = self.original_image
            starting_x = player.rect.topleft[0] + 40
            starting_y = player.rect.topright[1] + 13
            self.starting_angle = math.degrees(math.asin((self.t1 / self.radius))) - .7
            self.ending_angle = 34.5
        elif direction == "down":#correct
            self.rot_image = pygame.transform.rotate(self.original_image, 180)
            starting_x = player.rect.topleft[0] - 8
            starting_y = player.rect.bottomleft[1]
            self.starting_angle = 34.5 #math.degrees(math.asin((self.t1 / self.radius))) + 1.4
            self.ending_angle = 31.5
        elif direction == "left":#correct
                self.rot_image = pygame.transform.rotate(self.original_image, 90)
                starting_x = player.rect.topleft[0] - 8
                starting_y = player.rect.topleft[1]

                self.starting_angle = 181 #math.degrees(math.asin((self.t1 / self.radius))) + 1.4
                self.ending_angle = 177.5

                self.starting_angle = 180.5 #math.degrees(math.asin((self.t1 / self.radius))) + 1.4
                self.ending_angle = 178

        elif direction == "right": #Good
                self.rot_image = pygame.transform.rotate(self.original_image, -90)
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
            self.rot_inc += 25
            #print self.angle

            x = (self.pcx + (self.radius * math.cos(self.angle)))
            y = (self.pcy + (self.radius * math.sin(self.angle)))
            self.image = pygame.transform.rotate(self.rot_image, self.rot_inc)
            
            self.rect.topleft = x - 4, y - 4
            
            self.angle -= .4
        else:
            self.ready = False
            self.rot_inc = 0
            self.done = True
            self.rect.topleft = 0,0
            
            
            
class R_Attack(pygame.sprite.Sprite):


        def __init__(self, position, target, direction):
                pygame.sprite.Sprite.__init__(self)
                if direction == "left":
                    self.image = pygame.image.load('../images/arrow_left.png')
                elif direction == "right":
                    self.image = pygame.image.load('../images/arrow_right.png')
                elif direction == "up":
                    self.image = pygame.image.load('../images/arrow_up.png')
                else:
                    self.image = pygame.image.load('../images/arrow_down.png')
                self.rect = self.image.get_rect()
                self.position = position
                
                self.rect.topleft = position[0], position[1]
                self.target = target
                if not (position[1] - target[1]) == 0:
                        self.slope = (position[0] - target[0])/(position[1] - target[1])
                        self.image = pygame.transform.rotate(self.image, -(self.slope))
                self.distance = math.sqrt(abs((position[0] - target[0])**2) + abs((position[1] - target[1])**2))
        
        def update(self):
                x = self.target[0]
                y = self.target[1]
                my_x = self.rect.topleft[0]
                my_y = self.rect.topleft[1]
                if x >= self.position[0]:
                        if y > self.position[1]:#bottom right
                                my_x -= (self.position[0] - self.target[0])/(self.distance / 10)
                                my_y -= (self.position[1] - self.target[1])/(self.distance / 10)
                        elif y == self.position[1]:
                                my_x += 6
                        else: #topright
                                my_x += -(self.position[0] - self.target[0])/(self.distance / 10)
                                my_y -= (self.position[1] - self.target[1])/(self.distance / 10)
                else:
                        if y > self.position[1]: #bottom left
                                my_x -= (self.position[0] - self.target[0])/(self.distance / 10)
                                my_y += -(self.position[1] - self.target[1])/(self.distance / 10)
                        elif y == self.position[1]:
                                my_x -= 6
                        else: #topleft
                                my_x -= -(self.target[0] - self.position[0])/(self.distance / 10)
                                my_y -= -(self.target[1] - self.position[1])/(self.distance / 10)
                self.rect.topleft = my_x, my_y
                "Window 675 x 500"
                if my_x > 700:
                        self.kill()
                if my_x < 0:
                        self.kill()
                if my_y > 550:
                        self.kill()
                if my_y < 0:
                        self.kill()
                        
                        
"""
THIS is for not shooting the player.
"""
class Lazor(pygame.sprite.Sprite):


        def __init__(self, position, target):
                pygame.sprite.Sprite.__init__(self)
                self.image = pygame.image.load('../images/lazor.png')
                self.rect = self.image.get_rect()
                self.position = position
                
                self.rect.topleft = position[0], position[1]
                self.target = target
                if not (position[1] - target[1]) == 0:
                        self.slope = (position[0] - target[0])/(position[1] - target[1])
                self.distance = math.sqrt(abs((position[0] - target[0])**2) + abs((position[1] - target[1])**2))
                self.traveled = 0
        
        def update(self):
                self.traveled += 1
                x = self.target[0]
                y = self.target[1]
                my_x = self.rect.topleft[0]
                my_y = self.rect.topleft[1]
                if x > self.position[0]:
                        if y > self.position[1]:#bottom right
                                my_x -= (self.position[0] - self.target[0])/(self.distance / 10)
                                my_y -= (self.position[1] - self.target[1])/(self.distance / 10)
                        elif y == self.position[1]:
                                my_x += 15
                        else: #topright
                                my_x += -(self.position[0] - self.target[0])/(self.distance / 10)
                                my_y -= (self.position[1] - self.target[1])/(self.distance / 10)
                else:
                        if y > self.position[1]: #bottom left
                                my_x -= (self.position[0] - self.target[0])/(self.distance / 10)
                                my_y += -(self.position[1] - self.target[1])/(self.distance / 10)
                        elif y == self.position[1]:
                                my_x -= 15
                        else: #topleft
                                my_x -= -(self.target[0] - self.position[0])/(self.distance / 10)
                                my_y -= -(self.target[1] - self.position[1])/(self.distance / 10)
                self.rect.topleft = my_x, my_y
                "Window 675 x 500"
                if my_x > 700:
                        self.kill()
                if my_x < 0:
                        self.kill()
                if my_y > 550:
                        self.kill()
                if my_y < 0:
                        self.kill()

						
						
"""
THIS is used as a walking stick.
"""
class LazorStick(pygame.sprite.Sprite):


        def __init__(self, position, target):
                pygame.sprite.Sprite.__init__(self)
                self.image = pygame.image.load('../images/lazor.png')
                self.rect = self.image.get_rect()
                self.position = position
                
                self.rect.topleft = position[0], position[1]
                self.target = target
                if not (position[1] - target[1]) == 0:
                        self.slope = (position[0] - target[0])/(position[1] - target[1])
                self.distance = math.sqrt(abs((position[0] - target[0])**2) + abs((position[1] - target[1])**2))
                self.traveled = 0
        
        def update(self):
                self.traveled += 1
                x = self.target[0]
                y = self.target[1]
                my_x = self.rect.topleft[0]
                my_y = self.rect.topleft[1]
                if x > self.position[0]:
                        if y > self.position[1]:#bottom right
                                my_x -= (self.position[0] - self.target[0])/(self.distance / 10)
                                my_y -= (self.position[1] - self.target[1])/(self.distance / 10)
                        elif y == self.position[1]:
                                my_x += 15
                        else: #topright
                                my_x += -(self.position[0] - self.target[0])/(self.distance / 10)
                                my_y -= (self.position[1] - self.target[1])/(self.distance / 10)
                else:
                        if y > self.position[1]: #bottom left
                                my_x -= (self.position[0] - self.target[0])/(self.distance / 10)
                                my_y += -(self.position[1] - self.target[1])/(self.distance / 10)
                        elif y == self.position[1]:
                                my_x -= 15
                        else: #topleft
                                my_x -= -(self.target[0] - self.position[0])/(self.distance / 10)
                                my_y -= -(self.target[1] - self.position[1])/(self.distance / 10)
                self.rect.topleft = my_x, my_y
                "Window 675 x 500"
                if my_x > 700:
                        self.kill()
                if my_x < 0:
                        self.kill()
                if my_y > 550:
                        self.kill()
                if my_y < 0:
                        self.kill()
                if self.traveled > 10:
						self.kill()
						
						
class Fire_Attack(pygame.sprite.Sprite):


        def __init__(self, position, target, direction):
                pygame.sprite.Sprite.__init__(self)
                
                self.image = pygame.image.load('../images/hero_placeholder.png')
               
                self.rect = self.image.get_rect()
                self.position = position
                
                self.rect.topleft = position[0], position[1]
                self.target = target
                if not (position[1] - target[1]) == 0:
                        self.slope = (position[0] - target[0])/(position[1] - target[1])
                        self.image = pygame.transform.rotate(self.image, -(self.slope))
                self.distance = math.sqrt(abs((position[0] - target[0])**2) + abs((position[1] - target[1])**2))
        
        def update(self, player):
                x = self.target[0]
                y = self.target[1]
                my_x = self.rect.topleft[0]
                my_y = self.rect.topleft[1]
                if x >= self.position[0]:
                        if y > self.position[1]:#bottom right
                                my_x -= (self.position[0] - self.target[0])/(self.distance / 10)
                                my_y -= (self.position[1] - self.target[1])/(self.distance / 10)
                        elif y == self.position[1]:
                                my_x += 6
                        else: #topright
                                my_x += -(self.position[0] - self.target[0])/(self.distance / 10)
                                my_y -= (self.position[1] - self.target[1])/(self.distance / 10)
                else:
                        if y > self.position[1]: #bottom left
                                my_x -= (self.position[0] - self.target[0])/(self.distance / 10)
                                my_y += -(self.position[1] - self.target[1])/(self.distance / 10)
                        elif y == self.position[1]:
                                my_x -= 6
                        else: #topleft
                                my_x -= -(self.target[0] - self.position[0])/(self.distance / 10)
                                my_y -= -(self.target[1] - self.position[1])/(self.distance / 10)
                self.rect.topleft = my_x, my_y
                "Window 675 x 500"
                if my_x > 700:
                        self.kill()
                if my_x < 0:
                        self.kill()
                if my_y > 550:
                        self.kill()
                if my_y < 0:
                        self.kill()
                        
                        
