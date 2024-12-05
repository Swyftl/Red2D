import pygame

class Text:

    def __init__(self, text, screen, x, y, kwargs):
        self.screen = screen
        self.text = text

        if "font" in kwargs:
            self.text_font = kwargs["font"]
        else:
            self.text_font = "Arial"

        if "fontsize" in kwargs:
            self.font_size = kwargs["fontsize"]
        else:
            self.font_size = 22

        self.font_data = pygame.font.SysFont(self.text_font, self.font_size)
        self.text_surface = self.font_data.render(text, False, (0, 0, 0))

    def render(self):
        self.screen.blit(self.text_surface, (0, 0))