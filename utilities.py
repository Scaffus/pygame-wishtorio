import pygame
from colors import Colors
from pathlib import Path

path = Path(__file__).parent

def font(text="Placeholder", size=24, color=Colors.black, anti_alias=False, background=False, background_color=(Colors.dark)):
    font = pygame.font.Font(path / 'assets/fonts/REEMKUFI-REGULAR.ttf', size)
    if background:
        return font.render(text, anti_alias, color, background_color)
    return font.render(text, anti_alias, color)

def round_to_multiple(x, multiple):
    return multiple * round(x / multiple)