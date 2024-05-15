import pygame

WHITE = (255, 255, 255)
NODE_RADIUS = 5

def handle_beam_creation(beams, start_node, end_node):
    beams.append((start_node, end_node))

def draw_beams(screen, beams):
    for beam in beams:
        pygame.draw.line(screen, WHITE, beam[0], beam[1], 2)

def handle_beam_click(mouse_pos, nodes, beams, highlighted, beam_start_node):
    """Handle beam-related clicks."""
    if highlighted["create"] and highlighted["beam"]:
        for node in nodes:
            if (node[0] - NODE_RADIUS <= mouse_pos[0] <= node[0] + NODE_RADIUS) and (node[1] - NODE_RADIUS <= mouse_pos[1] <= node[1] + NODE_RADIUS):
                if beam_start_node is None:
                    return node  # Set beam_start_node
                else:
                    handle_beam_creation(beams, beam_start_node, node)
                    return None  # Reset beam_start_node
    return beam_start_node
