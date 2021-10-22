import sys
import pygame as py

py.init()
size = (800, 600)
window = py.display.set_mode(size)
py.display.set_caption("Perceptronik")

while True:
    window.fill((0, 0, 0))
    for ev in py.event.get():
        if ev.type == py.QUIT:
            py.quit()
            sys.exit(0)