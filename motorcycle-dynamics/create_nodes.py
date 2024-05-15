import pygame

BRIGHT_YELLOW = (255, 255, 0)
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
