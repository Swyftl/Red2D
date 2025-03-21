import keyboard
import mouse
import pygame
import os
import json

class InputManager:

    def __init__(self):
        self.input_file = 'input.R2D' if os.path.isfile('input.R2D') else None
        self.inputs = self.load_inputs()

    def load_inputs(self):
        if self.input_file:
            try:
                with open(self.input_file, 'r') as file:
                    return json.load(file)
            except (FileNotFoundError, json.JSONDecodeError):
                print("Error loading input.R2D")
                return {}
        return {}

    def get_key(self, name):
        for input_data in self.inputs:
            if input_data['name'] == name:
                return input_data['keys']
        return []  # Return empty list if not found

    def is_button_down(self, name):
        keys = self.get_key(name)
        return any(keyboard.is_pressed(key) for key in keys)

class Event:
        
    def __init__(self):
        self.isLeftMouseDown = False
        self.isRightMouseDown = False
        self.isQuit = False
    
    def CheckEvents(self):
        for event in pygame.event.get():
            # Checking if the close button is pressed
            if event.type == pygame.QUIT:
                self.isQuit = True
            else:
                self.isQuit
            
            # Checking if the MouseButtonLeft is pressed
            if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
                self.isLeftMouseDown = True
            else:
                self.isLeftMouseDown = False

            # Checking if the MouseButtonRight is Pressed
            if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[1]:
                self.isRightMouseDown = True
            else:
                self.isRightMouseDown = False

def get_mouse_position():
    return pygame.mouse.get_pos()