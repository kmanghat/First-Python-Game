## Pygame library
import pygame
import objects

## Initialize window 
pygame.init()

screenWidth = 600
screenHeight = 600

## Create 500x500 window
win = pygame.display.set_mode((screenHeight,screenWidth))

clock = pygame.time.Clock()
## Caption Window
pygame.display.set_caption("Warrior vs Goblin")


## instance of warrior
warrior = objects.character(0,490,64,64,objects.walkRightWarrior,objects.walkLeftWarrior,objects.charWarrior)
goblin = objects.character(490,490,64,64,objects.walkRightGoblin,objects.walkLeftGoblin,objects.charGoblin)

def redrawWindow():
	## Fill screen after movement
	win.blit(objects.background,(0,0))
	##Create Character and display to screen
	warrior.draw(win)
	goblin.draw(win)
	for beam in beams:
		beam.draw(win)
	
	for spit in acid:
		spit.draw(win)
		
	pygame.display.update()
	
## Loop till close
run = True
beams = []
acid = []
while run:
	##FPS set to 27
	clock.tick(27)
	
	## If quit is pressed
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
			
	## To make sure beam is within bounds
	for beam in beams:
		if beam.y - beam.radius < goblin.hitbox[1] + goblin.hitbox[3] and beam.y + beam.radius > goblin.hitbox[1]:
			if beam.x + beam.radius > goblin.hitbox[0] and beam.x - beam.radius < goblin.hitbox[0]:
				beams.pop(beams.index(beam))
				
		if beam.x < 600 and beam.x > 0:
			beam.x += beam.vel
		else:
			beams.pop(beams.index(beam))
	
	for spit in acid:
		if spit.y - spit.radius < warrior.hitbox[1] + warrior.hitbox[3] and spit.y + spit.radius > warrior.hitbox[1]:
			if spit.x + spit.radius > warrior.hitbox[0] and spit.x - spit.radius < warrior.hitbox[0]:
				acid.pop(acid.index(spit))
				
		if spit.x < 600 and spit.x > 0:
			spit.x += spit.vel
		else:
			acid.pop(acid.index(spit))
			
	##Get pressed key
	keys = pygame.key.get_pressed()
	
	if keys[pygame.K_RSHIFT]:
		if warrior.right:
			facing = 1
			
		if warrior.left:
			facing = -1
			
		if warrior.right == True or warrior.left == True:
			if len(beams) < 2:
				beams.append(objects.projectile(round(warrior.x + warrior.width//2),round(warrior.y + warrior.height//2),6,(255,0,0),facing))
			
	## Move character in a ceratin direction with velocity
	## Boundaries are also set for character depending on velocity width and screen
	if(keys[pygame.K_LEFT]) and warrior.x > warrior.vel:
		warrior.x -= warrior.vel
		warrior.left = True
		warrior.right = False
		warrior.standing = False
		
		
	elif(keys[pygame.K_RIGHT]) and warrior.x < screenWidth - warrior.width - warrior.vel:
		warrior.x += warrior.vel
		warrior.right = True
		warrior.left = False
		warrior.standing = False
	
	else:
		warrior.standing = True
		warrior.walkCount = 0
		
	if warrior.isJump == False:
		if(keys[pygame.K_UP]) and warrior.y > warrior.jump:
			warrior.isJump = True
			warrior.right = False
			warrior.left = False
			warrior.walkCount = 0
			
	else:
		if warrior.jump >= -10:
			jumpMultiplier = 1
			if warrior.jump < 0:
				jumpMultiplier = -1
				
			warrior.y -= (warrior.jump**2)*0.5*jumpMultiplier
			warrior.jump -= 1
		
		else:
			warrior.isJump = False
			warrior.jump = 10
	
	## Movement for Goblin
	if keys[pygame.K_e]:
		if goblin.right:
			goblinFacing = 1
			
		if goblin.left:
			goblinFacing = -1
			
		if goblin.right == True or goblin.left == True:
			if len(acid) < 2:
				acid.append(objects.projectile(round(goblin.x + goblin.width//2),round(goblin.y + goblin.height//2),6,(34,139,34),goblinFacing))
			
	## Move character in a ceratin direction with velocity
	## Boundaries are also set for character depending on velocity width and screen
	if(keys[pygame.K_a]) and goblin.x > goblin.vel:
		goblin.x -= goblin.vel
		goblin.left = True
		goblin.right = False
		goblin.standing = False
		
		
	elif(keys[pygame.K_d]) and goblin.x < screenWidth - goblin.width - goblin.vel:
		goblin.x += goblin.vel
		goblin.right = True
		goblin.left = False
		goblin.standing = False
	
	else:
		goblin.standing = True
		goblin.walkCount = 0
		
	if goblin.isJump == False:
		if(keys[pygame.K_w]) and goblin.y > goblin.jump:
			goblin.isJump = True
			goblin.right = False
			goblin.left = False
			goblin.walkCount = 0
			
	else:
		if goblin.jump >= -10:
			jumpMultiplier = 1
			if goblin.jump < 0:
				jumpMultiplier = -1
				
			goblin.y -= (goblin.jump**2)*0.5*jumpMultiplier
			goblin.jump -= 1
		
		else:
			goblin.isJump = False
			goblin.jump = 10
	redrawWindow()
	
pygame.quit()
