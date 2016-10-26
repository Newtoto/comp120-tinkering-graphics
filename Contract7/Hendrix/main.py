#    pxArray = pygame.PixelArray(purpleLines)
#    for x in range(0, width):
#        for y in range(0, height):
#            colour1 = screen.get_at((x, y)).r
#            if colour1 == purple:
#                colour1 = yellow
#            if colour1 == yellow:
#                colour1 = purple
#            pxArray[x:y] = (colour1, 0, 0)
#    del pxArray



import pygame, sys, colorsys
from pygame.locals import *
from PIL import Image

pygame.init()

width = 400
height = 600
angle = -90  # angle of each turn of corner spirals
dots = 0  # timer start for dots
timer = 0  # timer start for spirals

screen = pygame.display.set_mode((width, height), 0, 32)  # Setting screen size

# --- Defining loading functions ---

# function to load image from path, remember to omit 'Images/' from path
def imageload(path):
    return pygame.image.load('Images/' + path)


# function to resize and display images
def imageappear(image):
    image = pygame.transform.scale(image, (width, height))
    screen.blit(image, (0, 0), None, 0)

def imageappeardots(image):
    image = pygame.transform.scale(image, (width, height))
    image.set_alpha(120)
    screen.blit(image, (0, 0), None, 0)


# --- Loading in image layers and resizing ---
# base layer
baseImage = imageload('BaseImage.png')
imageappear(baseImage)

# dots layers
dotsImage1 = imageload('Dots/Dots1.png')
imageappeardots(dotsImage1)
dotsImage2 = imageload('Dots/Dots2.png')
dotsImage3 = imageload('Dots/Dots3.png')
dotsImage4 = imageload('Dots/Dots4.png')
dotsImage5 = imageload('Dots/Dots5.png')

# big spiral layers
purpleLines = imageload('BigSpiral/PurpleLines2.png')
imageappear(purpleLines)
purpleLinesInvert = imageload('BigSpiral/PurpleLinesInvert.png')


yellowLines = imageload('BigSpiral/YellowLines2.png')
imageappear(yellowLines)
yellowLinesInvert = imageload('BigSpiral/YellowLinesInvert.png')
# small spiral layer

topLeftSpiral = imageload('SmallSpiral.png')
topLeftSpiral = pygame.transform.scale(topLeftSpiral, (47, 47))
screen.blit(topLeftSpiral, (17, 16), None, 0)

topRightSpiral = imageload('SmallSpiral.png')
topRightSpiral = pygame.transform.scale(topRightSpiral, (47, 47))
screen.blit(topRightSpiral, (335, 17), None, 0)

bottomLeftSpiral = imageload('SmallSpiral.png')
bottomLeftSpiral = pygame.transform.scale(bottomLeftSpiral, (47, 47))
screen.blit(bottomLeftSpiral, (16, 541), None, 0)

bottomRightSpiral = imageload('SmallSpiral.png')
bottomRightSpiral = pygame.transform.scale(bottomRightSpiral, (47, 47))
screen.blit(bottomRightSpiral, (336, 541), None, 0)


while True:
    pressed = pygame.key.get_pressed()
    # spinner works for 90 degree turns but due to the top left point moving, blitting the spiral relative to the screen means that it moves for degrees that aren't in a form of 90 degrees.
    if pressed[pygame.K_DOWN]:

        dots += 1
        timer += 1
        # rotating the images
        bottomLeftSpiral = pygame.transform.rotate(bottomLeftSpiral, angle)
        bottomRightSpiral = pygame.transform.rotate(bottomLeftSpiral, angle)
        topLeftSpiral = pygame.transform.rotate(bottomLeftSpiral, angle)
        topRightSpiral = pygame.transform.rotate(bottomLeftSpiral, angle)
        imageappear(baseImage)  # refreshes the base image to erase the previous spiral pixels
        # refreshes the new spirals over the base image
        screen.blit(bottomLeftSpiral, (16, 541), None, 0)
        screen.blit(topLeftSpiral, (17, 16), None, 0)
        screen.blit(topRightSpiral, (335, 17), None, 0)
        screen.blit(bottomRightSpiral, (336, 541), None, 0)
        if dots < 5:
            imageappear(dotsImage1)
        elif dots < 10:
            imageappear(dotsImage2)
        elif dots < 15:
            imageappear(dotsImage3)
        elif dots < 20:
            imageappear(dotsImage4)
        elif dots < 25:
            imageappear(dotsImage5)
        else:
            imageappear(dotsImage1)
            dots = 0

        if timer < 2:
            imageappear(yellowLines)
            imageappear(purpleLines)
        elif timer < 4:
            imageappear(yellowLinesInvert)
            imageappear(purpleLinesInvert)
        else:
            timer = 0
            imageappear(yellowLines)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


    pygame.display.update()
