import pygame

# Each shape will be sent to this
# An event will be called from this script to render everything that has been passed in


class Render:
    def __init__(self, Graphics):
        self.shapes = []
        self.Graphics = Graphics

    def add_shape(self, shape):
        self.shapes.append(shape)

    def render(self):
        for shape in self.shapes:
            # Assuming each shape is an object with a render method or similar
            shape.render()
