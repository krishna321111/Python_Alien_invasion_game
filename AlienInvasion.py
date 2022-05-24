import sys

import pygame

import random

import math

from pygame import mixer

# Initializing pygame to use it's features
pygame.init()

#creating game window
screen = pygame.display.set_mode((800,600))

# Title of game
pygame.display.set_caption("Alien Invasion")

#Adding own background:
background = pygame.image.load('/home/krishna/gamepython/AlienInvasion_gamefile/game_images/background.png')

# Adding Shuttle to the game
shuttle_img = pygame.image.load('/home/krishna/gamepython/AlienInvasion_gamefile/game_images/rocket1.png')
shuttleX = 368
shuttleY = 520

	
def shuttle(x,y):
	screen.blit(shuttle_img,(x, y))
	
shuttleX_change = 0

# Adding alien to the game

# ALIEN1:
alien1_img = []
alien1X = []
alien1Y = []
alien1X_change = []
alien1Y_change = []
no_of_first_aliens = 5

for i in range(no_of_first_aliens):
	alien1_img.append(pygame.image.load('/home/krishna/gamepython/AlienInvasion_gamefile/game_images/alien2.png'))
	alien1X.append(random.randint(0,800))
	alien1Y.append(random.randint(0,150))
	alien1X_change.append(5)
	alien1Y_change.append(40)

def alien1(x, y, i):
	screen.blit(alien1_img[i] , (x , y))



#adding bullets ,, in bullet_state , fire = bullet moving & ready = can't be seen
bullet_img = pygame.image.load('/home/krishna/gamepython/AlienInvasion_gamefile/game_images/bullet.png')	
bulletX = 380
bulletY = 520	
bulletX_change = 0
bulletY_change = 8
bullet_state = "ready"

def fire_bullet(x,y):
	global bullet_state
	bullet_state = "fire"
	screen.blit(bullet_img,(x+10,y))
	

#Defining collisiom of bullet and alien:
def yescollision(bulletX,bulletY,alien1X,alien1Y):
	distance = math.sqrt(math.pow(bulletX - alien1X , 2) + math.pow(bulletY - alien1Y , 2))
	
	if distance <= 50:
		return True
	else:
		return False
	
#score of the game:

score_value = 0
font = pygame.font.Font('/home/krishna/gamepython/AlienInvasion_gamefile/gamefont/gamefont.ttf', 24)
textX = 10
textY = 10

def show_score(x, y):
	score = font.render("SCORE : " + str(score_value), True , (255,255,255))
	screen.blit(score, (x, y))
	
	
#GAME OVER TEXT

over = pygame.font.Font('/home/krishna/gamepython/AlienInvasion_gamefile/gamefont/gamefont.ttf', 100)
overX = 100
overY = 250

def game_over_text(x,y):
	game_over = over.render("GAME OVER" , True , (255,0,0))
	screen.blit(game_over, (x,y))
	
	
	
#background sound

mixer.music.load('/home/krishna/gamepython/AlienInvasion_gamefile/game_music/background.mp3')
mixer.music.play(-1)


#border
border = pygame.image.load('/home/krishna/gamepython/AlienInvasion_gamefile/game_images/border.png')


#Main While loop that runs the game
running = True
while running:
	
	#Background color of screen, RGB:
	screen.fill((0,0,0))
	
	#making background image appear on screen everytime.
	screen.blit(background, (0,0))
	
	# Border
	
	screen.blit(border, (0,500))
	
	""" Every event take place in this loop."""
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	
		# Moving the shuttle on the basis of command goven by keystrokes.
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RIGHT:
				shuttleX_change = 10
			if event.key == pygame.K_LEFT:
				shuttleX_change = -10
			if event.key == pygame.K_SPACE:
				if bullet_state == "ready":
					bullet_sound = mixer.Sound('/home/krishna/gamepython/AlienInvasion_gamefile/game_music/laser.wav')
					bullet_sound.play()
					bulletX = shuttleX
					fire_bullet(bulletX, bulletY)
			
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
				shuttleX_change = 0
				
				
	shuttleX += shuttleX_change
	
	#setting boundary for shuttle
	if shuttleX <= 0:
		shuttleX = 0
	if shuttleX >= 746:
		shuttleX =  746
		
	# Moving the aliens theirself:
	
	alien1X[i] += alien1X_change[i]
	
	
	#setting Boundary for alien1:
	for i in range(no_of_first_aliens):
		
		#Game over:
		if alien1Y[i] > 470:
			for j in range(no_of_first_aliens):
				alien1Y[j] = 2000
				
			game_over_text(overX, overY)
			break
			
			
		#moving aliens
		if alien1X[i] <= 0 :
			alien1X_change[i] = 5
			alien1Y[i] += alien1Y_change[i]
		if alien1X[i] >= 736:
			alien1X_change[i] = -5
			alien1Y[i] += alien1Y_change[i]
		
		
		# For after yescollision
		collision = yescollision(bulletX,bulletY,alien1X[i],alien1Y[i])
		if collision:
			collide_sound = mixer.Sound('/home/krishna/gamepython/AlienInvasion_gamefile/game_music/explode.wav')
			collide_sound.play()
			bulletY = 520
			bullet_state = "ready"
			score_value += 1
			alien1X[i]= random.randint(0,800)
			alien1Y[i] = random.randint(0,100)
			
			
		# Moving the aliens theirself:
	
		alien1X[i] += alien1X_change[i]
	
		#showing alien in every screen
		#ALIEN1:
		alien1(alien1X[i], alien1Y[i] , i)
		
	# Moving the bullet
	if bulletY <= 0 :
		bulletY = 520
		bullet_state = 'ready'
	
	if bullet_state == "fire":
		fire_bullet(bulletX,bulletY)
		bulletY -= bulletY_change
		
		
	#showing shuttle in every screen
	shuttle(shuttleX, shuttleY)
	
	#showing Text
	show_score(textX,textY)
	
	#displaying all the changes as updates
	pygame.display.update()

