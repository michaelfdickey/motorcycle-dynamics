# draw_ui.py

import pygame
import config
from ui_buttons import buttons, checkboxes, highlighted, checkbox_states

def draw_all_buttons(screen, font, small_font):
    for key in buttons:
        pygame.draw.rect(screen, config.WHITE, buttons[key])
        pygame.draw.rect(screen, config.BLACK, buttons[key], 2)
        label_surface = font.render(key.capitalize(), True, config.BLACK)
        label_rect = label_surface.get_rect(center=buttons[key].center)
        screen.blit(label_surface, label_rect)
        if highlighted[key]:
            pygame.draw.rect(screen, config.BRIGHT_YELLOW, buttons[key], 3)  # Highlight with bright yellow

    label_surface = font.render("Display", True, config.BLACK)
    screen.blit(label_surface, (10, config.SCREEN_HEIGHT - 190))

def draw_label(screen, rect, text, font):
    text_surface = font.render(text, True, config.BLACK)
    screen.blit(text_surface, (rect.x + 5, rect.y + 5))

def draw_checkbox(screen, rect, label, state):
    pygame.draw.rect(screen, config.WHITE, rect)
    pygame.draw.rect(screen, config.BLACK, rect, 2)
    if state:
        pygame.draw.line(screen, config.BLACK, (rect.left + 5, rect.centery), (rect.right - 5, rect.centery), 2)
    label_surface = config.small_font.render(label, True, config.BLACK)  # Use small_font here
    screen.blit(label_surface, (rect.right + 5, rect.centery - label_surface.get_height() // 2))