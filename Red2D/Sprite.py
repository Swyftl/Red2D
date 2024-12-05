import Red2D
import pygame.sprite

class Sprite:

    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color

        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(self.color)
        self.image.set_colorkey(color)

    def render(self):
        sprite = pygame.draw.rect(self.image, self.color, pygame.Rect(0, 0, self.width, self.height))
        return sprite