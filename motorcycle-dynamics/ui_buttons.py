import pygame

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
LIGHT_GRAY = (200, 200, 200)

# UI dimensions
UI_BAR_WIDTH = int(120 * 1.2)  # 20% larger than original width of 120
TOP_BAR_HEIGHT = 20
BUTTON_HEIGHT = int(40 * 0.8)  # 20% shorter
BUTTON_WIDTH = 60  # Increased width for larger buttons
BUTTON_SPACING = 10
EXIT_BUTTON_HEIGHT = 30

# Create buttons
buttons = {
    "create": pygame.Rect(10, 20, UI_BAR_WIDTH - 20, BUTTON_HEIGHT),
    "node": pygame.Rect(10, 25 + BUTTON_HEIGHT + BUTTON_SPACING, BUTTON_WIDTH, BUTTON_HEIGHT),
    "beam": pygame.Rect(80, 25 + BUTTON_HEIGHT + BUTTON_SPACING, BUTTON_WIDTH, BUTTON_HEIGHT),
    "fixture": pygame.Rect(10, 25 + 2 * (BUTTON_HEIGHT + BUTTON_SPACING), BUTTON_WIDTH, BUTTON_HEIGHT),
    "force": pygame.Rect(80, 25 + 2 * (BUTTON_HEIGHT + BUTTON_SPACING), BUTTON_WIDTH, BUTTON_HEIGHT),
    "torque": pygame.Rect(10, 25 + 3 * (BUTTON_HEIGHT + BUTTON_SPACING), BUTTON_WIDTH, BUTTON_HEIGHT),
    "mass": pygame.Rect(80, 25 + 3 * (BUTTON_HEIGHT + BUTTON_SPACING), BUTTON_WIDTH, BUTTON_HEIGHT),
    "exit": pygame.Rect(10, 1000 - EXIT_BUTTON_HEIGHT - 10, UI_BAR_WIDTH - 20, BUTTON_HEIGHT)  # Adjusted for screen height
}

highlighted = {
    "create": False,
    "node": False,
    "beam": False,
    "fixture": False,
    "force": False,
    "torque": False,
    "mass": False
}

def draw_button(screen, rect, text, is_highlighted, font):
    color = LIGHT_GRAY if is_highlighted else WHITE
    pygame.draw.rect(screen, color, rect)
    pygame.draw.rect(screen, BLACK, rect, 2)
    label = font.render(text, True, BLACK)
    screen.blit(label, (rect.x + 5, rect.y + 5))

def draw_all_buttons(screen, font):
    draw_button(screen, buttons["create"], "Create", highlighted["create"], font)
    draw_button(screen, buttons["node"], "Node", highlighted["node"], font)
    draw_button(screen, buttons["beam"], "Beam", highlighted["beam"], font)
    draw_button(screen, buttons["fixture"], "Fixture", highlighted["fixture"], font)
    draw_button(screen, buttons["force"], "Force", highlighted["force"], font)
    draw_button(screen, buttons["torque"], "Torque", highlighted["torque"], font)
    draw_button(screen, buttons["mass"], "Mass", highlighted["mass"], font)
    draw_button(screen, buttons["exit"], "Exit", False, font)

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
                    # Unhighlight other create options
                    for other_key in ["node", "beam", "fixture", "force", "torque", "mass"]:
                        if other_key != key:
                            highlighted[other_key] = False
                    highlighted[key] = not highlighted[key]
            return
