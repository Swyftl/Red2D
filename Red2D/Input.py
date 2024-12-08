import keyboard
import mouse

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