import pygame
from colors import Colors
import utilities as utils
import statistics

class Hud(pygame.sprite.Sprite):
    def __init__(self, game) :
        self.GAME = game
        self.surface = pygame.surface.Surface(self.GAME.SIZE)
        self.surface.set_colorkey(Colors.black)

        self.avrg_fps = 0
        self.fps_list = []

        self.avrg_ms = 0
        self.ms_list = []
        self.ms_color = Colors.green

        self.upd_ = 0
        self.upd_f = 6
        
        self.HOTBAR = Hotbar(self)

    def update(self):
        self.upd_ += 1
        if self.upd_ > self.upd_f:
            if len(self.fps_list) > 45:
                self.fps_list = self.fps_list[-25:-1]
            self.fps_list.append(round(self.GAME.CLOCK.get_fps()))
            self.avrg_fps = round(statistics.mean(self.fps_list))

            if len(self.ms_list) > 45:
                self.ms_list = self.ms_list[-25:-1]
            self.ms_list.append(round(self.GAME.delta_time * 1000))
            self.avrg_ms = statistics.mean(self.ms_list)

            if self.avrg_ms <= 16:
                self.ms_color = Colors.green
            else:
                self.ms_color = Colors.red
            
            self.HOTBAR.update()
            
            self.upd_ = 0


    def draw(self):
        self.surface.fill(Colors.black)
        # ? FPS
        self.surface.blit(utils.font(f" FPS: {self.avrg_fps} ", anti_alias=True, color=Colors.white, background=True), (0, 0))
        # ? Ms per frame
        self.surface.blit(utils.font(f" MS: {'%.1f' % self.avrg_ms} ", anti_alias=True, color=self.ms_color, background=True), (0, 36))
        # ? Energy count
        self.surface.blit(utils.font(f" ENERGY PRODUCTION: {self.GAME.ENERGY} ", anti_alias=True, color=Colors.white, background=True), (0, 72))
        # ? Energy capacity
        self.surface.blit(utils.font(f" ENERGY CAPACITY: {self.GAME.ENERGY_CAPACITY} ", anti_alias=True, color=Colors.white, background=True), (0, 108))
        # ? Update tiles count
        self.surface.blit(utils.font(f" UPDATE TILES: {len(self.GAME.MAP.tiles)} ", anti_alias=True, color=Colors.white, background=True), (0, 140))
        # ? Current chunk
        self.surface.blit(utils.font(f" CHUNK: {self.GAME.PLAYER.CURRENT_CHUNK} ", anti_alias=True, color=Colors.white, background=True), (0, 176))
        
        self.HOTBAR.draw()

        self.GAME.DISPLAY.blit(self.surface, (0, 0))

class Hotbar(pygame.sprite.Sprite):
    def __init__(self, hud) :
        self.HUD = hud
        
        self.slot_number = 9
        self.slot_size = self.HUD.GAME.SLOT_SIZE
        self.slot_surf = pygame.transform.scale(pygame.image.load("./assets/hud/slot.png").convert(), (self.HUD.GAME.SLOT_SIZE, self.HUD.GAME.SLOT_SIZE))
        self.slot_selected_surf = pygame.transform.scale(pygame.image.load("./assets/hud/slot_selected.png").convert(), (self.HUD.GAME.SLOT_SIZE, self.HUD.GAME.SLOT_SIZE))
        self.selected_slot = 0
        self.slots = {}

        self.hotbar = self.create_hotbar_surface()
        self.hotbar_slots_unselected = self.hotbar.copy()
        self.hotbar_items = pygame.surface.Surface(self.hotbar.get_size())
        self.hotbar_items.set_colorkey(Colors.black)
        self.hotbar_content_changed = True
        
        self.hotbar_pos = (self.HUD.GAME.WIDTH / 2 - self.hotbar.get_size()[0] / 2,
            self.HUD.GAME.HEIGHT - self.hotbar.get_size()[1] * 1.2)

    def create_hotbar_surface(self):
        hotbar_size = (self.slot_size * self.slot_number, self.slot_size)
        hotbar = pygame.surface.Surface(hotbar_size)
        for i in range(self.slot_number):
            hotbar.blit(self.slot_surf, (i * self.slot_size, 0))
            self.slots[i] = None
        self.slots[0] = self.HUD.GAME.MATERIALS['wishtorio:reactor']
        self.slots[1] = self.HUD.GAME.MATERIALS['wishtorio:accumulator']

        return hotbar

    def update(self):
        self.hotbar.blit(self.hotbar_slots_unselected, (0, 0))
        self.hotbar.blit(self.slot_selected_surf, (self.selected_slot * self.slot_size, 0))
        
        if self.hotbar_content_changed:
            for slot in range(self.slot_number):
                if self.slots[slot] != None:
                    self.hotbar_items.blit(
                        self.slots[slot].sprite_slot_sized ,
                        (slot * self.HUD.GAME.SLOT_SIZE, 0))
            self.hotbar_content_changed = False
            
        self.hotbar.blit(self.hotbar_items, (0, 0))

    def draw(self):
        self.HUD.GAME.DISPLAY.blit(self.hotbar, self.hotbar_pos)