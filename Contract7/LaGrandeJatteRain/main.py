import pygame
import random

pygame.init()
clock = pygame.time.Clock()

window_width = 750
window_width = 750
window_height = 501
window_size = (window_width, window_height)

bg = pygame.image.load("Images/BaseImage.jpg")
window = pygame.display.set_mode(window_size)

rain_pos_x = []
rain_pos_y = 0
rain_radius = []
Blue = (0,0,255)
x = 0

num_Rian_drops = 50000
for rain_index in xrange(num_Rian_drops):
    rain_pos_x.append(random.randrange(0, window_width))
    rain_radius.append(random.randrange(2, 5))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    window.blit(bg, (0, 0))
    ball_index = 0
    for rain_index in xrange(num_Rian_drops):
        rain_pos_y += 1

        pos_x = rain_pos_x[rain_index]
        pos_y = rain_pos_y
        radius = rain_radius[rain_index]
        pygame.draw.circle(window, Blue, (pos_x, pos_y), radius)

    pygame.display.flip()
    clock.tick(60)
