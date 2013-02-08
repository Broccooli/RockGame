import os, pygame, sys, helpers
from pygame.locals import *

INTRO_MESSAGE = [
"Everything comes into focus slowly. You are in a rublled filled room. Not alone. ", 
"The creature stupidly walking around the room, you have a burning urge to kill it. "]

DOOR_LOCKED = [
"This path is barred. There must be a way to open it."]

ENEMY_ALIVE = [
"No. They cannot... You must...",
"Destory them."]

SECOND_ROOM = [#the "1" allows for this to be held till an event happens, currently enemy death
"1",
"As the monster dies, the door opens.",
"Continue forward."]

THIRD_ROOM = [#the "1" allows for this to be held till an event happens, currently enemy death
"1",
"There is something large beyond this door.",
"Tear it down."]

KILL_GRUNK =[
"1",
"This creature is about your size, how could it push those rocks?",
"This belt maybe? Best to take it"]

FOURTH_ROOM = [
"Where are they? Proceed without thinking.",
"Why does the door look locked?"]

FIFTH_ROOM = [
"These enemies can be easily crushed."]