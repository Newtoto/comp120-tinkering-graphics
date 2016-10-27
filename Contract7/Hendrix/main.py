import pygame, sys, colorsys
from pygame.locals import *
from PIL import Image

pygame.init()

#defining colors
WIDTH = 400
HEIGHT = 600
PURPLE = [191, 55, 131]
YELLOW = [250, 212, 27]
WHITE = [255, 255, 255]

angle = -90
timer = 0
clock = pygame.time.Clock()

# creating screen
screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)

def loadscale(image, width, height):
    return pygame.transform.scale(pygame.image.load(image),(width, height))

# gets background image and creates another with purple and yellow inverted
bgImage = loadscale("Images/BaseImage.png", WIDTH, HEIGHT)

# Inverted purple and yellow background
bgImage2 = loadscale("Images/BaseImage.png", WIDTH, HEIGHT)
bgImageArray = pygame.PixelArray(bgImage2)
pygame.PixelArray.replace(bgImageArray, PURPLE, WHITE, 0)
pygame.PixelArray.replace(bgImageArray, YELLOW, PURPLE, 0)
pygame.PixelArray.replace(bgImageArray, WHITE, YELLOW, 0)
del bgImageArray

# loads in spirals
smallSpiral = loadscale('Images/SmallSpiral.png', 47, 47)

while True:

    if timer % 20 == 0:
        screen.blit(bgImage, (0, 0), None, 0)
        timer += 1
    elif timer % 10 == 0:
        screen.blit(bgImage2, (0, 0), None, 0)
        timer += 1
    else:
        timer += 1

    smallSpiral = pygame.transform.rotate(smallSpiral, angle)
    screen.blit(smallSpiral, (17, 16), None, 0)
    screen.blit(smallSpiral, (335, 17), None, 0)
    screen.blit(smallSpiral, (16, 541), None, 0)
    screen.blit(smallSpiral, (336, 541), None, 0)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    clock.tick(60)
    pygame.display.flip()