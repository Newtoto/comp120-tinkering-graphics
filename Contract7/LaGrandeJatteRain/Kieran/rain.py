import random
import pygame, sys
from pygame.locals import *

pygame.init()
clock = pygame.time.Clock()

ball_pos_x = []
ball_pos_y = []
ball_speed_x = []
ball_speed_y = []
ball_radius = []
xPos = 0
yPos = 0
WIDTH = 750
HEIGHT = 501
ball_index = 0
window = pygame.display.set_mode((WIDTH,HEIGHT),0,32)
BLACK = (0,0,0)
BLUE = (0,0,255,6)
bg = pygame.image.load("most-famous-paintings-7.jpg")
num_balls = 9
num_balls -= 1

for ball_index in xrange(num_balls):
    ball_radius.append(random.randrange(2, 5))

while True:
    window.blit(bg, (0, 0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    for ball_index in xrange(num_balls):
        xPos += 6
        yPos += 6
        radius = ball_radius[ball_index]

        window.blit(bg, (0, 0))
        pygame.draw.circle(window, BLUE, (xPos, yPos), radius)
        pygame.display.update()
        clock.tick(120)


