
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

# Used to create the enemies and hero.


class Characters:
    CharacterCount = 0

    def __int__(self, name):
        self.name = name
        Characters.CharacterCount += 1

    def load_image(self, image):
        char = pygame.image.load(image).convert_alpha()
        self.rect = char.get_rect()
        return char

    def bounded_movements(self):

        global XMovement, YMovement, enemy_X_movement, enemy_Y_movement
        rect = self.rect
        if XMovement + rect.right > WIDTH:
            XMovement = WIDTH - rect.right
        elif XMovement < 0:
            XMovement = 1
        else:
            XMovement += cx
        if YMovement > HEIGHT - rect.bottom - FLOOR:
            YMovement = HEIGHT - rect.bottom - FLOOR
        elif YMovement < 0:
            YMovement = 1
        else:
            YMovement += cy
# Change values below to speed up or reduce the enemy movements.
        if XMovement - enemy_X_movement > 0:
            enemy_X_movement += 2
        else:
            enemy_X_movement += -2
        if YMovement - enemy_Y_movement > 0:
            enemy_Y_movement += 2
        else:
            enemy_Y_movement += -2

# The controls are the WSAD letters instead of the arrow key...


def controls():
    global cx, cy
    for event in pygame.event.get():
        if event.type == pygame.locals.KEYDOWN and event.key == pygame.K_SPACE:
            True
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_q]:
        pygame.quit()
    if pressed[pygame.K_a]:
        cx = -5
    elif pressed[pygame.K_d]:
        cx = 5
    elif pressed[pygame.K_w]:
        cy = -5
    elif pressed[pygame.K_s]:
        cy = 5

# --- GAME LOOP ---


def game_loop():
    global cx, cy
    while True:
        controls()
        hero.bounded_movements()
        cy = cx = 0
        screen.fill(white)
        screen.blit(background1, (0, 0))
        screen.blit(hero_png, (XMovement, YMovement))
        screen.blit(enemy_png, (enemy_X_movement, enemy_Y_movement))
        pygame.display.flip()
        clock.tick(60)
        pygame.display.update()
    # *************************
    # **    END GAME CODE    **
    # *************************

    # setting frame rate at 60
    clock.tick(60)

# shutting down the game
pygame.quit()

