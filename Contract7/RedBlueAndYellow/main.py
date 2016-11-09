import pygame, sys, colorsys
from pygame.locals import *
from PIL import Image

WIDTH = 562
HEIGHT = 568
timer = 0
screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)  # Setting screen size
clock = pygame.time.Clock()

# --- Defining loading functions ---

# function to load image from path, remember to omit 'Images/' from path
def imageload(path):
    return pygame.image.load('Images/' + path)


def appear(image, x, y):
    screen.blit(image, (x, y), None, 0)


# --- Loading in image layers and saving flipped version ---

# base layer
baseImage = imageload('BaseImage.png')
baseImage = pygame.transform.scale(baseImage, (WIDTH/2, HEIGHT/2))

blImage = baseImage
trImage = pygame.transform.flip(blImage, 1, 1)
brImage = pygame.transform.flip(blImage, 1, 0)
tlImage = pygame.transform.flip(blImage, 0, 1)

images = [tlImage, trImage, brImage, blImage]

while True:

    holder = images[0]

    # rotates round the images
    if timer % 1 == 0:
        for i in xrange(3):
            images[i] = images[i+1]
        images[3] = holder

    # makes images appear in corresponding locations
    appear(images[0], 0, 0)
    appear(images[1], WIDTH/2, 0)
    appear(images[2], WIDTH/2, HEIGHT/2)
    appear(images[3], 0, HEIGHT/2)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    clock.tick(60)

    if timer < 2:
        timer += 0.1
    else:
        timer = 0
    print timer

    pygame.display.update()
