import keyboard
import mouse
import pygame

class Input:

    def __init__(self, key):
        self.key = key
        self.was_key_released = True

    def is_key_down(self):
        if keyboard.is_pressed(self.key):
            return True
        else:
            return False

    def is_just_pressed(self):
        if keyboard.is_pressed(self.key) and self.was_key_released:
            self.was_key_released = False
            return True
        elif not keyboard.is_pressed(self.key) and not self.was_key_released:
            self.was_key_released = True
            return False
        
class Axis:

    def __init__(self, negative: Input, positive: Input):
        self.negative = negative
        self.positive = positive
    
    def get(self):
        direction = 0
        if self.negative.is_key_down():
            direction -= 1
        elif self.positive.is_key_down():
            direction += 1
        else:
            direction = 0
        return direction

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