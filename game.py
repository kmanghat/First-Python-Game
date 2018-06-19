## Pygame library
import pygame

## Initialize window 
pygame.init()

## Create 500x500 window
win = pygame.display.set_mode((500,500))

## Caption Window
pygame.display.set_caption("First Game")

## position, dimension and velocity of character
x = 50
y = 50
width = 40
height = 60
vel = 5

## Loop till close
run = True
while run:
	## delay to take input
	pygame.time.delay(100)
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
			
	##Get pressed key
	keys = pygame.key.get_pressed()
	
	## Move character in a ceratin direction with velocity
	if(keys[pygame.K_LEFT]):
		x -= vel
		
	if(keys[pygame.K_RIGHT]):
		x += vel
	
	if(keys[pygame.K_DOWN]):
		y += vel
	
	if(keys[pygame.K_UP]):
		y -= vel
	
	## Fill screen after movement
	win.fill((0,0,0))
	##Create Character and display to screen
	pygame.draw.rect(win, (255,0,0), (x,y,width,height))
	pygame.display.update()

pygame.quit()
