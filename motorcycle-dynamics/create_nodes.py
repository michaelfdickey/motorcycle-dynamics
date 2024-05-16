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
        fixture_rect = pygame.Rect(fixture[0] - 10, fixture[1] - 10, 20, 20)
        pygame.draw.rect(screen, config.BLUE, fixture_rect, 3)
        pygame.draw.line(screen, config.BLUE, (fixture[0] - 10, fixture[1] - 10), (fixture[0] + 10, fixture[1] + 10), 3)
        pygame.draw.line(screen, config.BLUE, (fixture[0] + 10, fixture[1] - 10), (fixture[0] - 10, fixture[1] + 10), 3)

def handle_node_deletion(mouse_pos, nodes):
    for node in nodes:
        if (node[0] - config.NODE_RADIUS <= mouse_pos[0] <= node[0] + config.NODE_RADIUS) and (
            node[1] - config.NODE_RADIUS <= mouse_pos[1] <= node[1] + config.NODE_RADIUS
        ):
            nodes.remove(node)
            break
