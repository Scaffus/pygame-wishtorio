import pygame
from colors import Colors
from tile import Generator
import utilities as utils

class Player(pygame.sprite.Sprite):
    def __init__(self, game) -> None:
        self.GAME = game
        self.surface = pygame.surface.Surface((self.GAME.GRID_SIZE, self.GAME.GRID_SIZE))
        self.surface.fill(Colors.player)
        self.body = True

        self.left_p = False
        self.right_p = False
        self.up_p = False
        self.down_p = False

        self.pos = (0, 0)

        self.velx = 0
        self.vely = 0

    def draw(self):
        if self.body: self.GAME.DISPLAY.blit(self.surface, self.pos)

    def update(self):
        mpos = self.GAME.HOVERED_TILE_POS
        
        if pygame.mouse.get_pressed()[0] == 1:
            if mpos not in self.GAME.MAP.tiles:
                if self.GAME.HUD.HOTBAR.slots[self.GAME.HUD.HOTBAR.selected_slot].type == 1:
                    self.GAME.MAP.tiles[mpos] = Generator(self.GAME, mpos) 
        if pygame.mouse.get_pressed()[2] == 1:
            if mpos in self.GAME.MAP.tiles:
                self.GAME.MAP.tiles.pop(mpos)
        
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

        self.pos = (self.pos[0] + self.velx * self.GAME.GRID_SIZE,
                    self.pos[1] + self.vely * self.GAME.GRID_SIZE)

        self.reset_keys()
