import pygame
import sys
from create_nodes import handle_node_click, draw_nodes, handle_fixture_click, draw_fixtures
from create_beams import handle_beam_click, draw_beams
from ui_buttons import buttons, highlighted, draw_all_buttons, handle_button_click, UI_BAR_WIDTH, TOP_BAR_HEIGHT

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 1500
SCREEN_HEIGHT = 1000

# Colors
BLACK = (0, 0, 0)
SOFT_YELLOW = (255, 255, 224)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

# Setup the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Motorcycle Designer')

# Fonts
font = pygame.font.SysFont(None, 22)  # Reduced font size by 10%
small_font = pygame.font.SysFont(None, 18)  # Smaller font for the tally

nodes = []
beams = []
fixtures = []
beam_start_node = None

def draw_ui():
    # Left UI bar
    pygame.draw.rect(screen, SOFT_YELLOW, (0, 0, UI_BAR_WIDTH, SCREEN_HEIGHT))
    # Top UI bar
    pygame.draw.rect(screen, SOFT_YELLOW, (0, 0, SCREEN_WIDTH, TOP_BAR_HEIGHT))
    # Draw all buttons
    draw_all_buttons(screen, font)
    # Draw node and beam tally
    node_tally_text = small_font.render(f"Nodes: {len(nodes)}", True, RED)
    beam_tally_text = small_font.render(f"Beams: {len(beams)}", True, RED)
    screen.blit(node_tally_text, (SCREEN_WIDTH - 100, SCREEN_HEIGHT - 40))
    screen.blit(beam_tally_text, (SCREEN_WIDTH - 100, SCREEN_HEIGHT - 20))

def main():
    global nodes, beams, fixtures, beam_start_node

    running = True
    while running:
        screen.fill(BLACK)  # Changed background color to black

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if mouse_pos[0] <= UI_BAR_WIDTH or mouse_pos[1] <= TOP_BAR_HEIGHT:
                    handle_button_click(mouse_pos)
                else:
                    handle_node_click(mouse_pos, nodes, highlighted)
                    beam_start_node = handle_beam_click(mouse_pos, nodes, beams, highlighted, beam_start_node)
                    handle_fixture_click(mouse_pos, nodes, fixtures, highlighted)

        draw_ui()
        draw_nodes(screen, nodes)
        draw_beams(screen, beams)
        draw_fixtures(screen, fixtures)

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
