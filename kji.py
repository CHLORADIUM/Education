import pygame
import random

# Initialize Pygame
pygame.init()

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Set the width and height of the screen
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
BLOCK_SIZE = 10

# Create the window
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Set the window title
pygame.display.set_caption('Snake Game')

# Set the clock
clock = pygame.time.Clock()

# Define the font
font = pygame.font.SysFont(None, 25)

# Define the function to display the score
def display_score(score):
    score_text = font.render('Score: ' + str(score), True, WHITE)
    window.blit(score_text, [0, 0])

# Define the function to draw the snake
def draw_snake(snake_block_size, snake_list):
    for x in snake_list:
        pygame.draw.rect(window, BLACK, [x[0], x[1], snake_block_size, snake_block_size])

# Define the function to run the game
def game_loop():
    # Set the starting position of the snake
    x1 = WINDOW_WIDTH / 2
    y1 = WINDOW_HEIGHT / 2

    # Set the change in position of the snake
    x1_change = 0
    y1_change = 0

    # Set the length of the snake
    snake_list = []
    snake_length = 20
    

    # Set the position of the food
    food_x = round(random.randrange(0, WINDOW_WIDTH - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
    food_y = round(random.randrange(0, WINDOW_HEIGHT - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE

    # Set the game over flag
    game_over = False

    # Set the score
    score = 0

    # Run the game loop
    while not game_over:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -BLOCK_SIZE
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = BLOCK_SIZE
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -BLOCK_SIZE
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = BLOCK_SIZE
                    x1_change = 0

        # Update the snake's position
        x1 += x1_change
        y1 += y1_change

        # Check for collision with the walls
        if x1 >= WINDOW_WIDTH or x1 < 0 or y1 >= WINDOW_HEIGHT or y1 < 0:
            game_over = True

        # Check for collision with the food
        if x1 == food_x and y1 == food_y:
            food_x = round(random.randrange(0, WINDOW_WIDTH - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
            food_y = round(random.randrange(0, WINDOW_HEIGHT - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
            snake_length += 1
            score += 1

        # Draw the window and the snake
        window.fill(RED)
        pygame.draw.rect(window, WHITE, [food_x, food_y, BLOCK_SIZE, BLOCK_SIZE])
        snake_head = [x1, y1]
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_over = True

        draw_snake(BLOCK_SIZE, snake_list)
        display_score(score)

        # Update the window
        pygame.display.update()

        # Set the clock speed
        clock.tick(10)

    # Quit Pygame
    pygame.quit()
    quit()

# Run the game
game_loop()
