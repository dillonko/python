import pygame, sys, random
from pygame.locals import *

pygame.init()

screen=pygame.display.set_mode((1600,1120),0,32)
mouse_c=pygame.image.load(you).convert_alpha()

#Variables for shapes

BLUE=(0,64,128)
WHITE=(255,255,255)
pos1=(0,0)
pos2=(0,1130)
pos3=(1600,0)
pos4=(1600,1130)
randpos1=random.randint(0, 1120)
randpos2=random.randint(0, 1600)
radius=(5)

#Variables for shapes

x,y=770,560
movex, movey=0,0

#Controls

while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		if event.type==KEYDOWN:
			if event.key==K_LEFT:
				movex=-4
			elif event.key==K_RIGHT:
				movex=+4
			elif event.key==K_UP:
				movey=-4
			elif event.key==K_DOWN:
				movey=+4
		if event.type==KEYUP:
			if event.key==K_LEFT:
				movex=0
			elif event.key==K_RIGHT:
				movex=0
			elif event.key==K_UP:
				movey=0
			elif event.key==K_DOWN:
				movey=0
#Controls

screen.lock()
pygame.draw.circle(screen, WHITE, (random.randint(0, 1600), random.randint(0, 1600)), radius)
screen.unlock()

x+=movex
y+=movey

#Collision
if y < 0:
	y = 0
elif y > 1080:
	y = 1080
if x < 0:
	x = 0
elif x > 1550:
	x = 1550
#Collision
#Dots

screen.blit(mouse_c,(x,y))
pygame.display.update() 