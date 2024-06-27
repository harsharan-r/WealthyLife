from GameLogic import *
import sys
import time
import os

pygame.init()
pygame.mixer.init()

#setting game and menu variables
game_state = True

#adding window name
pygame.display.set_caption("Wealthy Life")

#setting framerate 
FPS = 60

background_music.set_volume(0.1)
background_music.play(loops=-1)

while True:
	clock.tick(FPS)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()


	
	
	

	pygame.display.update()
	