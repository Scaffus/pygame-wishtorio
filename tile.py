import time
import pygame
from colors import Colors
import utilities as utils
import json

def load_tiles(game):
    tiles = {}
    with open('tiles.json', 'r') as f:
        tiles = json.load(f)
    for tile in tiles:
        match tile.type:
            case 0:
                new = Tile(game, tile, tile.type, tile.size)
            case 1:
                new = Generator(game, tile)
        tiles[tile] = (new)
    return tiles

class Material:
    def __init__(self, game, name, type, size) -> None:
        self.GAME = game
        self.NAME = name
        self.TYPE = type
        self.SIZE = size
        self.sprite = pygame.image.load(f'./assets/materials/{self.NAME.replace(self.GAME.PREFIX, "")}')
        self.sprite_slot_sized = pygame.transform.scale(self.sprite.copy(), (self.GAME.SLOT_SIZE, self.GAME.SLOT_SIZE))
        self.sprite_grid_sized = pygame.transform.scale(self.sprite.copy(), (self.GAME.GRID_SIZE, self.GAME.GRID_SIZE))
    

class Tile(pygame.sprite.Sprite):
    def __init__(self, game, material, pos=(0, 0)) -> None:
        self.GAME = game
        self.MATERIAL = material
        self.POS = pos
        self.rect = self.MATERIAL.sprite_grid_sized.get_rect()
        self.rect.topleft = self.POS
        
    def change_type(self):
        pass

    def draw(self):
        self.GAME.MAP.map.blit(self.sprite, self.POS)

class Generator(Tile):
    def __init__(self, game, material, pos) -> None:
        self.GAME = game
        self.MATERIAL = material
        self.POS = pos
        self.sprite = self.MATERIAL.sprite_grid_sized
        self.rect = self.sprite.get_rect()

        self.cooldown_start = time.time()
        self.generate_time = 3
    
    def update(self):
        if self.cooldown_start + self.generate_time < self.GAME.now:
            self.GAME.ENERGY += 1
            self.cooldown_start = self.GAME.now