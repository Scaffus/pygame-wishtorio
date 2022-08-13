import pygame
from colors import Colors
from tile import PlaceholderTile
from random import randint
import utilities as utils

class Map(pygame.sprite.Sprite):
    def __init__(self, game) :
        self.GAME = game
        self.floor = pygame.surface.Surface(self.GAME.SIZE)
        self.floor_tiles = {}
        self.chunks = {}
        self.tiles = {}
        self.tile_pos = []

        self.grid = pygame.surface.Surface(self.GAME.SIZE)
        self.grid.set_colorkey((0, 0, 0))
        self.create_grid()
        self.show_grid = False

        self.map = pygame.surface.Surface(self.GAME.SIZE)
        self.map.set_colorkey((0, 0, 0))
        self.create_floor()

        self.upd_ = 0
        self.upd_f = 2

    def create_grid(self):
        for y in range(round(self.GAME.HEIGHT / self.GAME.GRID_SIZE) + 1):
            pygame.draw.line(self.grid, (Colors.gray), (0, y * self.GAME.GRID_SIZE - .5), (self.GAME.WIDTH, y * self.GAME.GRID_SIZE - .5), 2)
        for x in range(round(self.GAME.WIDTH / self.GAME.GRID_SIZE) + 1):
            pygame.draw.line(self.grid, (Colors.gray), (x * self.GAME.GRID_SIZE - .5, 0), (x * self.GAME.GRID_SIZE - .5, self.GAME.HEIGHT), 2)

    def create_floor(self):
        mat_stone_path = self.GAME.MATERIALS['wishtorio:stone_path']
        nbr_of_stone_tile = mat_stone_path.SIZE[0]
        stone_path = mat_stone_path.sprite_grid_sized
        for y in range(round(self.GAME.HEIGHT / self.GAME.GRID_SIZE) + 1):
            for x in range(round(self.GAME.WIDTH / self.GAME.GRID_SIZE) + 1):
                pos = (x * self.GAME.GRID_SIZE, y * self.GAME.GRID_SIZE)
                grab_rect = pygame.Rect(randint(0, nbr_of_stone_tile-1) * self.GAME.GRID_SIZE, 0, self.GAME.GRID_SIZE, self.GAME.GRID_SIZE)
                tile = stone_path.subsurface(grab_rect)
                self.floor_tiles[pos] = tile
                self.tile_pos.append(pos)
                
    def draw(self):
        self.GAME.DISPLAY.blit(self.floor, (0, 0))

        if self.upd_ > self.upd_f:
            self.map.fill(Colors.black)
            self.GAME.PLAYER.CURRENT_CHUNK = (utils.round_to_multiple(self.GAME.PLAYER.POS[0], self.GAME.CHUNK_SIZE), utils.round_to_multiple(self.GAME.PLAYER.POS[1], self.GAME.CHUNK_SIZE))
            # i_s = list(self.tiles.keys()).index(self.GAME.PLAYER.CURRENT_CHUNK)
            # i_f = list(self.tiles.keys()).index((
            #     self.GAME.PLAYER.CURRENT_CHUNK[0] + self.GAME.CHUNK_SIZE * self.GAME.GRID_SIZE,
            #     self.GAME.PLAYER.CURRENT_CHUNK[1] + self.GAME.CHUNK_SIZE * self.GAME.GRID_SIZE))
            start_pos = self.GAME.PLAYER.CURRENT_CHUNK
            end_pos = (self.GAME.PLAYER.CURRENT_CHUNK[0] + (self.GAME.GRID_SIZE * self.GAME.CHUNK_SIZE),
                            self.GAME.PLAYER.CURRENT_CHUNK[1] + (self.GAME.GRID_SIZE * self.GAME.CHUNK_SIZE))
            
            start_index = self.tile_pos.index(start_pos)
            end_index = self.tile_pos.index(end_pos)
            
            tiles_pos = self.tile_pos[start_index:end_index]
            for pos in tiles_pos:
                self.floor_tiles[pos].blit(self.GAME.DISPLAY, pos)
                
            # [self.tiles[pos].draw() for pos in self.tiles]
            self.upd_ = 0
        else: self.upd_ += 1

        self.GAME.DISPLAY.blit(self.map, (0, 0))
        if self.show_grid: self.GAME.DISPLAY.blit(self.grid, (0, 0))

    def update(self):
        [self.tiles[pos].update() for pos in self.tiles]