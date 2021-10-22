import pygame as py


class Button(object):

    def __init__(self, position, size, text, font_size=12, color="white", bg_color="black"):
        self.position = position
        self.text = text
        self.color = color
        self.bg_color = bg_color
        self.font = py.font.SysFont("Arial", font_size)
        self.text_render = self.font.render(text, 1, color)
        x, y, w, h = self.text_render.get_rect()
        self.rect = py.Rect(position, size)
        self.text_pos = (position[0] + (size[0] - w) / 2, position[1] + (size[1] - h) / 2)
        print(self.text_pos)

    def draw(self, window):
        py.draw.rect(window, self.bg_color, self.rect)
        window.blit(self.text_render, self.text_pos)
