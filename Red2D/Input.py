import keyboard
import mouse

class Input:

    def __init__(self, key):
        self.key = key

    def is_pressed(self):
        if keyboard.is_pressed(self.key):
            return True
        else:
            return False