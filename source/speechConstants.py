import os, pygame, sys, helpers
from pygame.locals import *

INTRO_MESSAGE = [
"Everything comes into focus slowly. This room is filled with rubble, and....", 
"The creature stupidly walking around the room, it must be destroyed. "]

DOOR_LOCKED = [
"This path is barred. There must be a way to open it."]

ENEMY_ALIVE = [
"No. They cannot... must...",
"Destory them."]

SECOND_ROOM = [#the "1" allows for this to be held till an event happens, currently enemy death
"1",
"As the creature dies, the door opens.",
"Continue forward."]

THIRD_ROOM = [#the "1" allows for this to be held till an event happens, currently enemy death
"1",
"There is something large beyond this door.",
"Must tear it down."]

KILL_GRUNK =[
"1",
"This creature is about my size, how could it push those rocks?",
"This belt maybe? Mine now."]

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

COMPANION_OPEN = [
"\"Ugh, what happened? I must've gotten hit by that boulder when it fell. Crap, guess theres no going back no-\"",
"What is this thing saying. Cannot understand.",
"\"Listen, I don't know you but it loo-\"",
"How long will it babble? Kill it or arm it."]

COMPANION_KILL = [
"It is weak and defenseless. Drive a blade into it"]

COMPANION_SWORD_D = [
"Hand him the blade. Hold the bow up. Make X with arms.",
"That should make him realize I want him to defend me",
"Should be an effective shield at least."]
COMPANION_SWORD_A= [
"Hand him the blade. Hold the bow up. Make few slashes in the air.",
"That should convey to kill all he sees"]
COMPANION_BOW_D = [
"Hold up the ranged weapon. Hold a shot while he stands there and motion for him to move. Fire.",
"That should show that he needs to wait for a clear line of sight to shoot"]
COMPANION_BOW_A = [
"Hold up the ranged weapon. Pull a shot and dash to the side of him then fire.",
"That should let him know to strafe for a better position to shoot from"]

PART2_ROOM1 = [
"This part seems different. What is that thing lying on the floor?",
"It seems to have killed the same things I have. Does that make us allies?"]

PART2_ROOM2 = [
"Waves of them. They must all perish"]

PART2_ROOM3 = [
"5"]

PART2_ROOM4 = [
"5"]

FINAL_ROOM = [
"Huge, powerful, and about to die."]
THRONE_ROOM = [
"Nice chair.",
"\"We must be close, the leader must be down there\"",
"Real nice chair."]

EXAMINE_ROCK = [
"Rock. Yes."]

EXAMINE_PLATE = [
"This needs to be pressed down with more weight than myself."]