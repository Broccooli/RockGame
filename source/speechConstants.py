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
"What a terrible position to be in.",
"Why does the door look locked?"]

FIFTH_ROOM = [
"These enemies can be easily crushed."]

SIXTH_ROOM = [
"This must have been made by someone.",
"I made it.",
"I made it?"]

KILL_SQUIK = [
"1",
"The gel protecting him is gone, but this gauntlet looks perfect for breaking rocks"]

FLOWERS = [
"What is that design? That switch..."]

NINTH_ROOM = [
"Must be careful of the trap I placed here.",
"Wait, trap?"]

FIGHT_TAHZI = [
"What is...? That weapon looks inter-",
"Move!"]