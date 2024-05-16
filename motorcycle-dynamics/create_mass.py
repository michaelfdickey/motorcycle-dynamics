import pygame

RED = (255, 0, 0)
NODE_RADIUS = 5

def draw_mass(screen, node, mass_value):
    """Draw a mass symbol hanging below the node with the specified mass value."""
    x, y = node
    trapezoid_height = 20
    trapezoid_width_top = 20
    trapezoid_width_bottom = 30

    # Draw the trapezoid
    points = [
        (x - trapezoid_width_top // 2, y + trapezoid_height),
        (x + trapezoid_width_top // 2, y + trapezoid_height),
        (x + trapezoid_width_bottom // 2, y + 2 * trapezoid_height),
        (x - trapezoid_width_bottom // 2, y + 2 * trapezoid_height)
    ]
    pygame.draw.polygon(screen, RED, points, 2)

    # Draw the hanging line into the node
    pygame.draw.line(screen, RED, (x, y), (x, y + trapezoid_height), 2)

    # Draw the mass value inside the trapezoid
    font = pygame.font.SysFont(None, 18)
    label = font.render(f"{mass_value}", True, RED)
    label_rect = label.get_rect(center=(x, y + 1.5 * trapezoid_height))
    screen.blit(label, label_rect)

def handle_mass_click(mouse_pos, nodes, masses, highlighted, mass_value):
    """Handle mass-related clicks."""
    if highlighted["create"] and highlighted["mass"]:
        for node in nodes:
            if (node[0] - NODE_RADIUS <= mouse_pos[0] <= node[0] + NODE_RADIUS) and (node[1] - NODE_RADIUS <= mouse_pos[1] <= node[1] + NODE_RADIUS):
                masses.append((node, mass_value))
                return

def draw_masses(screen, masses):
    """Draw all masses on the screen."""
    for mass in masses:
        draw_mass(screen, mass[0], mass[1])
