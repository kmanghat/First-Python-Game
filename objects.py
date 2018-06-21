import pygame

## Import images for warrior
walkRightWarrior = [pygame.image.load('Images/R1.png'),pygame.image.load('Images/R2.png'),pygame.image.load('Images/R3.png'),pygame.image.load('Images/R4.png'),pygame.image.load('Images/R5.png'),pygame.image.load('Images/R6.png'),pygame.image.load('Images/R7.png'),pygame.image.load('Images/R8.png'),pygame.image.load('Images/R9.png')]
walkLeftWarrior = [pygame.image.load('Images/L1.png'),pygame.image.load('Images/L2.png'),pygame.image.load('Images/L3.png'),pygame.image.load('Images/L4.png'),pygame.image.load('Images/L5.png'),pygame.image.load('Images/L6.png'),pygame.image.load('Images/L7.png'),pygame.image.load('Images/L8.png'),pygame.image.load('Images/L9.png')]
background = pygame.image.load('Images/bg.jpg')
charWarrior = pygame.image.load('Images/standing.png')

## Import Images for goblin
walkLeftGoblin = [pygame.image.load('Images/L1E.png'),pygame.image.load('Images/L2E.png'),pygame.image.load('Images/L3E.png'),pygame.image.load('Images/L4E.png'),pygame.image.load('Images/L5E.png'),pygame.image.load('Images/L6E.png'),pygame.image.load('Images/L7E.png'),pygame.image.load('Images/L8E.png'),pygame.image.load('Images/L11E.png')]
walkRightGoblin = [pygame.image.load('Images/R1E.png'),pygame.image.load('Images/R2E.png'),pygame.image.load('Images/R3E.png'),pygame.image.load('Images/R4E.png'),pygame.image.load('Images/R5E.png'),pygame.image.load('Images/R6E.png'),pygame.image.load('Images/R7E.png'),pygame.image.load('Images/R11E.png'),pygame.image.load('Images/R11E.png')]
charGoblin = pygame.image.load('Images/goblinStanding.png')


## position, dimension and velocity of character
class character:
	def __init__(self,x,y,width,height,walkRight,walkLeft,char):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.vel = 5
		self.isJump = False
		self.jump = 10
		self.right = False
		self.left = False
		self.walkCount = 0
		self.standing = True
		self.walkRight = walkRight
		self.walkLeft = walkLeft
		self.char = char
		self.hitbox = (self.x+17, self.y+2, 31, 57)
		self.health = 10
		self.alive = True
		
	def draw(self,win):
		## Loop frames 27/3 = 9 images for left and right
		if self.walkCount + 1 >= 27:
			self.walkCount = 0
			
		if not(self.standing):
			if self.left:
				win.blit(self.walkLeft[self.walkCount//3], (self.x,self.y))
				self.walkCount += 1
			elif self.right:
				win.blit(self.walkRight[self.walkCount//3], (self.x,self.y))
				self.walkCount += 1
		else:
			if self.left:
				win.blit(self.walkLeft[0], (self.x, self.y))
			elif self.right:
				win.blit(self.walkRight[0], (self.x, self.y))
			else:
				win.blit(self.char,(self.x,self.y))
				
		pygame.draw.rect(win, (255,0,0), (self.hitbox[0], self.hitbox[1] - 20,50,10))
		pygame.draw.rect(win, (0,128,0), (self.hitbox[0], self.hitbox[1] - 20,50 - ((5) * (10 - self.health)),10))
		self.hitbox = (self.x+17, self.y+2, 31, 57)

	def hit(self):
		if self.health > 0:
			self.health -= 1
## Attack
class projectile:
	def __init__(self,x,y,radius,color,facing):
		self.x = x
		self.y = y
		self.radius = radius
		self.color = color
		self.facing = facing
		self.vel = 10*facing
		
	def draw(self,win):
		pygame.draw.circle(win,self.color,(self.x,self.y), self.radius)
