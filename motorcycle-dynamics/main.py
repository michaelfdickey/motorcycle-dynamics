import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
screen = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("Motorcycle Dynamics")

# Colors
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)

# Set background color
screen.fill(BLACK)

# Draw the yellow left column
pygame.draw.rect(screen, YELLOW, pygame.Rect(0, 0, 200, 800))

# Draw the top row
pygame.draw.rect(screen, BLACK, pygame.Rect(0, 0, 1200, 20))

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if the exit button is clicked
            x, y = event.pos
            if x <= 200 and y >= 780:
                running = False

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
