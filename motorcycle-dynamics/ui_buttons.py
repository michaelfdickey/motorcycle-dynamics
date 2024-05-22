import pygame

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
LIGHT_GRAY = (200, 200, 200)
MEDIUM_GRAY = (120, 120, 120)
DARKER_GRAY = (60, 60, 60)
BRIGHT_YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
FIXTURE_COLOR = BLUE

# UI dimensions
UI_BAR_WIDTH = int(120 * 1.2)  # 20% larger than original width of 120
TOP_BAR_HEIGHT = 20
BUTTON_HEIGHT = int(40 * 0.8)  # 20% shorter
BUTTON_WIDTH = 60  # Increased width for larger buttons
BUTTON_SPACING = 10
EXIT_BUTTON_HEIGHT = 30
CHECKBOX_SIZE = 20

# Create buttons
buttons = {
    "create": pygame.Rect(10, 20, UI_BAR_WIDTH - 20, BUTTON_HEIGHT),
    "node": pygame.Rect(10, 25 + BUTTON_HEIGHT + BUTTON_SPACING, BUTTON_WIDTH, BUTTON_HEIGHT),
    "beam": pygame.Rect(80, 25 + BUTTON_HEIGHT + BUTTON_SPACING, BUTTON_WIDTH, BUTTON_HEIGHT),
    "fixture": pygame.Rect(10, 25 + 2 * (BUTTON_HEIGHT + BUTTON_SPACING), BUTTON_WIDTH, BUTTON_HEIGHT),
    "force": pygame.Rect(80, 25 + 2 * (BUTTON_HEIGHT + BUTTON_SPACING), BUTTON_WIDTH, BUTTON_HEIGHT),
    "torque": pygame.Rect(10, 25 + 3 * (BUTTON_HEIGHT + BUTTON_SPACING), BUTTON_WIDTH, BUTTON_HEIGHT),
    "mass": pygame.Rect(80, 25 + 3 * (BUTTON_HEIGHT + BUTTON_SPACING), BUTTON_WIDTH, BUTTON_HEIGHT),
    "edit": pygame.Rect(10, 160 + 4 * (BUTTON_HEIGHT + BUTTON_SPACING), UI_BAR_WIDTH - 20, BUTTON_HEIGHT),  # Edit group header button
    "delete": pygame.Rect(10, 165 + 5 * (BUTTON_HEIGHT + BUTTON_SPACING), BUTTON_WIDTH, BUTTON_HEIGHT),
    "move": pygame.Rect(80, 165 + 5 * (BUTTON_HEIGHT + BUTTON_SPACING), BUTTON_WIDTH, BUTTON_HEIGHT),
    "modify": pygame.Rect(10, 165 + 6 * (BUTTON_HEIGHT + BUTTON_SPACING), BUTTON_WIDTH, BUTTON_HEIGHT),
    "clear": pygame.Rect(80, 165 + 6 * (BUTTON_HEIGHT + BUTTON_SPACING), BUTTON_WIDTH, BUTTON_HEIGHT),
    "exit": pygame.Rect(10, 1000 - EXIT_BUTTON_HEIGHT - 10, UI_BAR_WIDTH - 20, BUTTON_HEIGHT),  # Adjusted for screen height
}

# Create labels and checkboxes for grid
grid_labels = {
    "display": pygame.Rect(10, 650, UI_BAR_WIDTH - 20, BUTTON_HEIGHT),  # Grid label positioned above checkboxes, changed to "Display"
    "1ft": pygame.Rect(40, 690, 50, CHECKBOX_SIZE),   # 1' grid label
    "1in": pygame.Rect(40, 720, 50, CHECKBOX_SIZE),   # 1" grid label
    "snap": pygame.Rect(40, 750, 50, CHECKBOX_SIZE),  # Snap label
}
checkboxes = {
    "1ft": pygame.Rect(10, 690, CHECKBOX_SIZE, CHECKBOX_SIZE),  # Checkbox for 1' grid
    "1in": pygame.Rect(10, 720, CHECKBOX_SIZE, CHECKBOX_SIZE),  # Checkbox for 1" grid
    "snap": pygame.Rect(10, 750, CHECKBOX_SIZE, CHECKBOX_SIZE), # Checkbox for snap
}

highlighted = {
    "create": False,
    "node": False,
    "beam": False,
    "fixture": False,
    "force": False,
    "torque": False,
    "mass": False,
    "edit": False,
    "delete": False,
    "move": False,
    "modify": False,
    "clear": False,
}

checkbox_states = {
    "1ft": True,   # 1' grid is visible by default
    "1in": False,  # 1" grid is not visible by default
    "snap": True, # Snap is now enabled by default
}

selected_button_group = None

def draw_button(screen, rect, text, is_highlighted, font):
    color = LIGHT_GRAY if is_highlighted else WHITE
    pygame.draw.rect(screen, color, rect)
    pygame.draw.rect(screen, BLACK, rect, 2)
    label = font.render(text, True, BLACK)
    screen.blit(label, (rect.x + 5, rect.y + 5))

def draw_label(screen, rect, text, font):
    label = font.render(text, True, BLACK)
    screen.blit(label, (rect.x + 5, rect.y))

def draw_checkbox(screen, rect, is_checked):
    pygame.draw.rect(screen, WHITE, rect)
    pygame.draw.rect(screen, BLACK, rect, 2)
    if is_checked:
        pygame.draw.line(screen, BLACK, (rect.x, rect.y), (rect.x + rect.width, rect.y + rect.height), 2)
        pygame.draw.line(screen, BLACK, (rect.x, rect.y + rect.height), (rect.x + rect.width, rect.y), 2)

def draw_all_buttons(screen, font, small_font):
    draw_button(screen, buttons["create"], "Create", highlighted["create"], font)
    draw_button(screen, buttons["node"], "Node", highlighted["node"], font)
    draw_button(screen, buttons["beam"], "Beam", highlighted["beam"], font)
    draw_button(screen, buttons["fixture"], "Fixture", highlighted["fixture"], font)
    draw_button(screen, buttons["force"], "Force", highlighted["force"], font)
    draw_button(screen, buttons["torque"], "Torque", highlighted["torque"], font)
    draw_button(screen, buttons["mass"], "Mass", highlighted["mass"], font)
    draw_button(screen, buttons["edit"], "Edit", highlighted["edit"], font)
    draw_button(screen, buttons["delete"], "Delete", highlighted["delete"], font)
    draw_button(screen, buttons["move"], "Move", highlighted["move"], font)
    draw_button(screen, buttons["modify"], "Modify", highlighted["modify"], font)
    draw_button(screen, buttons["clear"], "Clear", highlighted["clear"], font)
    draw_button(screen, buttons["exit"], "Exit", False, font)
    draw_label(screen, grid_labels["display"], "Display", font)  # Changed label to "Display"
    draw_checkbox(screen, checkboxes["1ft"], checkbox_states["1ft"])
    draw_label(screen, grid_labels["1ft"], "1' Grid", small_font)  # Updated label to "1' Grid"
    draw_checkbox(screen, checkboxes["1in"], checkbox_states["1in"])
    draw_label(screen, grid_labels["1in"], "1\" Grid", small_font)  # Updated label to "1\" Grid"
    draw_checkbox(screen, checkboxes["snap"], checkbox_states["snap"])
    draw_label(screen, grid_labels["snap"], "Snap", small_font)