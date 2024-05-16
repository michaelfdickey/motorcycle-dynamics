import pygame
import sys
from ui_buttons import buttons, highlighted, checkboxes, checkbox_states, selected_button_group, draw_all_buttons, draw_label, draw_checkbox
import config

mass_input_active = False
input_text = ""
confirmation_active = False

def handle_button_click(mouse_pos):
    global highlighted, selected_button_group, confirmation_active
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
                    for edit_key in ["delete", "move", "modify", "clear"]:
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
            elif key == "clear":
                if selected_button_group == "edit":
                    confirmation_active = True
                    print("Clear button clicked, confirmation_active set to True")
            elif key in ["node", "beam", "fixture", "force", "torque", "mass"]:
                if selected_button_group == "create":
                    for other_key in ["node", "beam", "fixture", "force", "torque", "mass"]:
                        if other_key != key:
                            highlighted[other_key] = False
                    highlighted[key] = not highlighted[key]
            elif key in ["delete", "move", "modify"]:
                if selected_button_group == "edit":
                    for other_key in ["delete", "move", "modify", "clear"]:
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

def draw_confirmation_prompt(screen, title, confirmation_text, callback):
    print("Drawing confirmation prompt")
    font = config.font
    prompt_width, prompt_height = 300, 200
    prompt_rect = pygame.Rect((config.SCREEN_WIDTH - prompt_width) // 2, (config.SCREEN_HEIGHT - prompt_height) // 2, prompt_width, prompt_height)
    
    pygame.draw.rect(screen, config.SOFT_YELLOW, prompt_rect)
    pygame.draw.rect(screen, config.BLACK, prompt_rect, 2)
    
    title_surface = font.render(title, True, config.BLACK)
    screen.blit(title_surface, (prompt_rect.x + (prompt_width - title_surface.get_width()) // 2, prompt_rect.y + 20))
    
    confirmation_surface = font.render(confirmation_text, True, config.BLACK)
    screen.blit(confirmation_surface, (prompt_rect.x + (prompt_width - confirmation_surface.get_width()) // 2, prompt_rect.y + 60))
    
    yes_button = pygame.Rect(prompt_rect.x + 50, prompt_rect.y + 120, 80, 30)
    cancel_button = pygame.Rect(prompt_rect.x + 170, prompt_rect.y + 120, 80, 30)
    
    pygame.draw.rect(screen, config.WHITE, yes_button)
    pygame.draw.rect(screen, config.BLACK, yes_button, 2)
    pygame.draw.rect(screen, config.WHITE, cancel_button)
    pygame.draw.rect(screen, config.BLACK, cancel_button, 2)
    
    yes_surface = font.render("Yes", True, config.BLACK)
    screen.blit(yes_surface, (yes_button.x + (yes_button.width - yes_surface.get_width()) // 2, yes_button.y + 5))
    
    cancel_surface = font.render("Cancel", True, config.BLACK)
    screen.blit(cancel_surface, (cancel_button.x + (cancel_button.width - cancel_surface.get_width()) // 2, cancel_button.y + 5))
    
    return prompt_rect, yes_button, cancel_button

def handle_confirmation_click(mouse_pos, prompt_rect, yes_button, cancel_button, callback):
    global confirmation_active
    if yes_button.collidepoint(mouse_pos):
        print("Yes button clicked")
        callback()
        confirmation_active = False
    elif cancel_button.collidepoint(mouse_pos):
        print("Cancel button clicked")
        confirmation_active = False
    elif not prompt_rect.collidepoint(mouse_pos):
        confirmation_active = False
