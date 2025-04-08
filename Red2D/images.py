import pygame

class Image:

    def __init__(self, image, x, y, x_size, y_size, zindex):
        self.image = image
        self.x = x
        self.y = y
        self.x_size = x_size
        self.y_size = y_size
        self.zindex = zindex

    def render(self):
        self.loadedImage = pygame.image.load(f'_internal\Assets\{self.image}')
        self.loadedImage = pygame.transform.scale(self.loadedImage, (self.x_size, self.y_size))