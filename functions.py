import pygame
import random

from vars import width, height, square_size, screen, green, white, red

def generate_food():
    food_x = round(random.randrange(0, width - square_size) / float(square_size)) * float(square_size)
    food_y = round(random.randrange(0, height - square_size) / float(square_size)) * float(square_size)
    return food_x, food_y


def design_food(size, food_x, food_y):
    pygame.draw.rect(screen, green, [food_x, food_y, size, size])


def design_snake(size, pixels):
    for pixel in pixels:
        pygame.draw.rect(screen, white, [pixel[0], pixel[1], size, size])


def design_score(score):
    font = pygame.font.SysFont('Helvetica', 25)
    text = font.render(f'Pontos: {score}', True, red)
    screen.blit(text, [1, 1])


def select_velocity(key):
    if key == pygame.K_DOWN:
        velocity_x = 0
        velocity_y = square_size
    elif key == pygame.K_UP:
        velocity_x = 0
        velocity_y = -square_size
    elif key == pygame.K_LEFT:
        velocity_x = -square_size
        velocity_y = 0
    elif key == pygame.K_RIGHT:
        velocity_x = square_size
        velocity_y = 0

    return velocity_x, velocity_y