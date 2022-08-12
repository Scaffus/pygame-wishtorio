import time

import pygame

from colors import Colors
from cursor import Cursor
from highlight import Highlight
from hud import Hud
from map import Map
from materials import Material, load_tiles
from player import Player


class App:
    pygame.init()

    def __init__(self, grid_size: int, window_size: tuple = (1280, 720)) -> None:
        self.SIZE = self.WIDTH, self.HEIGHT = window_size
        self.WIN = pygame.display.set_mode(window_size)
        self.DISPLAY = pygame.surface.Surface(self.SIZE)
        self.CLOCK = pygame.time.Clock()

        self.RUN = True

        self.GRID_SIZE = grid_size
        self.SLOT_SIZE = 64
        self.PREFIX  = 'wishtorio:'

        self.prev_time = time.time()
        self.delta_time = None
        self.now = 0

        self.MATERIALS = load_tiles(self)

        self.CURSOR = Cursor(self)
        self.HIGHLIGHT = Highlight(self)
        self.HUD = Hud(self)
        self.MAP = Map(self)
        self.PLAYER = Player(self)

        self.RESOURCES = {
            'iron_ore': 0,
            'copper_ore': 0,
        }
        self.ENERGY = 0

        pygame.mouse.set_visible(False)
        pygame.display.set_icon(pygame.image.load("./assets/icon.png").convert_alpha())
        pygame.display.set_caption("Wishtorio")

        self.HOVERED_TILE_POS = None

    def update(self):
        self.PLAYER.update()
        self.HIGHLIGHT.update()
        self.MAP.update()
        self.HUD.update()

    def event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.RUN = False

            if event.type == pygame.KEYDOWN:
                # ? Movements
                if event.key == pygame.K_q:
                    self.PLAYER.left_p = True
                if event.key == pygame.K_d:
                    self.PLAYER.right_p = True
                if event.key == pygame.K_z:
                    self.PLAYER.up_p = True
                if event.key == pygame.K_s:
                    self.PLAYER.down_p = True

                # ? Hotbar slots
                if event.key == pygame.K_1:
                    self.HUD.HOTBAR.selected_slot = 0
                if event.key == pygame.K_2:
                    self.HUD.HOTBAR.selected_slot = 1
                if event.key == pygame.K_3:
                    self.HUD.HOTBAR.selected_slot = 2
                if event.key == pygame.K_4:
                    self.HUD.HOTBAR.selected_slot = 3
                if event.key == pygame.K_5:
                    self.HUD.HOTBAR.selected_slot = 4
                if event.key == pygame.K_6:
                    self.HUD.HOTBAR.selected_slot = 5
                if event.key == pygame.K_7:
                    self.HUD.HOTBAR.selected_slot = 6
                if event.key == pygame.K_8:
                    self.HUD.HOTBAR.selected_slot = 7
                if event.key == pygame.K_9:
                    self.HUD.HOTBAR.selected_slot = 8
                    
                # ? Refresh
                if event.key == pygame.K_r:
                    self.HUD.HOTBAR.hotbar_content_changed = True

                if event.key == pygame.K_ESCAPE:
                    self.RUN = False

    def draw(self):
        self.MAP.draw()
        self.PLAYER.draw()
        self.HIGHLIGHT.draw()
        self.HUD.draw()
        self.CURSOR.draw()

        self.WIN.blit(self.DISPLAY, (0, 0))
        pygame.display.update()

        self.CLOCK.tick()

    def run(self):
        # self.PLAYER.body = False
        while self.RUN:
            self.now = time.time()
            self.delta_time = self.now - self.prev_time
            self.prev_time = self.now

            self.event_handler()
            self.update()
            self.draw()

if __name__ == '__main__':
    app = App(32)
    app.run()
