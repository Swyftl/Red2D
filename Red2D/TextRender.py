import pygame

class Text:

    def __init__(self, text, screen, x, y):
        self.font = pygame.font.SysFont('Arial', 30)
        self.text_surface = self.font.render(text, False, (0, 0, 0))
        self.screen = screen

    def render(self):
        self.screen.blit(self.text_surface, (0, 0))