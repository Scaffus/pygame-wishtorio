import pygame
from colors import Colors
import utilities as utils

class Cursor(pygame.sprite.Sprite):
    def __init__(self, game) -> None:
        self.GAME = game
        self.cursor = pygame.image.load('./assets/hud/cursor.cur').convert_alpha()

    def update(self):
        pass

    def draw(self):
        self.GAME.DISPLAY.blit(self.cursor, (pygame.mouse.get_pos()))