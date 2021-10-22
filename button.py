import pygame as py

class Button(object):

    def __init__(self, size, position, text, color, bg_color):
        self.size = size
        self.position = position
        self.text = text
        self.color = color
        self.bg_color = color

    def draw(self, window):
