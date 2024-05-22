import pygame

# Initialize Pygame to use fonts
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 1500
SCREEN_HEIGHT = 1000

# UI dimensions
UI_BAR_WIDTH = int(120 * 1.2)  # 20% larger than original width of 120
TOP_BAR_HEIGHT = 20

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SOFT_YELLOW = (240, 230, 140)
BRIGHT_YELLOW = (255, 255, 0)
MEDIUM_GRAY = (120, 120, 120)
DARKER_GRAY = (60, 60, 60)
BLUE = (0, 0, 255)
FIXTURE_COLOR = BLUE
RED = (255, 0, 0)
BEAM_COLOR = (255,255,255)
TEXT_LENGTH_COLOR = (240,240,240)
BEAM_TEXT_COLOR = (240,140,240)

# Grid sizes
FOOT_GRID_SIZE = 144
INCH_GRID_SIZE = 12

# Grid settings
current_grid_size = FOOT_GRID_SIZE  # Default grid size

# Node radius
NODE_RADIUS = 5

# Mass input rectangle
mass_input_rect = pygame.Rect(10, 25 + 4 * (40 * 0.8 + 10), 100, 40 * 0.8)

# Fonts
font = pygame.font.SysFont(None, 22)  # Reduced font size by 10%
small_font = pygame.font.SysFont(None, 18)  # Smaller font for the tally
