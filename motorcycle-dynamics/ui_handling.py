import pygame
import sys
from ui_buttons import buttons, highlighted, checkboxes, checkbox_states, selected_button_group, draw_all_buttons, draw_label, draw_checkbox
import config

mass_input_active = False
input_text = ""

def handle_button_click(mouse_pos):
    global highlighted, selected_button_group
    for key in buttons:
        if buttons[key].collidepoint(mouse_pos):
            print(f"Button {key} clicked")
            if key == "exit":
                pygame.quit()
                sys.exit()
            elif key == "create":
                highlighted["create"] = not highlighted["create"]
                if highlighted["create"]:
                    highlighted["edit"] = False
                    selected_button_group = "create"
                    for edit_key in ["delete", "move", "modify"]:
                        highlighted[edit_key] = False
                else:
                    selected_button_group = None
            elif key == "edit":
                highlighted["edit"] = not highlighted["edit"]
                if highlighted["edit"]:
                    highlighted["create"] = False
                    selected_button_group = "edit"
                    for create_key in ["node", "beam", "fixture", "force", "torque", "mass"]:
                        highlighted[create_key] = False
                else:
                    selected_button_group = None
            elif key in ["node", "beam", "fixture", "force", "torque", "mass", "delete_nodes", "delete_beams", "delete_fixtures", "delete_weights"]:
                if selected_button_group == "create":
                    for other_key in ["node", "beam", "fixture", "force", "torque", "mass"]:
                        if other_key != key:
                            highlighted[other_key] = False
                    highlighted[key] = not highlighted[key]
                elif selected_button_group == "edit":
                    for other_key in ["delete_nodes", "delete_beams", "delete_fixtures", "delete_weights"]:
                        if other_key != key:
                            highlighted[other_key] = False
                    highlighted[key] = not highlighted[key]
            return

def handle_checkbox_click(mouse_pos):
    for key in checkboxes:
        if checkboxes[key].collidepoint(mouse_pos):
            checkbox_states[key] = not checkbox_states[key]
            return

def handle_keydown_event(event):
    global input_text
    if event.key == pygame.K_BACKSPACE:
        input_text = input_text[:-1]
    else:
        input_text += event.unicode

def draw_ui(screen, nodes, beams):
    font = config.font
    small_font = config.small_font
    
    pygame.draw.rect(screen, config.SOFT_YELLOW, (0, 0, config.UI_BAR_WIDTH, config.SCREEN_HEIGHT))
    pygame.draw.rect(screen, config.SOFT_YELLOW, (0, 0, config.SCREEN_WIDTH, config.TOP_BAR_HEIGHT))
    
    draw_all_buttons(screen, font, small_font)
    
    if highlighted["create"] and highlighted["mass"]:
        pygame.draw.rect(screen, config.WHITE, config.mass_input_rect)
        pygame.draw.rect(screen, config.BLACK, config.mass_input_rect, 2)
        draw_label(screen, config.mass_input_rect, input_text, font)
    
    tally_text = f"Nodes: {len(nodes)}  Beams: {len(beams)}"
    tally_surface = small_font.render(tally_text, True, (255, 0, 0))
    screen.blit(tally_surface, (config.SCREEN_WIDTH - tally_surface.get_width() - 10, config.SCREEN_HEIGHT - tally_surface.get_height() - 10))
