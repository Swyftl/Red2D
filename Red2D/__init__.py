import pygame.time

import Red2D.Graphics
import Red2D.Math
import Red2D.Render
import Red2D.Player


class Engine:

    def __init__(self, window_x, window_y):
        self.window_x = window_x
        self.window_y = window_y

        self.Clock = pygame.time.Clock()
        self.Screen = pygame.display.set_mode((self.window_x, self.window_y))

        self.running = True
        self.framerate = 60

        self.rendered_frames = 0

        self.Graphics = Graphics.Graphics(self.Screen)
        self.Render = Render.Render(Graphics)

    def tick(self, background_color):
        for event in pygame.event.get():
            if event == pygame.QUIT:
                self.running = False
        try:
            self.Screen.fill(background_color)
        except ValueError:
            print(str(background_color)+" is not a valid colour, defaulting to white")
            self.Screen.fill("White")

    def render_frame(self):
        pygame.display.flip()
        self.Clock.tick(self.framerate)
        self.rendered_frames += 1

    def set_title(self, title):
        pygame.display.set_caption(str(title))

    def set_framerate(self, framerate):
        self.framerate = int(framerate)

    def new_player(self, initial_x, initial_y, x_size, y_size):
        player = Red2D.Player.Player(initial_x, initial_y, x_size, y_size, self.Screen)
        self.Render.add_shape(player)
        return player
