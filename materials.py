import pygame
import json

def load_tiles(game):
    tiles = {}
    with open('tiles.json', 'r') as f:
        materials = json.load(f)
    for material in materials:
        match material.type:
            case 0:
                new_material = Material(game, material, material.type, material.size)
            case 1:
                new_generator = Generator
        tiles[material] = (new_material)
    return tiles

class Material:
    def __init__(self, game, name, type, size) -> None:
        self.GAME = game
        self.NAME = name
        self.SIZE = size
        # ? 0 = default
        # ? 1 = generator
        # ? 2 = inventory
        self.TYPE = type
        
        self.texture_path = f'./assets/materials/{self.NAME.replace("wishtorio:", "")}.png'
        try:
            self.sprite = pygame.image.load(self.texture_path).convert_alpha()
        except FileNotFoundError:
            self.sprite = pygame.image.load('./assets/materials/not_found.png').convert_alpha()
        self.sprite_grid_sized = pygame.transform.scale(self.sprite, (self.GAME.GRID_SIZE, self.GAME.GRID_SIZE))
        self.sprite_slot_sized = pygame.transform.scale(self.sprite, (self.GAME.SLOT_SIZE, self.GAME.SLOT_SIZE))