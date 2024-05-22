import pygame
import config
import math
from method_of_joints import calculate_joint_forces

def draw_beams(screen, beams, nodes, fixtures, masses):
    for beam in beams:
        node1_idx, node2_idx = beam
        node1, node2 = nodes[node1_idx], nodes[node2_idx]
        pygame.draw.line(screen, config.BEAM_COLOR, node1, node2, 2)  # Set beam color here
        draw_measurements(screen, node1, node2)

    # Calculate joint forces and display them
    beam_forces = calculate_joint_forces(nodes, beams, fixtures, masses)
    if beam_forces is not None:
        for i, force in enumerate(beam_forces):
            beam = beams[i]
            node1_idx, node2_idx = beam
            node1, node2 = nodes[node1_idx], nodes[node2_idx]
            mid_x, mid_y = (node1[0] + node2[0]) // 2, (node1[1] + node2[1]) // 2
            font = pygame.font.SysFont(None, 18)
            text_surface = font.render(f"{force:.2f}", True, config.BEAM_TEXT_COLOR)  # Change to desired color
            screen.blit(text_surface, (mid_x, mid_y))

def handle_beam_click(mouse_pos, nodes, beams, highlighted, beam_start_node, grid_size):
    if highlighted["create"] and highlighted["beam"]:
        for idx, node in enumerate(nodes):
            if (node[0] - config.NODE_RADIUS <= mouse_pos[0] <= node[0] + config.NODE_RADIUS) and (node[1] - config.NODE_RADIUS <= mouse_pos[1] <= node[1] + config.NODE_RADIUS):
                if beam_start_node is None:
                    beam_start_node = idx
                else:
                    beams.append((beam_start_node, idx))
                    beam_start_node = None
    return beam_start_node

def draw_measurements(screen, node1, node2):
    x1, y1 = node1
    x2, y2 = node2
    dx = x2 - x1
    dy = y2 - y1
    hypotenuse_pixels = math.sqrt(dx ** 2 + dy ** 2)
    
    # Assuming the grid size is in pixels and represents 1 foot or 1 inch
    if config.current_grid_size == config.FOOT_GRID_SIZE:
        hypotenuse_inches = hypotenuse_pixels / config.FOOT_GRID_SIZE * 12
    else:  # config.current_grid_size == config.INCH_GRID_SIZE
        hypotenuse_inches = hypotenuse_pixels / config.INCH_GRID_SIZE

    mid_x, mid_y = (x1 + x2) // 2, (y1 + y2) // 2
    length_text = f"L: {hypotenuse_inches:.1f}\""
    font = pygame.font.SysFont(None, 18)
    text_surface = font.render(length_text, True, config.BEAM_TEXT_COLOR)  # Change to desired color
    screen.blit(text_surface, (mid_x - text_surface.get_width() // 2, mid_y + 10))  # Adjust the y-coordinate


def handle_beam_deletion(mouse_pos, beams, nodes):
    for beam in beams:
        node1_idx, node2_idx = beam
        node1, node2 = nodes[node1_idx], nodes[node2_idx]
        if point_to_segment_distance(mouse_pos, node1, node2) < config.NODE_RADIUS:
            beams.remove(beam)
            return True
    return False

def point_to_segment_distance(point, start, end):
    px, py = point
    sx, sy = start
    ex, ey = end
    line_mag = math.sqrt((ex - sx) ** 2 + (ey - sy) ** 2)
    if line_mag < 0.000001:
        return math.sqrt((px - sx) ** 2 + (py - sy) ** 2)
    u = ((px - sx) * (ex - sx) + (py - sy) * (ey - sy)) / (line_mag ** 2)
    if u < 0:
        ix, iy = sx, sy
    elif u > 1:
        ix, iy = ex, ey
    else:
        ix = sx + u * (ex - sx)
        iy = sy + u * (ey - sy)
    return math.sqrt((px - ix) ** 2 + (py - iy) ** 2)
