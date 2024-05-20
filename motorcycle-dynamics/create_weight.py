# create_weight.py

import pygame
import config

def handle_weight_click(mouse_pos, nodes, weights, highlighted, weight_value):
    if highlighted["create"] and highlighted["weight"]:
        for node in nodes:
            if (node[0] - config.NODE_RADIUS <= mouse_pos[0] <= node[0] + config.NODE_RADIUS) and (node[1] - config.NODE_RADIUS <= mouse_pos[1] <= node[1] + config.NODE_RADIUS):
                weights.append((node[0], node[1], weight_value))

def draw_weights(screen, weights):
    for weight in weights:
        x, y, weight_value = weight
        pygame.draw.polygon(screen, config.RED, [(x - 10, y + 10), (x + 10, y + 10), (x, y + 20)])
        text_surface = config.small_font.render(f"{weight_value}", True, config.RED)
        screen.blit(text_surface, (x - 10, y + 25))

def handle_weight_deletion(mouse_pos, weights):
    for weight in weights:
        if (weight[0] - 10 <= mouse_pos[0] <= weight[0] + 10) and (weight[1] + 10 <= mouse_pos[1] <= weight[1] + 30):
            weights.remove(weight)
            return True
    return False
