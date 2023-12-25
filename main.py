# importações das libs
import pygame
import random


# configurações
pygame.init()

pygame.display.set_caption('Python Snake')

width, height = 600, 400
screen = pygame.display.set_mode((width, height))

clock = pygame.time.Clock()

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)

square_size = 10.0 # px
velocity = 15 #


def generate_food():
    food_x = round(random.randrange(0, width - square_size) / square_size) * square_size
    food_y = round(random.randrange(0, height - square_size) / square_size) * square_size
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

# loop infinito do jogo

def run():
    
    game_over = False 

    # desenhando cobra
    x = width / 2
    y = height / 2
    velocity_x = 0
    velocity_y = 0
    snake_size = 1
    pixels = []

    # desenhando comida
    food_x, food_y = generate_food()

    while not game_over:

        screen.fill(black)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                velocity_x, velocity_y = select_velocity(event.key)


        design_food(square_size, food_x, food_y)

        if x < 0 or x >= width or y < 0 or y >= height:
            game_over = True

        x += velocity_x
        y += velocity_y

        pixels.append([x, y])
        if len(pixels) > snake_size:
            del pixels[0]
        
        for pixel in pixels[:-1]:
            if pixel == [x, y]:
                game_over = True
        

        design_snake(square_size, pixels)

        design_score(snake_size -1)

        pygame.display.update()

        if x == food_x and y == food_y:
            snake_size += 1
            food_x, food_y = generate_food()

        clock.tick(velocity)



if __name__ == '__main__':
    run()