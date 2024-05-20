# create_beams.py

import pygame
import config
import math

def handle_beam_click(mouse_pos, nodes, beams, highlighted, beam_start_node):
    if highlighted["create"] and highlighted["beam"]:
        for node in nodes:
            if (node[0] - config.NODE_RADIUS <= mouse_pos[0] <= node[0] + config.NODE_RADIUS) and (
                node[1] - config.NODE_RADIUS <= mouse_pos[1] <= node[1] + config.NODE_RADIUS
            ):
                if beam_start_node is None:
                    beam_start_node = node
                else:
                    beams.append((beam_start_node, node))
                    beam_start_node = None
                break
    return beam_start_node

def draw_beams(screen, beams):
    for beam in beams:
        start, end = beam
        # Calculate beam properties
        dx = end[0] - start[0]
        dy = end[1] - start[1]
        length = math.sqrt(dx**2 + dy**2)
        angle = math.degrees(math.atan2(dy, dx))
        horizontal_length = abs(end[0] - start[0])
        vertical_length = abs(end[1] - start[1])
        
        # Draw the beam
        pygame.draw.line(screen, config.WHITE, start, end, 2)
        
        # Display beam properties
        midpoint = ((start[0] + end[0]) / 2, (start[1] + end[1]) / 2)
        display_text = f"{length:.2f}"
        text_surface = config.small_font.render(display_text, True, config.WHITE)
        screen.blit(text_surface, (midpoint[0] - text_surface.get_width() / 2, midpoint[1] + 10))

def handle_beam_deletion(mouse_pos, beams):
    for beam in beams:
        start, end = beam
        distance = point_to_segment_distance(mouse_pos, start, end)
        if distance < config.NODE_RADIUS:
            beams.remove(beam)
            break

def point_to_segment_distance(point, start, end):
    # Calculate the distance from a point to a line segment
    px, py = point
    sx, sy = start
    ex, ey = end
    line_mag = ((ex - sx) ** 2 + (ey - sy) ** 2) ** 0.5
    if line_mag == 0:
        return ((px - sx) ** 2 + (py - sy) ** 2) ** 0.5
    u = ((px - sx) * (ex - sx) + (py - sy) * (ey - sy)) / (line_mag ** 2)
    if u < 0:
        closest_point = (sx, sy)
    elif u > 1:
        closest_point = (ex, ey)
    else:
        closest_point = (sx + u * (ex - sx), sy + u * (ey - sy))
    return ((px - closest_point[0]) ** 2 + (py - closest_point[1]) ** 2) ** 0.5
