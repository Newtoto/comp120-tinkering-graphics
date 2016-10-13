import pygame, sys
from pygame.locals import *

width = 400
height = 600
angle = 0

screen = pygame.display.set_mode((width, height), 0, 32)  # Setting screen size

# --- Defining loading functions ---

# function to resize and display images
def imageappear(image):
    image = pygame.transform.scale(image, (width, height))
    screen.blit(image, (0, 0), None, 0)


# function to load image from path, remember to omit 'Images/' from path
def imageload(path):
    return pygame.image.load('Images/' + path)


# --- Loading in image layers and resizing ---

# base layer
baseImage = imageload('BaseImage.png')
imageappear(baseImage)

# dots layers
dotsImage1 = imageload('Dots/Dots1.png')
imageappear(dotsImage1)

dotsImage2 = imageload('Dots/Dots2.png')
imageappear(dotsImage2)

dotsImage3 = imageload('Dots/Dots3.png')
imageappear(dotsImage3)

dotsImage4 = imageload('Dots/Dots4.png')
imageappear(dotsImage4)

dotsImage5 = imageload('Dots/Dots5.png')
imageappear(dotsImage5)

# big spiral layers
purpleLines = imageload('BigSpiral/PurpleLines.png')
imageappear(purpleLines)

yellowLines = imageload('BigSpiral/YellowLines.png')
imageappear(yellowLines)

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

    #spinner doesn't work, the function is calling hence 'confirm' on pressing the down arrow
    if pressed[pygame.K_DOWN]:
        angle = angle + 10
        bLSpiral = pygame.transform.rotate(bLSpiral, angle)
        screen.blit(bLSpiral, (0, 0), None, 0)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
