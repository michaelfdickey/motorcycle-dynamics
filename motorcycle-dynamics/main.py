import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
screen = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("Motorcycle Dynamics")

# Colors
BLACK = (0, 0, 0)
SOFT_YELLOW = (255, 235, 205)  # Updated color
RED = (255, 0, 0)  # Added color for EXIT label and border

# Set background color
screen.fill(SOFT_YELLOW)  # Updated to use SOFT_YELLOW

# Draw the yellow left column
pygame.draw.rect(screen, SOFT_YELLOW, pygame.Rect(0, 0, 200, 800))  # Updated to use SOFT_YELLOW

# Draw the top row
pygame.draw.rect(screen, SOFT_YELLOW, pygame.Rect(0, 0, 1200, 20))  # Updated to use SOFT_YELLOW

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
                # Draw a red border around the exit button area
                pygame.draw.rect(screen, RED, pygame.Rect(0, 780, 200, 20), 3)  # Added red border
                font = pygame.font.Font(None, 36)
                text = font.render('EXIT', True, RED)
                screen.blit(text, (80, 782))  # Added 'EXIT' label in red
                running = False

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
