import pygame
import Red2D.Graphics

class Player:

    def __init__(self, graphics, initial_x, initial_y, x_size, y_size):
        self.position = pygame.Vector2(initial_x, initial_y)
        self.size = pygame.Vector2(x_size, y_size)

        self.visible = True
        self.graphics = graphics
        self.color = "Red"

    def render_player(self):
        if self.visible:
            Red2D.Graphics.Graphics.render_rect(self.graphics, self.color, pygame.Rect(self.position.x, self.position.y, self.size.x, self.size.y))