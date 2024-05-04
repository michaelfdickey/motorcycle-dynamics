import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
screen = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("Motorcycle Dynamics")

# Colors
BLACK = (0, 0, 0)
LIGHT_BLUE = (173, 216, 230)  # Added color for clicked button
RED = (255, 0, 0)  # Added color for EXIT label and border
SOFT_YELLOW = (255, 247, 0)  # Soft yellow color for the left column

# Set background color
screen.fill(BLACK)  # Changed to BLACK

# Draw the yellow left column
pygame.draw.rect(screen, SOFT_YELLOW, pygame.Rect(0, 0, 60, 800))  # Changed to SOFT_YELLOW and width to 60 pixels

# Draw the top row
pygame.draw.rect(screen, BLACK, pygame.Rect(0, 0, 1200, 20))  # Changed to BLACK

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if the exit button is clicked
            x, y = event.pos
            if x <= 60 and y >= 780:  # Adjusted to match the width of the yellow column
                # Draw a red border around the exit button area persistently
                pygame.draw.rect(screen, RED, pygame.Rect(0, 780, 60, 20), 2)  # Changed to RED and width to 2 pixels
                font = pygame.font.Font(None, 36)
                # Change the exit button color to light blue when clicked
                text = font.render('EXIT', True, LIGHT_BLUE)  # Kept LIGHT_BLUE for the text color
                screen.blit(text, (10, 782))  # Adjusted text position to match the resized button
                running = False

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
