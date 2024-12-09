import pygame

from Red2D.Graphics import Graphics


class Rectangle:

    def __init__(self, x, y, width, height, render, graphics, zindex):
        self.position = pygame.Vector2(x, y)
        self.size = pygame.Vector2(width, height)
        self.Render = render
        self.graphics = graphics
        self.visible = True
        self.zindex = zindex
        render.add_shape(self)

    def render(self):
        if self.visible:
            self.graphics.render("red", self.position.x, self.position.y, self.size.x, self.size.y, self.zindex)