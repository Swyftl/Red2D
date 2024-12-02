import keyboard
import mouse

class Input:

    def __init__(self, key):
        self.key = key
        self.was_key_released = True
    def is_pressed(self):
        if keyboard.is_pressed(self.key):
            return True
        else:
            return False

    def just_pressed(self):
        if keyboard.is_pressed(self.key) and self.was_key_released == True:
            self.was_key_released = False
            return True
        elif not keyboard.is_pressed(self.key) and self.was_key_released == False:
            self.was_key_released = True
            return False