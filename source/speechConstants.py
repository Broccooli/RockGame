import os, pygame, sys, helpers
from pygame.locals import *

INTRO_MESSAGE = [
"Everything comes into focus slowly. You are in a rublled filled room. Not alone. ", 
"The creature stupidly walking around the room, you have a burning urge to kill it. "]

SECOND_ROOM = [#the "1" allows for this to be held till an event happens, currently enemy death
"1",
"As the monster dies, the door opens.",
"Continue forward."]