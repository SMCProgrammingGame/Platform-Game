# library
import pygame
import sys
from PlayerClass import Player
from TileClass import Tile
from PIL import Image

# version check
if sys.version_info[0] < 3:
    raise "Ran with Python 2. Needed Python 3."

# variables
W = 640
H = 480
FPS = 30
white = (255, 255, 255)

# init and create pygame window
pygame.init()
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption('Prog Club Game')
screen.fill(white)
clock = pygame.time.Clock()

# create sprite group
all_sprites = pygame.sprite.Group()

# load in image of level
im = Image.open('New Piskel.png')
imW, imH = im.size
pix = im.load()

gameTiles = []
for y in range(0, imH):
    for x in range(0, imW):
        gameTiles.append(Tile(x, y, pix[x, y], H, imH))
all_sprites.add(gameTiles)

for x in gameTiles:
    if x.

# initialize Player object and add it to the sprite group
player = Player(W, H)
all_sprites.add(player)

# game loop
running = True
while running:
    # process inputs (events)
    for event in pygame.event.get():
        # checks for a closing window
        if event.type == pygame.QUIT:
            running = False

    # update
    all_sprites.update()

    # draw / render
    screen.fill(white)
    all_sprites.draw(screen)

    # flip display
    pygame.display.flip()

    # controls loop speed
    clock.tick(FPS)
pygame.quit()