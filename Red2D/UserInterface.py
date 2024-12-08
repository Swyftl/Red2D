import mouse
import pygame.draw

import Red2D


class Button:

    def __init__(self, x, y, width, height, text, screen, **kwargs):
        self.ButtonReleased = True
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.text = text

        self.screen = screen

        if "color" in kwargs:
            self.color = kwargs.get("color")
        else:
            self.color = "Red"

    def render(self):
        pygame.draw.rect(self.screen, self.color,
                         pygame.Rect(self.x - self.width / 2, self.y - self.height / 2, self.width, self.height))

    def mouse_hovering(self):
        mousePos = pygame.mouse.get_pos()
        if (self.x - self.width / 2, self.y - self.width / 2) < mousePos < (
        self.x + self.width / 2, self.y + self.width / 2):
            return True
        else:
            return False

    def button_clicked(self):
        if self.mouse_hovering() and mouse.is_pressed() and self.ButtonReleased:
            print("Clicked Button")
            self.ButtonReleased = False
            return True
        elif self.mouse_hovering() and not mouse.is_pressed() and not self.ButtonReleased:
            self.ButtonReleased = True
            return False
        else:
            return False
