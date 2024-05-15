import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 1500
SCREEN_HEIGHT = 1000

# Colors
WHITE = (255, 255, 255)
SOFT_YELLOW = (255, 255, 224)
BLACK = (0, 0, 0)
BRIGHT_YELLOW = (255, 255, 0)
LIGHT_GRAY = (200, 200, 200)

# Setup the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Motorcycle Designer')

# Fonts
font = pygame.font.SysFont(None, 24)

# UI dimensions
UI_BAR_WIDTH = 120
TOP_BAR_HEIGHT = 20
EXIT_BUTTON_HEIGHT = 30
BUTTON_HEIGHT = 30
BUTTON_SPACING = 10

# Create buttons
buttons = {
    "create": pygame.Rect(10, 20, 100, BUTTON_HEIGHT),
    "node": pygame.Rect(10, 70, 100, BUTTON_HEIGHT),
    "beam": pygame.Rect(10, 110, 100, BUTTON_HEIGHT),
    "fixture": pygame.Rect(10, 150, 100, BUTTON_HEIGHT),
    "force": pygame.Rect(10, 190, 100, BUTTON_HEIGHT),
    "torque": pygame.Rect(10, 230, 100, BUTTON_HEIGHT),
    "exit": pygame.Rect(10, SCREEN_HEIGHT - EXIT_BUTTON_HEIGHT - 10, 100, BUTTON_HEIGHT)
}

highlighted = {
    "create": False,
    "node": False,
    "beam": False,
    "fixture": False,
    "force": False,
    "torque": False
}

nodes = []

def draw_button(screen, rect, text, is_highlighted):
    color = LIGHT_GRAY if is_highlighted else WHITE
    pygame.draw.rect(screen, color, rect)
    pygame.draw.rect(screen, BLACK, rect, 2)
    label = font.render(text, True, BLACK)
    screen.blit(label, (rect.x + 10, rect.y + 5))

def handle_button_click(mouse_pos):
    global highlighted
    for key in buttons:
        if buttons[key].collidepoint(mouse_pos):
            if key == "exit":
                pygame.quit()
                sys.exit()
            elif key == "create":
                highlighted["create"] = not highlighted["create"]
            else:
                if highlighted["create"]:
                    highlighted[key] = not highlighted[key]

def draw_ui():
    # Left UI bar
    pygame.draw.rect(screen, SOFT_YELLOW, (0, 0, UI_BAR_WIDTH, SCREEN_HEIGHT))
    # Top UI bar
    pygame.draw.rect(screen, SOFT_YELLOW, (0, 0, SCREEN_WIDTH, TOP_BAR_HEIGHT))
    # Buttons
    draw_button(screen, buttons["create"], "Create", highlighted["create"])
    draw_button(screen, buttons["node"], "Node", highlighted["node"])
    draw_button(screen, buttons["beam"], "Beam", highlighted["beam"])
    draw_button(screen, buttons["fixture"], "Fixture", highlighted["fixture"])
    draw_button(screen, buttons["force"], "Force", highlighted["force"])
    draw_button(screen, buttons["torque"], "Torque", highlighted["torque"])
    draw_button(screen, buttons["exit"], "Exit", False)

def main():
    global nodes

    running = True
    while running:
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if mouse_pos[0] > UI_BAR_WIDTH and mouse_pos[1] > TOP_BAR_HEIGHT:
                    if highlighted["create"] and highlighted["node"]:
                        nodes.append(mouse_pos)
                else:
                    handle_button_click(mouse_pos)

        draw_ui()

        for node in nodes:
            pygame.draw.circle(screen, BRIGHT_YELLOW, node, 5)

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
