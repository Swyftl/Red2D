import pygame
import Red2D

class PhysicsObject:

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.velocity = [0, 0]
        self.acceleration = [0, 0]
        self.zindex = 0
    
    def update(self):
        PhysicsObject = pygame.draw.rect(Red2D.window, (255, 255, 255), pygame.Rect(self.x, self.y, self.width, self.height))