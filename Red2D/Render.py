import pygame

# Each shape will be sent to this
# An event will be called from this script to render everything that has been passed in


class Render:
    def __init__(self, Graphics):
        self.shapes = []
        self.Graphics = Graphics

    def add_shape(self, shape):
        self.shapes.append(shape)

    def sortShapes(self):
        sorted_shapes = sorted(self.shapes, key= lambda obj: obj.zindex)
        return sorted_shapes

    def render(self):
        for shape in self.sortShapes():
            shape.render()
