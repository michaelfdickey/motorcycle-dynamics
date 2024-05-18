# create_beams.py

import pygame
import config

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
        pygame.draw.line(screen, config.WHITE, beam[0], beam[1], 2)

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
