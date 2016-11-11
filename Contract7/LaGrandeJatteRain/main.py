import pygame
import random

pygame.init()

# defining variables
clock = pygame.time.Clock()

window_width = 750
window_height = 501
window_size = (window_width, window_height)
window = pygame.display.set_mode(window_size)

bg = pygame.image.load("Images/BaseImage.jpg")

# setting up rain aspects
rain_pos_x = []
rain_pos_y = 0
rain_radius = []
Blue = (180,225,255)
num_Rain_drops = 3000

# making rain array
for rain_index in xrange(num_Rain_drops):
    rain_pos_x.append(random.randrange(0, window_width))
    rain_radius.append(random.randrange(1, 2))

running = True
while running:

    window.blit(bg, (0, 0))

    # making rain drops appear
    for rain_index in xrange(num_Rain_drops):

        if rain_pos_y > window_height:
            rain_pos_y = 0
        else:
            rain_pos_y += 1

        pos_x = rain_pos_x[rain_index]
        pos_y = window_height - rain_pos_y
        radius = rain_radius[rain_index]
        pygame.draw.circle(window, Blue, (pos_x, pos_y), radius)

    pygame.display.flip()
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
