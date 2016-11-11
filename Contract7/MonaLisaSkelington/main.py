import pygame, sys, colorsys
from pygame.locals import *
from time import sleep
width = 396
height = 599

screen = pygame.display.set_mode((width, height), 0, 32)  # Setting screen size

# --- Defining loading functions ---

# function to load image from path, remember to omit 'Images/' from path
def imageload(path):
    return pygame.image.load('Images/' + path)


# function to display images
def appear(image):
    screen.blit(image, (0, 0), None, 0)


# --- Loading in image layers and resizing ---

# base layer
baseImage = imageload('Mona_Lisa.jpg')
skell = imageload('Mona_Lisa_skell.jpg')

while True:
    pressed = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    if pressed[K_i]:
        print "i pressed"
        for x in range(baseImage.get_width()):
            for y in range(baseImage.get_height()):
                RGBA = baseImage.get_at((x, y))
                for i in range(3):
                    # Invert RGB, but not Alpha
                    RGBA[i] = 255 - RGBA[i]
                baseImage.set_at((x, y), RGBA)

    appear(baseImage)

    if pressed[K_s]:
        print "s pressed"
        appear(skell)
        #sleep(60)

    pygame.display.update()
