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
SOFT_ORANGE = (255, 165, 0)  # Defined soft orange color for button highlight

# Set background color
screen.fill(BLACK)  # Confirmed BLACK as the main background color

# Draw the yellow left column (secondary navigation bar)
pygame.draw.rect(screen, SOFT_YELLOW, pygame.Rect(0, 0, 100, 800))  # Adjusted to 100 pixels wide and full height

# Draw the main navigation bar across the top
pygame.draw.rect(screen, SOFT_YELLOW, pygame.Rect(0, 0, 1200, 20))  # Updated main navigation bar to soft yellow

# Draw a red border around the exit button area persistently
pygame.draw.rect(screen, LIGHT_BLUE, pygame.Rect(0, 780, 100, 20), 2)  # Adjusted to 100 pixels wide
font = pygame.font.SysFont('Arial', 16)  # Changed font to Arial

# Render the exit button text persistently
text = font.render('EXIT', True, BLACK, None)  # Added RED background for the EXIT label
screen.blit(text, (10, 782))  # Adjusted text position to match the resized button

# Create button variables
create_button_highlighted = False
selected_button = None

# Draw the 'Create' button
def draw_create_button(highlighted):
    color = SOFT_YELLOW if highlighted else SOFT_YELLOW
    pygame.draw.rect(screen, color, pygame.Rect(0, 20, 100, 20))
    text = font.render('CREATE', True, BLACK, None)
    screen.blit(text, (10, 22))

# Draw additional buttons
def draw_additional_buttons():
    buttons = ["NODE", "BEAM", "FIXTURE", "FORCE", "TORQUE"]
    y_pos = 40
    for button in buttons:
        color = SOFT_ORANGE if selected_button == button else SOFT_YELLOW
        if button in ["NODE", "BEAM"]:
            width = 50 if button == "NODE" else 50
            x_pos = 0 if button == "NODE" else 50
        else:
            width = 100
            x_pos = 0
        pygame.draw.rect(screen, color, pygame.Rect(x_pos, y_pos, width, 20))
        text = font.render(button, True, BLACK, None)
        screen.blit(text, (x_pos + 10, y_pos + 2))
        y_pos += 20

draw_create_button(create_button_highlighted)
draw_additional_buttons()

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            # Toggle 'Create' button highlight
            if 0 <= x <= 100 and 20 <= y <= 40:
                create_button_highlighted = not create_button_highlighted
                selected_button = None if create_button_highlighted else selected_button
                draw_create_button(create_button_highlighted)
                draw_additional_buttons()
            # Check if the exit button is clicked
            elif x <= 100 and y >= 780:
                running = False
            # Check for additional button clicks
            elif create_button_highlighted:
                if 0 <= x <= 50 and 40 <= y <= 60:  # NODE button
                    selected_button = "NODE"
                elif 50 <= x <= 100 and 40 <= y <= 60:  # BEAM button
                    selected_button = "BEAM"
                elif 0 <= x <= 100 and 60 <= y <= 80:  # FIXTURE button
                    selected_button = "FIXTURE"
                elif 0 <= x <= 100 and 80 <= y <= 100:  # FORCE button
                    selected_button = "FORCE"
                elif 0 <= x <= 100 and 100 <= y <= 120:  # TORQUE button
                    selected_button = "TORQUE"
                draw_additional_buttons()

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
