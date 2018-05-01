
# platform_game.py
# By: {group members names}
# Date created: March 1st, 2018
# This program is a simple game that was made by SMC programming club members.
# Game is meant to be a simple platform game with eniemies, platforms, lives,
# a timer, and an end
# Built with the pygame library.

#Iimporting libraries that are needed to run the game
import pygame
import sys

# Importanting classes from seperate files in order to be organized
import lib.menu as menu

# declaring constants
WIDTH = 700
HEIGHT = 500

# Game needs Pyhthon 3 and higher in order to be ran without errors
if sys.version_info[0] < 3:
    raise "Ran with Python 2. Needed Python 3."


# initalizing pygame
pygame.init()

# defining the window
size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Platform Game")

# setting up clock for refresh rate
clock = pygame.time.Clock()

# varible used to control the game loop
done = False

# --- GAME LOOP ---
while not done:
    # setting up control for the game to quit when ordered to
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # *************************
    # ** GAME CODE GOES HERE **
    # *************************

    mouse  = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if 300+100 > mouse[0] > 300 and 400+50 > mouse[1] >400:
        pygame.draw.rect(screen,(0,255,0),(300,400,100,50))
        if click[0] == 1 : done = True
    else:
        pygame.draw.rect(screen,(0,200,0),(300,400,100,50))

    myfont = pygame.font.SysFont("freesansbold.ttf", 30)
    textSurf = myfont.render('Quit',False, (0,0,0))
    textRect = textSurf.get_rect(center=(350,425))
    screen.blit(textSurf, textRect)

    pygame.display.update()
    # *************************
    # **    END GAME CODE    **
    # *************************

    # setting frame rate at 60
    clock.tick(60)

# shutting down the game
pygame.quit()

