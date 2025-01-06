import pygame
import Red2D.Graphics
import Red2D.Render

class Player:

    def __init__(self, initial_x, initial_y, x_size, y_size, screen, zindex):
        self.position = pygame.Vector2(initial_x, initial_y)
        self.size = pygame.Vector2(x_size, y_size)

        self.visible = True
        self.graphics = Red2D.Graphics.Graphics(screen)
        self.color = "Red"
        self.zindex = zindex
    
    def move(self, x_increment, y_increment):
        self.position.x += x_increment.get()
        self.position.y += y_increment.get()
    
    def set_position(self, pos_x, pos_y):
        self.position.x = pos_x
        self.position.y = pos_y

    def render(self):
        self.graphics.render("red", self.position.x, self.position.y, self.size.x, self.size.y, self.zindex)

