import pygame, sys, colorsys
from pygame.locals import *
from PIL import Image

WIDTH = 562
HEIGHT = 568
WHITE = 255, 255, 255
timer = 0
screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)  # Setting screen size
clock = pygame.time.Clock()

# --- Defining loading functions ---

# function to load image from path, remember to omit 'Images/' from path
def imageload(path):
    return pygame.image.load('Images/' + path)


def appear(image):
    screen.blit(image, (0, 0), None, 0)


# --- Loading in image layers and saving flipped version ---

# base layer
baseImage = imageload('BaseImage.png')
appear(baseImage)

trImage = pygame.transform.flip(baseImage, 1, 0)
blImage = pygame.transform.flip(baseImage, 0, 1)
brImage = pygame.transform.flip(baseImage, 1, 1)



while True:

    # cycles through flipped images
    if timer < 1:
        appear(trImage)
    elif timer < 2:
        appear(brImage)
    elif timer < 3:
        appear(blImage)
    elif timer < 4:
        appear(baseImage)
    elif timer < 5:
        timer = 0

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    clock.tick(30)
    timer += 0.1
    pygame.display.update()
