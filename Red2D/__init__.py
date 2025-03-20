import pygame.time
import os

import Red2D.Graphics
import Red2D.Math
import Red2D.Render
import Red2D.Player
import Red2D.Draw
import Red2D.TextRender
import Red2D.Sprite
import Red2D.Logging
import Red2D.UserInterface
import Red2D.Input
import Red2D.check_updates
import Red2D.Scene

pygame.font.init()

class Engine:

    def __init__(self, window_x, window_y):

        Red2D.check_updates.check_for_updates()

        self.window_x = window_x
        self.window_y = window_y

        self.Clock = pygame.time.Clock()
        self.Screen = pygame.display.set_mode((self.window_x, self.window_y))

        self.running = True
        self.framerate = 60

        self.delta = 1/self.framerate

        self.total_frames_rendered = 0

        self.Graphics = Red2D.Graphics.Graphics(self.Screen)
        self.Render = Red2D.Render.Render(self.Graphics)
        self.Logging = Red2D.Logging.Logging(True)
        self.Events = Red2D.Input.Event()
        self.SceneManager = Red2D.Scene.Scene_Manager(self)

        self.Logging.log("Initialized logging", level="Log")

        self.background_color = "white"

        ProgramIcon = pygame.image.load('./Red2D/Red2D_Icon.ico')
        pygame.display.set_icon(ProgramIcon)
        pygame.display.set_caption('Red2D Engine')

        self.CheckFilesExist()

    def CheckFilesExist(self):
        if not os.path.exists('./_internal'):
            self.Logging.log("Internal Folder Not Found, Making Now")
            os.mkdir('./_internal')
        if not os.path.exists('./_internal/Assets'):
            self.Logging.log("Internal Assets Folder Not Found, Making Now")
            os.mkdir('./_internal/Assets')
        if not os.path.exists('./_internal/Assets/Images'):
            self.Logging.log("Internal Images Folder Not Found, Making Now")
            os.mkdir('./_internal/Assets/Images')
        if not os.path.exists('./_internal/Assets/Sounds'):
            self.Logging.log("Internal Sounds Folder Not Found, Making Now")
            os.mkdir('./_internal/Assets/Sounds')

    def set_title(self, text):
        pygame.display.set_caption(text)
    
    def set_icon(self, icon_location):
        ProgramIcon = pygame.image.load(icon_location)
        pygame.display.set_icon(ProgramIcon)

    def render_frame(self):
        # Start of frame rendering
        try:
            self.Screen.fill(self.background_color)
        except ValueError:
            print(str(self.background_color)+" is not a valid colour, defaulting to white")
            self.Screen.fill("White")
        
        self.Events.CheckEvents()
        if self.Events.isQuit:
            self.running = False
            pygame.quit()
        if self.Events.isLeftMouseDown:
            Red2D.UserInterface.isMousePressed = True
        else:
            Red2D.UserInterface.isMousePressed = False

        # rendering items
        self.Render.render()

        # End of frame rendering
        pygame.display.flip()
        self.Clock.tick(self.framerate)
        self.delta = 1/self.framerate
        self.total_frames_rendered += 1

    def set_title(self, title):
        pygame.display.set_caption(str(title))

    def set_framerate(self, framerate):
        self.framerate = int(framerate)
    
    # All of the stuff for passing the rendered items to the renderer
    def new_player(self, initial_x, initial_y, x_size, y_size, **kwargs):
        if "zindex" in kwargs:
            zindex = kwargs.get("zindex")
        else:
            zindex = 0
        player = Red2D.Player.Player(initial_x, initial_y, x_size, y_size, self.Screen, zindex)
        return player

    def new_Rectangle(self, x, y, width, height, **kwargs):
        if "zindex" in kwargs:
            zindex = kwargs.get("zindex")
        else:
            zindex = 0
        new_rectangle = Red2D.Draw.Rectangle(x, y, width, height, self.Render, self.Graphics, zindex)
        return new_rectangle

    def new_Text(self, text, x, y, **kwargs):
        if "zindex" in kwargs:
            zindex = kwargs.get("zindex")
        else:
            zindex = 0
        text_render = Red2D.TextRender.Text(text, self.Screen, x, y, zindex,kwargs)
        return text_render

    def new_Sprite(self, x, y, width, height, color, **kwargs):
        if "zindex" in kwargs:
            zindex = kwargs.get("zindex")
        else:
            zindex = 0
        new_sprite = Red2D.Sprite.Sprite(x, y, width, height, color, zindex)
        return new_sprite

    def new_Button(self, x, y, width, height, text, **kwargs):
        if "zindex" in kwargs:
            zindex = kwargs.get("zindex")
        else:
            zindex = 0
        new_button = Red2D.UserInterface.Button(x, y, width, height, text, self.Screen, zindex)
        return new_button
    
    def new_PhysicsObject(self, x, y, width, height, **kwargs):
        if "zindex" in kwargs:
            zindex = kwargs.get("zindex")
        else:
            zindex = 0
        new_physics_object = Red2D.PhysicsObject.PhysicsObject(x, y, width, height, zindex)
        return new_physics_object
    
    def get_window_size(self):
        return self.window_x, self.window_y
    
    def get_window_x(self):
        return self.window_x
    
    def get_window_y(self):
        return self.window_y
    
    def new_scene(self):
        return self.SceneManager.new_scene()