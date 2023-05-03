
import pygame

import random

 


# Define constants for the game

WIDTH = 640

HEIGHT = 480

BLACK = (0, 0, 0)

WHITE = (255, 255, 255)

RED = (255, 0, 0)

GREEN = (0, 255, 0)

BLUE = (0, 0, 255)

 


# Initialize Pygame

pygame.init()

 


# Set the size of the screen

screen = pygame.display.set_mode((WIDTH, HEIGHT))

 


# Set the caption for the window

pygame.display.set_caption("Bullseye Game")

 


# Set the font for the score

font = pygame.font.Font(None, 36)

 


# Define the class for the bullseye

class Bullseye(pygame.sprite.Sprite):

    def init(self):

        super().init()

        self.image = pygame.Surface((50, 50))

        self.image.fill(BLUE)

        pygame.draw.circle(self.image, WHITE, (25, 25), 20)

        pygame.draw.circle(self.image, RED, (25, 25), 10)

        self.rect = self.image.get_rect()

        self.rect.center = (random.randint(50, WIDTH-50), random.randint(50, HEIGHT-50))

 


# Create a sprite group for the bullseyes

bullseyes = pygame.sprite.Group()

for i in range(10):

    bullseye = Bullseye()

    bullseyes.add(bullseye)

 


# Set the initial score to zero

score = 0

 


# Start the game loop

running = True

while running:

    # Handle events

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:

            # Check if the player clicked on a bullseye

            for bullseye in bullseyes:

                if bullseye.rect.collidepoint(event.pos):

                    # Add points to the score based on the size of the bullseye

                    if bullseye.rect.width == 50:

                        score += 5

                    elif bullseye.rect.width == 30:

                        score += 10

                    elif bullseye.rect.width == 10:

                        score += 20

                    bullseye.kill()

 


    # Clear the screen

    screen.fill(BLACK)

 


    # Draw the bullseyes

    bullseyes.draw(screen)

 


    # Draw the score

    score_text = font.render(f"Score: {score}", True, GREEN)

    screen.blit(score_text, (10, 10))

 


    # Update the screen

    pygame.display.update()

 


# Quit Pygame

pygame.quit()