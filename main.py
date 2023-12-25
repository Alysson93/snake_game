# importações das libs
import pygame

from vars import width, height, screen, black, square_size, clock, velocity
from functions import generate_food, select_velocity, design_food, design_score, design_snake


# configurações
pygame.init()

pygame.display.set_caption('Python Snake')

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