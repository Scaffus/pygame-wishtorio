import pygame
from colors import Colors
from tile import GeneratorTile, InventoryTile
import utilities as utils

class Player(pygame.sprite.Sprite):
    def __init__(self, game) :
        self.GAME = game
        self.sprite = pygame.surface.Surface((self.GAME.GRID_SIZE, self.GAME.GRID_SIZE))
        self.sprite.fill(Colors.player)
        self.body = True

        self.CURRENT_CHUNK = (0, 0)
        self.POS = (0, 0)

        self.left_p = False
        self.right_p = False
        self.up_p = False
        self.down_p = False


        self.velx = 0
        self.vely = 0
        

    def draw(self):
        if self.body: self.GAME.DISPLAY.blit(self.sprite, self.POS)

    def update(self):
        tile_pos = self.GAME.HOVERED_TILE_POS
        
        self.CURRENT_CHUNK = (utils.round_to_multiple(self.POS[0], (self.GAME.CHUNK_SIZE - 1) * self.GAME.GRID_SIZE),
                              utils.round_to_multiple(self.POS[1], (self.GAME.CHUNK_SIZE - 1) * self.GAME.GRID_SIZE))
        
        # if self.CURRENT_CHUNK not in self.GAME.MAP.CHUNKS:
        #     self.GAME.MAP.CHUNKS[self.CURRENT_CHUNK] = self.GAME.MAP.generate_chunk(self.CURRENT_CHUNK)
        
        if pygame.mouse.get_pressed()[0] == 1:
            if tile_pos not in self.GAME.MAP.tiles:
                mat_tile = self.GAME.HUD.HOTBAR.slots[self.GAME.HUD.HOTBAR.selected_slot]
                match mat_tile.TYPE:
                    case 1: 
                        self.GAME.MAP.tiles[tile_pos] = GeneratorTile(self.GAME, mat_tile, tile_pos)
                    case 2:
                        self.GAME.MAP.tiles[tile_pos] = InventoryTile(self.GAME, mat_tile, tile_pos)
                        match mat_tile.NAME:
                            case 'accumulator':
                                self.GAME.ENERGY_CAPACITY += self.GAME.MATERIALS['wishtorio:accumulator'].storage_capacity

        if pygame.mouse.get_pressed()[2] == 1:
            if tile_pos in self.GAME.MAP.tiles:
                self.GAME.MAP.tiles.pop(tile_pos)
        
        if self.body: self.move()
        
    def reset_keys(self):
        self.left_p = False
        self.right_p = False
        self.up_p = False
        self.down_p = False
        
    def move(self):
        self.velx = 0
        self.vely = 0
        
        if self.left_p:
            self.velx -= 1
        if self.right_p:
            self.velx += 1
        if self.up_p:
            self.vely -= 1
        if self.down_p:
            self.vely += 1

        self.POS = (self.POS[0] + self.velx * self.GAME.GRID_SIZE,
                    self.POS[1] + self.vely * self.GAME.GRID_SIZE)

        self.reset_keys()
