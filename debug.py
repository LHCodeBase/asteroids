import pygame
from constants import DEBUG_TEXT_COLOR 

pygame.font.init()
FONT = pygame.font.Font(None, 24)

def show_variables(screen, *args):
    pygame.display.set_caption("Debug Overlay")
    line = 40
    for arg in args:
        rendered_text = FONT.render(arg, True, DEBUG_TEXT_COLOR)
        screen.blit(rendered_text, (20, line))
        line += 30
    pass
