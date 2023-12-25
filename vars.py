import pygame

width, height = 600, 400
screen = pygame.display.set_mode((width, height))

clock = pygame.time.Clock()

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)

square_size = 10.0 # px
velocity = 15 #