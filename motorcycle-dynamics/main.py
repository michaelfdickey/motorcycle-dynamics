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
SOFT_YELLOW = (255, 247, 200)  # Adjusted soft yellow color for navigation bars

# Set background color
screen.fill(BLACK)  # Confirmed BLACK as the main background color

# Draw the yellow left column (secondary navigation bar)
pygame.draw.rect(screen, SOFT_YELLOW, pygame.Rect(0, 0, 100, 800))  # Adjusted to 100 pixels wide and full height

# Draw the main navigation bar across the top
pygame.draw.rect(screen, SOFT_YELLOW, pygame.Rect(0, 0, 1200, 20))  # Added main navigation bar in soft yellow

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if the exit button is clicked
            x, y = event.pos
            if x <= 100 and y >= 780:  # Adjusted to match the width of the secondary navigation bar
                # Draw a red border around the exit button area persistently
                pygame.draw.rect(screen, RED, pygame.Rect(0, 780, 100, 20), 2)  # Adjusted to 100 pixels wide
                font = pygame.font.Font(None, 36)
                # Change the exit button color to light blue when clicked
                text = font.render('EXIT', True, LIGHT_BLUE, RED)  # Added RED background for the EXIT label
                screen.blit(text, (10, 782))  # Adjusted text position to match the resized button
                running = False

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()