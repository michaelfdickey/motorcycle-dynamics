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

# Set background color
screen.fill(BLACK)  # Changed to BLACK

# Draw the yellow left column
pygame.draw.rect(screen, BLACK, pygame.Rect(0, 0, 200, 800))  # Changed to BLACK

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
            if x <= 200 and y >= 780:
                # Draw a light blue border around the exit button area persistently
                pygame.draw.rect(screen, LIGHT_BLUE, pygame.Rect(0, 780, 200, 20), 3)  # Changed to LIGHT_BLUE and made persistent
                font = pygame.font.Font(None, 36)
                # Change the exit button color to light blue when clicked
                text = font.render('EXIT', True, LIGHT_BLUE)  # Changed to LIGHT_BLUE
                screen.blit(text, (80, 782))
                running = False

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
