import pygame
import pygame.freetype
from pygame import gfxdraw
import random
import os
from states.state import State
#from text_utils import draw_centered_text, draw_smooth_circle

#self.assets_dir = os.path.join("assets")
#purple_fish_img = pygame.image.load("assets/purple_fish_e1.png").convert_alpha()

class Fish:
    def __init__(self, loc, img_l, img_r, facing_left=True, dx=0, dy=0):
        self.loc = loc
        self.x = self.loc[0]
        self.y = self.loc[1]
        self.left_sprite = img_l
        self.right_sprite = img_r
        self.facing_left = facing_left
        self.dx = dx
        self.dy = dy

    def display(self, surface):
        if self.facing_left:
            surface.blit(self.left_sprite, self.loc)
        else:
            surface.blit(self.right_sprite, self.loc)

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d or pygame.K_RIGHT:
                self.dx = 4
                self.dy = -2
                if self.facing_left:
                    self.facing_left = False
            elif event.key == pygame.K_a or pygame.K_LEFT:
                self.dx = -4
                self.dy = -2
                if not self.facing_left:
                    self.facing_left = True

    def update(self, delta_time):
        self.x += self.dx
        self.y += self.dy
        self.loc = (self.x, self.y)

class ScreenOne(State):
    def __init__(self, game):
        State.__init__(self, game)
        self.assets_dir = self.game.assets_dir
        self.bg = pygame.image.load(os.path.join(self.assets_dir, "background1A.png"))
        self.surface = self.game.game_canvas
        self.purple_fish = Fish((52, 98), pygame.image.load(os.path.join(self.assets_dir, "purple_fish_LEFT.png")), pygame.image.load(os.path.join(self.assets_dir, "purple_fish_RIGHT.png")), facing_left=False)

    def update(self, delta_time):
        self.purple_fish.update(delta_time)

    def render(self, surface):
        surface.blit(self.bg, (0,0))
        self.purple_fish.display(surface)

    def handle_event(self, event):
        self.purple_fish.handle_event(event)



        
