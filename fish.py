import pygame
import pygame.freetype
from pygame import gfxdraw
import random
from states.state import State
from text_utils import draw_centered_text, draw_smooth_circle

self.assets_dir = os.path.join("assets")
purple_fish_img = pygame.image.load("assets/purple_fish_e1.png").convert_alpha()

class Fish:
    def __init__(self, loc, img, orientation, dx=0, dy=0):
        self.loc = loc
        self.x = self.loc[0]
        self.y = self.loc[1]
        self.img = img
        self.orientation = orientation
        self.dx = dx
        self.dy = dy

    def display(self, surface):
        surface.blit(self.img, self.loc)
        
