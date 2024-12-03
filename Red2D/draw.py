import pygame

from Red2D.Graphics import Graphics


class Rectangle:

    def __init__(self, x, y, width, height, render, graphics):
        self.position = pygame.Vector2(x, y)
        self.size = pygame.Vector2(width, height)
        self.render = render
        self.graphics = graphics
        render.add_shape(self)


    def render(self):
        self.graphics.render("red", self.position.x, self.position.y, self.size.x, self.size.y)