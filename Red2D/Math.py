import pygame
import math

# Math functions that could be useful

def rect(left, top, width, height):
    return pygame.Rect(left, top, width, height)

def get_angle_between(objectone, objecttwo):
    return math.atan2(objecttwo.position.y - objectone.position.y, objecttwo.position.x - objectone.position.x)