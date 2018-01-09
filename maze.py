"""
Save MacGyver !
A Game in wich we must help MacGyver finding is way around a maze
in order to escape he must reach the exit, but before then he must
pick up objects along the way in order to conceive a siringue of chemical
so he can put to sleep the guard at the exit !

 Python Script
 Files : maze.py, classes.py, constantes.py, level.txt + images
 """

# Import of the libraries needed
import pygame
from pygame.locals import *
from constantes import *
from classes import *

# Init of the Pygame library
pygame.init()

# Displaying the windows
WINDOW = pygame.display.set_mode((WINDOW_SIZE, 480))
# setting the height to 480 so we have an upper black margin
# Icone
ICONE = pygame.image.load(MAC_GYVER).convert_alpha()
pygame.display.set_icon(ICONE)
# Title
pygame.display.set_caption(WINDOW_TITLE)


# displaying a background for the tile of the maze
BACKGROUND_TILES = pygame.image.load(BACKGROUND).convert()
WINDOW.blit(BACKGROUND_TILES, (30, 30))
# the background is streched from below the black margin to the opposite corner

# displaying the character .png
CHAR_IMG = pygame.image.load(MAC_GYVER).convert_alpha()  # Add the png and transparency

# displaying the walls of the maze
WALL = pygame.image.load(WALL).convert()

# displaying the objects png's
TUBEIMG = pygame.image.load(TUBE).convert_alpha()
NEEDLEIMG = pygame.image.load(NEEDLE).convert_alpha()
ETHERIMG = pygame.image.load(ETHER).convert_alpha()


# refreshing the screen for the background to be visible over the default one
pygame.display.flip()

# Variable for the infinite loop
CONTINUE_GAME = 1

# Variables to check if the items have been picked or not:
TUBENOTPICKED = True
ETHERNOTPICKED = True
NEEDLENOTPICKED = True

GAME_WON = False
GAME_LOOSE = False

pygame.key.set_repeat(400, 30)  #Moving MaGyver by maintening a arrow_key pressed

LEVEL = Level('Level.txt')
LEVEL.generate()
LEVEL.display(WINDOW)
MAC = Char(CHAR_IMG, LEVEL)
TUBE = loot(TUBEIMG, LEVEL)
TUBE.display(TUBEIMG, WINDOW)
NEEDLE = loot(NEEDLEIMG, LEVEL)
NEEDLE.display(NEEDLEIMG, WINDOW)
ETHER = loot(ETHERIMG, LEVEL)
ETHER.display(ETHERIMG, WINDOW)


# infinite loop
while CONTINUE_GAME:

    pygame.time.Clock().tick(30)  # Limiting the loop speed to 30f/s to save processor ressources

    for event in pygame.event.get():    #Seeking every events happening while the game is running
        if event.type == quit:  # If any of these events is QUIT type
            CONTINUE_GAME = 0   # Loop is stopped and the game windows is closed

        # Keyboard touch used to moove MacGyver:
        elif event.type == KEYDOWN:
            if event.key == K_DOWN:  # If ARROW DOWN pressed
                MAC.mooving('down')
            elif event.key == K_UP:
                MAC.mooving('up')
            elif event.key == K_LEFT:
                MAC.mooving('left')
            elif event.key == K_RIGHT:
                MAC.mooving('right')


    # Re-pasting after the events
    WINDOW.blit(BACKGROUND_TILES, (0, 30))
    # the background is streched from below the black margin to the opposite corner
    LEVEL.display(WINDOW)
    WINDOW.blit(MAC.Image, (MAC.x, MAC.y))

    if TUBENOTPICKED:
        WINDOW.blit(TUBE.Loot_Image, (TUBE.x, TUBE.y))
    if (MAC.x, MAC.y) == (TUBE.x, TUBE.y):
        TUBENOTPICKED = False
        WINDOW.blit(TUBE.Loot_Image, (0, 0))


    if NEEDLENOTPICKED:
        WINDOW.blit(NEEDLE.Loot_Image, (NEEDLE.x, NEEDLE.y))
    if (MAC.x, MAC.y) == (NEEDLE.x, NEEDLE.y):
        NEEDLENOTPICKED = False
        WINDOW.blit(NEEDLE.Loot_Image, (10, 0))


    if ETHERNOTPICKED:
        WINDOW.blit(ETHER.Loot_Image, (ETHER.x, ETHER.y))
    if (MAC.x, MAC.y) == (ETHER.x, ETHER.y):
        ETHERNOTPICKED = False
        WINDOW.blit(ETHER.Loot_Image, (30, 0))


    # refreshing screen
    pygame.display.flip()


    # EndGame Victory or loose
    if LEVEL.structure[MAC.case_y][MAC.case_x] == 'a':  # If MacGyver reach the guard :
        if TUBENOTPICKED is False and NEEDLENOTPICKED is False and ETHERNOTPICKED is False:
        # If every objects have been looted, he won.
            GAME_WON = True
        else:
            GAME_LOOSE = True  # Else it's game over !


    if GAME_WON is True:
        WINDOW.blit(BACKGROUND_TILES, (0, 30))
        # draw over everything on the screen now by re-drawing the background
        FONT = pygame.FONT.Font(None, 25)
        TEXT = FONT.render("You won ! MacGyver is safe thanks to you !", 1, (255, 255, 255))
        # Display the text in white with rounded edge
        TEXTRECT = TEXT.get_rect()
        TEXTRECT.centerx, TEXTRECT.centery = WINDOW_SIZE / 2, WINDOW_SIZE / 2  # Centering the text
        WINDOW.blit(TEXT, TEXTRECT)

        pygame.display.flip()

    if GAME_LOOSE is True:
        WINDOW.blit(BACKGROUND_TILES, (0, 30))
        # draw over everything on the screen now by re-drawing the background
        FONT = pygame.FONT.Font(None, 25)
        TEXT = FONT.render("Game over! You just died.", 1, (255, 255, 255))
        # Display the text in white with rounded edge
        TEXTRECT = TEXT.get_rect()
        TEXTRECT.centerx, TEXTRECT.centery = WINDOW_SIZE / 2, WINDOW_SIZE / 2
        WINDOW.blit(TEXT, TEXTRECT)

        pygame.display.flip()
