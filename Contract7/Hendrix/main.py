import pygame, sys, colorsys
from pygame.locals import *
from PIL import Image

pygame.init()

#defining colors
PURPLE = 191, 55, 131
YELLOW = 250, 212, 27
WHITE = 255, 255, 255
BLACK = 0, 0, 0

# screen dimentions
WIDTH = 400
HEIGHT = 600

angle = -90  # degrees turned by corner spirals
timer = 0  # initialising timer variable for while loop
clock = pygame.time.Clock()

# creating mask to go over dots
maskHeight = 93
dotBlock = pygame.Surface((15, 15))
dotBlock.set_alpha(90)
dotBlock.fill(BLACK)
blockXleft = 5
blockXright = 380
blockY = 426
blockDist = 0
blockUp = True

def dotsblit(dotBlock, Xside, Y, blockDist):
    screen.blit(dotBlock, (Xside, Y - blockDist))
    screen.blit(dotBlock, (Xside, Y - blockDist + 130))
    screen.blit(dotBlock, (Xside, Y - blockDist + 260))
    screen.blit(dotBlock, (Xside, Y - blockDist + 390))


# creating screen
screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)

def loadscale(image, width, height):
    return pygame.transform.scale(pygame.image.load(image),(width, height))

# gets background image and creates another with purple and yellow inverted
bgImage = loadscale("Images/BaseImage.png", WIDTH, HEIGHT)

# Inverted purple and yellow background
bgImage2 = loadscale("Images/BaseImage.png", WIDTH, HEIGHT)
bgImageArray = pygame.PixelArray(bgImage2)
pygame.PixelArray.replace(bgImageArray, PURPLE, WHITE, 0)  # changes purple to white temporarily
pygame.PixelArray.replace(bgImageArray, YELLOW, PURPLE, 0)  # changes yellow to purple
pygame.PixelArray.replace(bgImageArray, WHITE, YELLOW, 0)  # changes temporary white to yellow
del bgImageArray

# loads in spirals
smallSpiral = loadscale('Images/SmallSpiral.png', 47, 47)

while True:

    # switching between background images to change purple and yellow
    if timer % 20 == 0:
        hendrix = bgImage
        timer += 1
    elif timer % 10 == 0:
        hendrix = bgImage2
        timer += 1
    else:
        timer += 1
    screen.blit(hendrix, (0, 0), None, 0)

    # rotating spirals by angle and making them appear
    if timer % 5 == 0:
        smallSpiral = pygame.transform.rotate(smallSpiral, angle)
    screen.blit(smallSpiral, (17, 16), None, 0)
    screen.blit(smallSpiral, (335, 17), None, 0)
    screen.blit(smallSpiral, (16, 541), None, 0)
    screen.blit(smallSpiral, (336, 541), None, 0)

    # moving mask over dots
    if timer % 10 == 0:
        if maskHeight < 450:
            if blockUp == True:
                maskHeight += 26
                blockDist += 26
            else:
                if maskHeight == 15:
                    blockUp = True
                    blockDist = -78
                else:
                    maskHeight -= 26
        else:
            blockUp = False
            maskHeight -= 26

    dotBlock = pygame.Surface((15, maskHeight))
    dotBlock.set_alpha(180)

    # making dot masks appear
    screen.blit(dotBlock, (blockXleft, blockY - blockDist))
    screen.blit(dotBlock, (blockXright, blockY - blockDist))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    clock.tick(60)
    pygame.display.flip()