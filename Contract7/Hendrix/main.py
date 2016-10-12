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


# function to load image from path, omit 'Images/' from path
def imageload(path):
    return pygame.image.load('Images/' + path)


# --- Defining movement functions ---

def spinner(swirl):
    print "confirm"
    angle = angle + 10
    swirl = pygame.transform.rotate(swirl, angle)
    screen.blit(swirl, (0, 0), None, 0)

# --- Loading in image layers and resizing ---

# base layer
baseImage = imageload('BaseImage.jpg')
#imageappear(baseImage)

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

tLSpiral = imageload('SmallSpirals/TopLeftSpiral.png')
imageappear(tLSpiral)

tRSpiral = imageload('SmallSpirals/TopRightSpiral.png')
imageappear(tRSpiral)

bLSpiral = imageload('SmallSpirals/BottomLeftSpiral.png')
imageappear(bLSpiral)

bRSpiral = imageload('SmallSpirals/BottomRightSpiral.png')
imageappear(bRSpiral)


while True:
    pressed = pygame.key.get_pressed()

    #spinner doesn't work, the function is calling hence 'confirm' on pressing the down arrow
    if pressed[pygame.K_DOWN]:
        spinner(bLSpiral)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
