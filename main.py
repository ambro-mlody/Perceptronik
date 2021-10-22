import sys
import pygame as py
import button

py.init()
size = (800, 600)
window = py.display.set_mode(size)
py.display.set_caption("Perceptronik")
b = button.Button((0, 0), (40, 40), "7", 34, bg_color="blue")

while True:
    window.fill((0, 0, 0))
    for ev in py.event.get():
        if ev.type == py.QUIT:
            py.quit()
            sys.exit(0)

    b.draw(window)
    py.display.update()
