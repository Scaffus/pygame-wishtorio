import pygame
from colors import Colors
import utilities as utils

class Highlight(pygame.sprite.Sprite):
    def __init__(self, game) -> None:
        self.GAME = game
        self.highlight_size_ratio = (self.GAME.GRID_SIZE / 2) - self.GAME.GRID_SIZE / 8
        self.highlight_surf = pygame.transform.scale(pygame.image.load("./assets/highlight.png").convert_alpha(), (self.GAME.GRID_SIZE + self.highlight_size_ratio, self.GAME.GRID_SIZE + self.highlight_size_ratio))
        self.rect = self.highlight_surf.get_rect()
        self.rect.topleft = (self.highlight_size_ratio / 2, self.highlight_size_ratio / 2)
        self.highlight_pos = (0, 0)

    def update(self):
        mpos = pygame.mouse.get_pos()
        hovered_tile_pos = (
            utils.round_to_multiple(mpos[0] - self.GAME.GRID_SIZE / 2, self.GAME.GRID_SIZE),
            utils.round_to_multiple(mpos[1] - self.GAME.GRID_SIZE / 2, self.GAME.GRID_SIZE))
        self.GAME.HOVERED_TILE_POS = hovered_tile_pos

        self.highlight_pos = (
            hovered_tile_pos[0] - self.highlight_size_ratio / 2,
            hovered_tile_pos[1] - self.highlight_size_ratio / 2)

    def draw(self):
        self.GAME.DISPLAY.blit(self.highlight_surf, (self.highlight_pos))