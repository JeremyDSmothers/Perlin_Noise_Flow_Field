import pygame
from pygame.constants import QUIT
import random
import math
from perlin_noise import PerlinNoise
pygame.init()


#global variables
window_width = window_height = 400
incr = 5
scale = 20
noise1 = PerlinNoise()

win = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Perlin Noise Flow Field")

#classes

##### BEGIN Setup "FUNCTION" #####
cols = window_width // scale
rows = window_height // scale


##### END Setup "FUNCTION" #####

def draw_point(surface, x, y):
    pygame.draw.line(surface, (x, y), (x, y))

def scale_map(val, src, dst):
    return ((val - src[0]) / (src[1] - src[0])) * (dst[1]-dst[0]) + dst[0]

def draw_numbers(surface):
    font = pygame.font.SysFont('Arial',12)
    off = 0
    for j in range(rows):
        for i in range(cols):
            surface.blit(font.render(str(off), True, (255, 0, 0)), (i * scale, j * scale))
            off+=1

def draw_vector(surface, start_point, angle):
    print('draw')
    print(start_point, angle)
    x1 = start_point[0] + scale
    y1 = start_point[1]
    end_point = pygame.math.Vector2(0,scale)

    print(end_point)
    end_point = end_point.rotate(angle)
    print(end_point)

    pygame.draw.line(surface, (51, 51, 51), (start_point[0]*scale, start_point[1]*scale), (start_point[0]*scale + end_point[0], start_point[1]*scale + end_point[1]), 1)

    return end_point

def redrawGameWindow():
    win.fill((255, 255, 255))

    yoff = 0

    #do pixel manip between HERE
    # pixel_array = pygame.PixelArray(win)
    
    for j in range(rows):
        xoff = 0
        for i in range(cols):
            xoff += incr
            r = scale_map(noise1([xoff/rows, yoff/cols]), (-0.65, 0.65), (0, 360))

            start_point = pygame.math.Vector2(i, j)
            end_point = pygame.math.Vector2(0,scale).rotate(r)
            draw_vector(win, start_point, r)

            # print(r)
            # r = (random.randint(0, 255),random.randint(0, 255),random.randint(0, 255))
            # pygame.draw.rect(win, (r, r, r), (i*scale, j*scale, scale, scale))
        
        yoff += incr
        
    # draw_numbers(win)

    # pixel_array.close()
    #and HERE

    pygame.display.update()

#main loop
run = True
while run: 
    # pygame.time.delay(500)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    redrawGameWindow()

pygame.quit()