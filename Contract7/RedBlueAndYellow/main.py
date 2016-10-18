import pygame, sys, colorsys
from pygame.locals import *

width = 592
height = 600

screen = pygame.display.set_mode((width, height), 0, 32)  # Setting screen size

# --- Defining loading functions ---

# function to load image from path, remember to omit 'Images/' from path
def imageload(path):
    return pygame.image.load('Images/' + path)


# function to display images
def resize (image):
    image = pygame.transform.scale(image, (width, height))
    return image


def appear(image):
    screen.blit(image, (0, 0), None, 0)


# --- Loading in image layers and resizing ---

# base layer
baseImage = imageload('BaseImage.jpg')
baseImage = resize(baseImage)
appear(baseImage)


while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
