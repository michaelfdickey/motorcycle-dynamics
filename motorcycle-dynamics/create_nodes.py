# create_nodes.py

import pygame
import config

def handle_node_click(mouse_pos, nodes, highlighted, snap_to_grid, grid_size):
    if highlighted["create"] and highlighted["node"]:
        if snap_to_grid and grid_size:
            mouse_pos = (
                round(mouse_pos[0] / grid_size) * grid_size,
                round(mouse_pos[1] / grid_size) * grid_size,
            )
        nodes.append(mouse_pos)

def draw_nodes(screen, nodes):
    for node in nodes:
        pygame.draw.circle(screen, config.BRIGHT_YELLOW, node, config.NODE_RADIUS)

def handle_fixture_click(mouse_pos, nodes, fixtures, highlighted):
    if highlighted["create"] and highlighted["fixture"]:
        for node in nodes:
            if (node[0] - config.NODE_RADIUS <= mouse_pos[0] <= node[0] + config.NODE_RADIUS) and (
                node[1] - config.NODE_RADIUS <= mouse_pos[1] <= node[1] + config.NODE_RADIUS
            ):
                fixtures.append(node)

def draw_fixtures(screen, fixtures):
    for fixture in fixtures:
        fixture_size = 30  # Size of the fixture symbol
        line_thickness = 3  # Thickness of the lines
        triangle_height = fixture_size
        triangle_base_half = fixture_size  # Make the triangle wider
        node_x, node_y = fixture

        # Draw the triangle below the node
        triangle_points = [
            (node_x, node_y),  # Top point (at the node)
            (node_x - triangle_base_half, node_y + triangle_height),  # Bottom-left point
            (node_x + triangle_base_half, node_y + triangle_height)   # Bottom-right point
        ]
        pygame.draw.polygon(screen, config.BLUE, triangle_points, line_thickness)

        # Draw the comb-like teeth
        num_teeth = 5
        tooth_height = 5
        tooth_spacing = 2 * triangle_base_half / (num_teeth + 1)
        for i in range(1, num_teeth + 1):
            tooth_x = node_x - triangle_base_half + i * tooth_spacing
            pygame.draw.line(screen, config.BLUE, (tooth_x, node_y + triangle_height), (tooth_x, node_y + triangle_height + tooth_height), line_thickness)

def handle_fixture_deletion(mouse_pos, fixtures):
    for fixture in fixtures:
        fixture_size = 30  # Should match the size used in draw_fixtures
        if (fixture[0] - fixture_size // 2 <= mouse_pos[0] <= fixture[0] + fixture_size // 2) and (
            fixture[1] <= mouse_pos[1] <= fixture[1] + fixture_size):
            fixtures.remove(fixture)
            return True
    return False

def handle_node_deletion(mouse_pos, nodes):
    for node in nodes:
        if (node[0] - config.NODE_RADIUS <= mouse_pos[0] <= node[0] + config.NODE_RADIUS) and (
            node[1] - config.NODE_RADIUS <= mouse_pos[1] <= node[1] + config.NODE_RADIUS
        ):
            nodes.remove(node)
            return True
    return False