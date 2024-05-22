# create_weight.py
import pygame
import config

def handle_weight_click(mouse_pos, nodes, weights, highlighted, weight_value):
    if highlighted["create"] and highlighted["weight"]:
        for idx, node in enumerate(nodes):
            if (node[0] - config.NODE_RADIUS <= mouse_pos[0] <= node[0] + config.NODE_RADIUS) and (node[1] - config.NODE_RADIUS <= mouse_pos[1] <= node[1] + config.NODE_RADIUS):
                weights.append((idx, weight_value))

def draw_weights(screen, weights, nodes):
    for weight in weights:
        node_idx, value = weight
        x, y = nodes[node_idx]
        font = pygame.font.SysFont(None, 18)
        text_surface = font.render(f"{value} lbs", True, config.BLACK)
        pygame.draw.polygon(screen, config.RED, [(x, y), (x - 10, y + 20), (x + 10, y + 20)])
        screen.blit(text_surface, (x - text_surface.get_width() // 2, y + 25))

def handle_weight_deletion(mouse_pos, weights, nodes):
    for weight in weights:
        node_idx, _ = weight
        x, y = nodes[node_idx]
        if (x - config.NODE_RADIUS <= mouse_pos[0] <= x + config.NODE_RADIUS) and (y - config.NODE_RADIUS <= mouse_pos[1] <= y + config.NODE_RADIUS):
            weights.remove(weight)
            return True
    return False
