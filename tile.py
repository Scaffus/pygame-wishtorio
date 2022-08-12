import time
import pygame
import json

def load_materials(game):
    """
    Loads tiles as objects and returns them in a list
    """
    tiles = {}
    materials = {}
    with open('tiles.json', 'r') as f:
        tiles = json.load(f)
    for tile in tiles:
        name = tile
        tile = tiles[tile]
        materials[name] = Material(game, tile, name)
    return materials

class Material:
    def __init__(self, game, tile, name):
        self.GAME = game
        self.TILE = tile
        self.NAME = name
        self.TYPE = self.TILE['type']
        self.SIZE = self.TILE['size']
        self.sprite = pygame.image.load(f'./assets/materials/{self.NAME.replace(self.GAME.PREFIX, "")}.png')
        self.sprite_slot_sized = pygame.transform.scale(self.sprite.copy(), (self.GAME.SLOT_SIZE, self.GAME.SLOT_SIZE))
        self.sprite_grid_sized = pygame.transform.scale(self.sprite.copy(), (self.GAME.GRID_SIZE * self.SIZE[0], self.GAME.GRID_SIZE * self.SIZE[1]))
    

class Tile(pygame.sprite.Sprite):
    def __init__(self, game, material, pos=(0, 0)):
        self.GAME = game
        self.MATERIAL = material
        self.POS = pos
        self.rect = self.MATERIAL.sprite_grid_sized.get_rect()
        self.rect.topleft = self.POS

    def draw(self):
        self.GAME.MAP.map.blit(self.sprite, self.POS)

class GeneratorTile(Tile):
    def __init__(self, game, material, pos):
        self.GAME = game
        self.MATERIAL = material
        self.POS = pos
        self.sprite = self.MATERIAL.sprite_grid_sized
        self.rect = self.sprite.get_rect()

        self.cooldown_start = time.time()
        self.generator_cooldown = self.MATERIAL.TILE['generator_cooldown']
        self.generated_material = self.MATERIAL.TILE['generated_material']
        self.number_of_generated_material = self.MATERIAL.TILE['number_of_generated_material']
        self.generator_energy_cost = self.MATERIAL.TILE['generator_energy_cost']
    
    def update(self):
        if self.cooldown_start + self.generator_cooldown < self.GAME.now:
            if self.GAME.ENERGY > self.generator_energy_cost:
                self.GAME.ENERGY += 1 if self.generated_material == 'wishtorio:energy' else 0
                self.GAME.RESOURCES[self.generated_material] += self.number_of_generated_material
                self.GAME.ENERGY -= self.generator_energy_cost
                self.cooldown_start = self.GAME.now
            
class InventoryTile(Tile):
    def __init__(self, game, material, pos):
        self.GAME = game
        self.MATERIAL = material
        self.POS = pos
        self.sprite = self.MATERIAL.sprite_grid_sized
        self.storage_capacity = self.MATERIAL.TILE['storage_capacity']
        self.stored_material = self.MATERIAL.TILE['stored_material']