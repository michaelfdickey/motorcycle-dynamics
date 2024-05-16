import pygame

# Screen dimensions
SCREEN_WIDTH = 1500
SCREEN_HEIGHT = 1000

# Colors
BLACK = (0, 0, 0)
SOFT_YELLOW = (255, 255, 224)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
LIGHT_GRAY = (200, 200, 200)
MEDIUM_GRAY = (120, 120, 120)
DARKER_GRAY = (60, 60, 60)

# UI dimensions
UI_BAR_WIDTH = int(120 * 1.2)  # 20% larger than original width of 120
TOP_BAR_HEIGHT = 20
BUTTON_HEIGHT = int(40 * 0.8)  # 20% shorter
BUTTON_WIDTH = 60  # Increased width for larger buttons
BUTTON_SPACING = 10
EXIT_BUTTON_HEIGHT = 30
CHECKBOX_SIZE = 20

# Fonts
pygame.init()
font = pygame.font.SysFont(None, 22)  # Reduced font size by 10%
small_font = pygame.font.SysFont(None, 18)  # Smaller font for the tally

# Mass input rect
mass_input_rect = pygame.Rect(10, 25 + 4 * (BUTTON_HEIGHT + BUTTON_SPACING), 100, BUTTON_HEIGHT)
