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
"What is...? That weapon looks inter...",
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

MEET_WIZARD = [
"-What have you done?!-",
"I can understand it?",
"-Of course you can understand me!-",
"It reads my mind?",
"-You have no mind! Fool! You are but a construct like everything else here!-",
"-I created you!-",
"-Your job was to keep the discarded section clean by destroying the broken models!-",
"-How did you even get over here and why did you destory the functional ones?!-",
"I was supposed to destroy...",
"-Ugh. I made you too powerful. But all is not lost. I can always make more.-",
"-But what you killed down there, that will no be remade.-",
"-Instead, you will take its place.-",
"-Come here, I will end your urge to destroy and leave you here to gaurd the throne-"]

FIGHT_WIZARD = [
"End my urge? Creature. My urge will never end."
]

ACCEPT_WIZARD = [
"-Good, I knew you would obey. I did impart some of my own mind into you afterall-"
]

FREEDOM_END= [
"This place is empty. If he was truly my creator then I now have no purpose.",
"This does not bother me. I will leave."
]

MASTER_END =[
"This was indeed a nice chair.",
"My new feeling is clear: unless it's that wizard, anything that comes in here dies",
"This is good"
]

COMPANION_DEATH = [
"Lazy creature. It gets covered in red then just lays there. I'm leaving without it"]
