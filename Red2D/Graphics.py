import pygame

class Graphics:

    def __init__(self, screen):
        self.Screen = screen

    def render_rect(self, color, x, y, x_size, y_size):
        new_rect = pygame.Rect(x-x_size/2, y-y_size/2, x_size, y_size)
        pygame.draw.rect(self.Screen, color, new_rect)