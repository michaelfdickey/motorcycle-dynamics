# main.py

import pygame
import sys
from create_nodes import handle_node_click, draw_nodes, handle_fixture_click, draw_fixtures, handle_node_deletion, handle_fixture_deletion
from create_beams import handle_beam_click, draw_beams, handle_beam_deletion
from create_mass import handle_mass_click, draw_masses
from grid import draw_grids
from ui_handling import draw_ui, handle_button_click, handle_checkbox_click, handle_keydown_event, mass_input_active, input_text, draw_confirmation_prompt_in_ui_bar, handle_confirmation_click_in_ui_bar
import config
from config import FOOT_GRID_SIZE, INCH_GRID_SIZE  # Import the necessary constants
from ui_buttons import highlighted, checkbox_states

nodes = []
beams = []
fixtures = []
masses = []
beam_start_node = None
mass_value = 100
confirmation_active = False

def clear_all():
    global nodes, beams, fixtures, masses
    print("Clearing all entities")
    nodes = []
    beams = []
    fixtures = []
    masses = []

def main(screen):
    global nodes, beams, fixtures, masses, beam_start_node, mass_value, mass_input_active, confirmation_active
    global prompt_rect, yes_button, cancel_button

    running = True
    while running:
        screen.fill(config.BLACK)

        draw_grids(screen, checkbox_states)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if confirmation_active:
                    yes_rect, no_rect = draw_confirmation_prompt_in_ui_bar(screen)
                    handle_confirmation_click_in_ui_bar(mouse_pos, yes_rect, no_rect, clear_all)
                else:
                    if mouse_pos[0] <= config.UI_BAR_WIDTH or mouse_pos[1] <= config.TOP_BAR_HEIGHT:
                        handle_button_click(mouse_pos)
                        handle_checkbox_click(mouse_pos)
                        if highlighted["create"] and highlighted["mass"]:
                            if config.mass_input_rect.collidepoint(mouse_pos):
                                mass_input_active = True
                            else:
                                mass_input_active = False
                    else:
                        snap_to_grid = checkbox_states["snap"]
                        if checkbox_states["1in"]:
                            grid_size = INCH_GRID_SIZE
                        elif checkbox_states["1ft"]:
                            grid_size = FOOT_GRID_SIZE
                        else:
                            grid_size = None
                        if highlighted["create"]:
                            handle_node_click(mouse_pos, nodes, highlighted, snap_to_grid, grid_size)
                            beam_start_node = handle_beam_click(mouse_pos, nodes, beams, highlighted, beam_start_node)
                            handle_fixture_click(mouse_pos, nodes, fixtures, highlighted)
                            handle_mass_click(mouse_pos, nodes, masses, highlighted, mass_value)
                        elif highlighted["edit"] and highlighted["delete"]:
                            if not handle_fixture_deletion(mouse_pos, fixtures):
                                if not handle_node_deletion(mouse_pos, nodes):
                                    handle_beam_deletion(mouse_pos, beams)
            elif event.type == pygame.KEYDOWN and mass_input_active:
                handle_keydown_event(event)

        draw_ui(screen, nodes, beams)
        draw_nodes(screen, nodes)
        draw_beams(screen, beams)
        draw_fixtures(screen, fixtures)
        draw_masses(screen, masses)

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
    pygame.display.set_caption('Motorcycle Designer')
    main(screen)
