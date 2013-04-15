from HUB import Menu
import pygame, sys
from pygame.locals import *

class TitleScreen():

    def __init__(self, surface):
        self.s = surface
        self.background = pygame.image.load('../images/title.png')
        self.menu = Menu((480, 51), (255, 255, 204), 
                         (102, 0, 0), pygame.font.SysFont('Verdana', 15, True),
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
