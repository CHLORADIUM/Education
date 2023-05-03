import game_2
import random

# Initialize Pygame
game_2.init()

# Set the screen dimensions
screen_width = 800
screen_height = 600

# Create the screen
screen = game_2.display.set_mode((screen_width, screen_height))
game_2.display.set_caption("Animation and Keystroke Handling")

# Set the background color
background_color = (255, 255, 255)

# Set the font
font = game_2.font.Font(None, 36)

# Set the initial position of the rectangle
rect_x = 0
rect_y = screen_height // 2

# Set the speed of the rectangle
rect_speed = 5

# Set the initial score
score = 0

# Set the clock
clock = game_2.time.Clock()

# Main game loop
running = True
while running:

    # Handle events
    for event in game_2.event.get():
        if event.type == game_2.QUIT:
            running = False
        elif event.type == game_2.KEYDOWN:
            if event.key == game_2.K_UP:
                rect_y -= rect_speed
            elif event.key == game_2.K_DOWN:
                rect_y += rect_speed
            elif event.key == game_2.K_ESCAPE:
                running = False

    # Update the rectangle position
    rect_x += rect_speed

    # If the rectangle goes off the screen, reset it
    if rect_x > screen_width:
        rect_x = 0
        rect_y = random.randint(0, screen_height)

        # Increment the score
        score += 1

    # Set the background color
    screen.fill(background_color)

    # Draw the rectangle
    game_2.draw.rect(screen, (255, 0, 0), (rect_x, rect_y, 50, 50))

    # Draw the score
    score_text = font.render("Score: {}".format(score), True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    # Update the screen
    game_2.display.flip()


    # Set the frame rate
    clock.tick(60)


# Quit Pygame
game_2.quit()