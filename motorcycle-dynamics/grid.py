"""
import pygame
from config import SCREEN_WIDTH, SCREEN_HEIGHT, MEDIUM_GRAY, DARKER_GRAY

FOOT_GRID_SIZE = 144  # 1' grid size in pixels
INCH_GRID_SIZE = 12  # 1" grid size in pixels

def draw_grid(screen, grid_size, color):
    for x in range(0, SCREEN_WIDTH, grid_size):
        pygame.draw.line(screen, color, (x, 0), (x, SCREEN_HEIGHT))
    for y in range(0, SCREEN_HEIGHT, grid_size):
        pygame.draw.line(screen, color, (0, y), (SCREEN_WIDTH, y))

def draw_grids(screen, checkbox_states):
    if checkbox_states["1in"]:
        draw_grid(screen, INCH_GRID_SIZE, DARKER_GRAY)  # 1" grid
    if checkbox_states["1ft"]:
        draw_grid(screen, FOOT_GRID_SIZE, MEDIUM_GRAY)  # 1' grid
"""
        

import pygame
import config

def draw_grid(screen, grid_size, color):
    for x in range(0, config.SCREEN_WIDTH, grid_size):
        pygame.draw.line(screen, color, (x, 0), (x, config.SCREEN_HEIGHT))
    for y in range(0, config.SCREEN_HEIGHT, grid_size):
        pygame.draw.line(screen, color, (0, y), (config.SCREEN_WIDTH, y))

def draw_grids(screen, checkbox_states):
    if checkbox_states["1in"]:
        draw_grid(screen, config.INCH_GRID_SIZE, config.DARKER_GRAY)
    if checkbox_states["1ft"]:
        draw_grid(screen, config.FOOT_GRID_SIZE, config.MEDIUM_GRAY)