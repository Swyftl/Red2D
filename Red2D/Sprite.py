import Red2D
import pygame.sprite

class Sprite(pygame.sprite.Sprite):

    def __init__(self, x, y, width, height, color, zindex):
        self.width = width
        self.height = height
        self.color = color
        self.x = x
        self.y = y
        self.zindex = zindex

        super().__init__()

        self.image = pygame.Surface((width, height))
        self.image.fill(self.color)
        self.image.set_colorkey(self.color)
    
    def is_on_screen(self, screen_x, screen_y):
        # Get the position of the sprite and make sure it is on the screen
        # This will take into account the size of the sprite
        if self.x < 0 or self.x > Red2D.Engine.get_window_x():
            return False
        else:
            True

    def render(self):
        sprite = pygame.draw.rect(self.image, self.color, pygame.Rect(self.x, self.y, self.width, self.height))
        return sprite