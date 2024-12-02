import pygame

class Graphics:

    def __init__(self, screen):
        self.Screen = screen

    def render_rect(self, color, rect):
        pygame.draw.rect(self.Screen, color, rect)