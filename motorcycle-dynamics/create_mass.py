# create_mass.py

import pygame
import config

def handle_mass_click(mouse_pos, nodes, masses, highlighted, mass_value):
    if highlighted["create"] and highlighted["mass"]:
        for node in nodes:
            if (node[0] - config.NODE_RADIUS <= mouse_pos[0] <= node[0] + config.NODE_RADIUS) and (
                node[1] - config.NODE_RADIUS <= mouse_pos[1] <= node[1] + config.NODE_RADIUS
            ):
                masses.append((node, mass_value))

def draw_masses(screen, masses):
    for mass in masses:
        node, value = mass
        mass_size = 47  # Increase the size by another 30% (36 * 1.3 = 46.8)
        line_thickness = 3
        trapezoid_height = mass_size
        trapezoid_base_top = mass_size // 2
        trapezoid_base_bottom = mass_size
        node_x, node_y = node

        # Draw the trapezoid below the node
        trapezoid_points = [
            (node_x - trapezoid_base_bottom // 2, node_y + trapezoid_height),  # Bottom-left point
            (node_x + trapezoid_base_bottom // 2, node_y + trapezoid_height),  # Bottom-right point
            (node_x + trapezoid_base_top // 2, node_y + trapezoid_height - (trapezoid_height // 2)),  # Top-right point
            (node_x - trapezoid_base_top // 2, node_y + trapezoid_height - (trapezoid_height // 2))  # Top-left point
        ]
        pygame.draw.polygon(screen, config.RED, trapezoid_points, line_thickness)

        # Draw the vertical line connecting the node to the trapezoid
        pygame.draw.line(screen, config.RED, node, (node_x, node_y + trapezoid_height - (trapezoid_height // 2)), line_thickness)

        # Draw the mass value inside the trapezoid
        font = config.font
        value_surface = font.render(str(value), True, config.RED)
        value_rect = value_surface.get_rect(center=(node_x, node_y + trapezoid_height - (trapezoid_height // 2) / 2))
        screen.blit(value_surface, value_rect)

def handle_mass_deletion(mouse_pos, masses):
    for mass in masses:
        node, _ = mass
        mass_size = 47  # Should match the size used in draw_masses
        if (node[0] - mass_size // 2 <= mouse_pos[0] <= node[0] + mass_size // 2) and (
            node[1] <= mouse_pos[1] <= node[1] + mass_size):
            masses.remove(mass)
            return True
    return False