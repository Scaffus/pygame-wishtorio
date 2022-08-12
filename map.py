from random import random
import pygame
from colors import Colors
from tile import Tile
from random import randint

class Map(pygame.sprite.Sprite):
    def __init__(self, game) -> None:
        self.GAME = game
        self.floor = pygame.surface.Surface(self.GAME.SIZE)
        self.tiles = {}

        self.grid = pygame.surface.Surface(self.GAME.SIZE)
        self.grid.set_colorkey((0, 0, 0))
        self.create_grid()
        self.show_grid = False

        self.map = pygame.surface.Surface(self.GAME.SIZE)
        self.map.set_colorkey((0, 0, 0))
        self.create_floor()

        self.upd_ = 0
        self.upd_f = 1

    def create_grid(self):
        for y in range(round(self.GAME.HEIGHT / self.GAME.GRID_SIZE) + 1):
            pygame.draw.line(self.grid, (Colors.gray), (0, y * self.GAME.GRID_SIZE - .5), (self.GAME.WIDTH, y * self.GAME.GRID_SIZE - .5), 2)
        for x in range(round(self.GAME.WIDTH / self.GAME.GRID_SIZE) + 1):
            pygame.draw.line(self.grid, (Colors.gray), (x * self.GAME.GRID_SIZE - .5, 0), (x * self.GAME.GRID_SIZE - .5, self.GAME.HEIGHT), 2)

    def create_floor(self):
        nbr_of_stone_tile = 16
        stone_path = pygame.transform.scale(pygame.image.load("./assets/materials/stone_path.png").convert(), (self.GAME.GRID_SIZE * nbr_of_stone_tile, self.GAME.GRID_SIZE))
        for y in range(round(self.GAME.HEIGHT / self.GAME.GRID_SIZE) + 1):
            for x in range(round(self.GAME.WIDTH / self.GAME.GRID_SIZE) + 1):
                pos = (x * self.GAME.GRID_SIZE, y * self.GAME.GRID_SIZE)
                grab_rect = pygame.Rect(randint(0, 15) * self.GAME.GRID_SIZE, 0, self.GAME.GRID_SIZE, self.GAME.GRID_SIZE)
                tile = stone_path.subsurface(grab_rect)
                self.floor.blit(tile, pos)

    def draw(self):
        self.GAME.DISPLAY.blit(self.floor, (0, 0))

        if self.upd_ > self.upd_f:
            self.map.fill(Colors.black)
            [self.tiles[pos].draw() for pos in self.tiles]
            self.upd_ = 0
        else: self.upd_ += 1

        self.GAME.DISPLAY.blit(self.map, (0, 0))
        if self.show_grid: self.GAME.DISPLAY.blit(self.grid, (0, 0))

    def update(self):
        [self.tiles[pos].update() for pos in self.tiles]