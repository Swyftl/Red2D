import Red2D
import pygame.sprite

class Sprite(pygame.sprite.Sprite):

    def __init__(self, x, y, width, height, color):
        self.width = width
        self.height = height
        self.color = color
        self.x = x
        self.y = y

        super().__init__()

        self.image = pygame.Surface((width, height))
        self.image.fill(self.color)
        self.image.set_colorkey(self.color)

    def render(self):
        sprite = pygame.draw.rect(self.image, self.color, pygame.Rect(self.x, self.y, self.width, self.height))
        return sprite