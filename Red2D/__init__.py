import pygame.time

import Red2D.Graphics
import Red2D.Math
import Red2D.Render
import Red2D.Player
import Red2D.Draw
import Red2D.TextRender
import Red2D.Sprite
import Red2D.Logging
from Red2D.UserInterface import Button

pygame.font.init()

class Engine:

    def __init__(self, window_x, window_y):
        self.window_x = window_x
        self.window_y = window_y

        self.Clock = pygame.time.Clock()
        self.Screen = pygame.display.set_mode((self.window_x, self.window_y))

        self.running = True
        self.framerate = 60

        self.delta = 1/self.framerate

        self.rendered_frames = 0

        self.Graphics = Graphics.Graphics(self.Screen)
        self.Render = Render.Render(Graphics)
        self.Logging = Red2D.Logging.Logging(True)

        self.Logging.log("Initialized logging", level="Log")

        self.background_color = "white"

    def render_frame(self):
        # Start of frame rendering
        try:
            self.Screen.fill(self.background_color)
        except ValueError:
            print(str(self.background_color)+" is not a valid colour, defaulting to white")
            self.Screen.fill("White")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

        # rendering items
        self.Render.render()

        # End of frame rendering
        pygame.display.flip()
        self.Clock.tick(self.framerate)
        self.delta = 1/self.framerate
        self.rendered_frames += 1

    def set_title(self, title):
        pygame.display.set_caption(str(title))

    def set_framerate(self, framerate):
        self.framerate = int(framerate)

    def new_player(self, initial_x, initial_y, x_size, y_size):
        player = Red2D.Player.Player(initial_x, initial_y, x_size, y_size, self.Screen)
        self.Render.add_shape(player)
        return player

    def new_Rectangle(self, x, y, width, height):
        new_rectangle = Draw.Rectangle(x, y, width, height, self.Render, self.Graphics)
        return new_rectangle

    def new_Text(self, text, x, y, **kwargs):
        text_render = TextRender.Text(text, self.Screen, x, y, kwargs)
        self.Render.add_shape(text_render)
        return text_render

    def new_Sprite(self, x, y, width, height, color):
        new_sprite = Sprite.Sprite(x, y, width, height, color)
        self.Render.add_shape(new_sprite)
        return new_sprite

    def new_Button(self, x, y, width, height, text):
        new_button = Button(x, y, width, height, text, self.Screen)
        self.Render.add_shape(new_button)
        return new_button