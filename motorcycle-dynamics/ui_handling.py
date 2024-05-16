import pygame
import sys
from ui_buttons import buttons, highlighted, checkboxes, checkbox_states, draw_all_buttons
import config

mass_input_active = False
input_text = "100"

def draw_ui(screen, nodes, beams):
    global mass_input_active, input_text

    # Left UI bar
    pygame.draw.rect(screen, config.SOFT_YELLOW, (0, 0, config.UI_BAR_WIDTH, config.SCREEN_HEIGHT))
    # Top UI bar
    pygame.draw.rect(screen, config.SOFT_YELLOW, (0, 0, config.SCREEN_WIDTH, config.TOP_BAR_HEIGHT))
    # Draw all buttons
    draw_all_buttons(screen, config.font, config.small_font)

    # Draw mass input box if mass is selected
    if highlighted["create"] and highlighted["mass"]:
        pygame.draw.rect(screen, config.WHITE, config.mass_input_rect)  # White background
        pygame.draw.rect(screen, config.BLACK, config.mass_input_rect, 2)  # Black outline
        label = config.small_font.render(input_text, True, config.BLACK)
        screen.blit(label, (config.mass_input_rect.x + 5, config.mass_input_rect.y + 5))

    # Draw node and beam tally
    node_tally_text = config.small_font.render(f"Nodes: {len(nodes)}", True, config.RED)
    beam_tally_text = config.small_font.render(f"Beams: {len(beams)}", True, config.RED)
    screen.blit(node_tally_text, (config.SCREEN_WIDTH - 100, config.SCREEN_HEIGHT - 40))
    screen.blit(beam_tally_text, (config.SCREEN_WIDTH - 100, config.SCREEN_HEIGHT - 20))

def handle_button_click(mouse_pos):
    global highlighted
    for key in buttons:
        if buttons[key].collidepoint(mouse_pos):
            if key == "exit":
                pygame.quit()
                sys.exit()
            elif key == "create":
                highlighted["create"] = not highlighted["create"]
            else:
                if highlighted["create"]:
                    # Unhighlight other create options
                    for other_key in ["node", "beam", "fixture", "force", "torque", "mass"]:
                        if other_key != key:
                            highlighted[other_key] = False
                    highlighted[key] = not highlighted[key]
            return

def handle_checkbox_click(mouse_pos):
    global checkbox_states
    for key in checkboxes:
        if checkboxes[key].collidepoint(mouse_pos):
            checkbox_states[key] = not checkbox_states[key]
            return

def handle_keydown_event(event):
    global mass_value, mass_input_active, input_text
    if event.key == pygame.K_RETURN:
        try:
            mass_value = int(input_text)
        except ValueError:
            mass_value = 100  # Default to 100 if invalid input
        mass_input_active = False
    elif event.key == pygame.K_BACKSPACE:
        input_text = input_text[:-1]
    else:
        input_text += event.unicode
