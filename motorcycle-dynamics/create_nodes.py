import pygame

BRIGHT_YELLOW = (255, 255, 0)
FIXTURE_COLOR = (0, 0, 255)
NODE_RADIUS = 5

def handle_node_creation(nodes, mouse_pos):
    """Add a new node at the mouse position."""
    nodes.append(mouse_pos)

def draw_nodes(screen, nodes):
    """Draw all nodes on the screen."""
    for node in nodes:
        pygame.draw.circle(screen, BRIGHT_YELLOW, node, NODE_RADIUS)

def handle_node_click(mouse_pos, nodes, highlighted):
    """Handle node-related clicks."""
    if highlighted["create"] and highlighted["node"]:
        handle_node_creation(nodes, mouse_pos)

def draw_fixture(screen, node):
    """Draw a fixture symbol on the node."""
    x, y = node
    fixture_size = 10
    pygame.draw.line(screen, FIXTURE_COLOR, (x - fixture_size, y + fixture_size), (x + fixture_size, y + fixture_size), 2)
    pygame.draw.line(screen, FIXTURE_COLOR, (x - fixture_size / 2, y), (x + fixture_size / 2, y), 2)
    pygame.draw.line(screen, FIXTURE_COLOR, (x - fixture_size, y + fixture_size), (x - fixture_size / 2, y), 2)
    pygame.draw.line(screen, FIXTURE_COLOR, (x + fixture_size, y + fixture_size), (x + fixture_size / 2, y), 2)

def handle_fixture_click(mouse_pos, nodes, fixtures, highlighted):
    """Handle fixture-related clicks."""
    if highlighted["create"] and highlighted["fixture"]:
        for node in nodes:
            if (node[0] - NODE_RADIUS <= mouse_pos[0] <= node[0] + NODE_RADIUS) and (node[1] - NODE_RADIUS <= mouse_pos[1] <= node[1] + NODE_RADIUS):
                fixtures.append(node)
                return

def draw_fixtures(screen, fixtures):
    """Draw all fixtures on the screen."""
    for fixture in fixtures:
        draw_fixture(screen, fixture)
