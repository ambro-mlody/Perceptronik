import random
import sys
import pygame as py
import button
import data


py.init()
size = (390, 550)
window = py.display.set_mode(size)
py.display.set_caption("Perceptronik")


def number_clicked(self):
    d = data.data[int(self.text)]
    i = 0
    for p in canvas:
        p.clicked = d[i]
        if d[i] == 0:
            p.bg_color = "white"
        else:
            p.bg_color = "red"
        i += 1


font = 34
button_size = (40, 40)
menu = []
x = 6
y = 461
diff = 43
position = (x, y)
for i in range(5):
    menu.append(button.Button(position, button_size, str(i), font, bg_color="blue", on_click=number_clicked))
    position = (position[0] + diff, position[1])

position = (x, y + diff)
for i in range(5, 10):
    menu.append(button.Button(position, button_size, str(i), font, bg_color="blue", on_click=number_clicked))
    position = (position[0] + diff, position[1])


def rand_clicked(self):
    for pixel in canvas:
        prob = 0.025
        rand = random.random()
        if rand < prob:
            if pixel.clicked == 0:
                pixel.clicked = 1
                pixel.bg_color = "red"
            else:
                pixel.clicked = 0
                pixel.bg_color = "white"


font = 20
button_size = (50, 40)
diff_x = 53
menu.append(button.Button(position, button_size, "rand", font, color="black", bg_color="gray", on_click=rand_clicked))
position = (position[0] + diff_x, position[1])


def clean_clicked(self):
    for pixel in canvas:
        if pixel.clicked == 1:
            pixel.bg_color = "white"
            pixel.clicked = 0


menu.append(button.Button(position, button_size, "clean", font, color="black", bg_color="gray", on_click=clean_clicked))
position = (position[0], position[1] - diff)
menu.append(button.Button(position, button_size, "check", font, color="black", bg_color="gray"))
position = (position[0] - diff_x, position[1])
menu.append(button.Button(position, button_size, "learn", font, color="black", bg_color="gray"))

position = (position[0] + 2 * diff_x, position[1])
button_size = (size[0] - position[0] - x, size[1] - position[1] - x)
font = 60
output_screen = button.Button(position, button_size, "", font, color="black", bg_color="green")


def pixel_clicked(self):
    if self.clicked == 0:
        self.bg_color = "red"
        self.clicked = 1
    else:
        self.bg_color = "white"
        self.clicked = 0


button_size = (60, 60)
x = 40
position = (x, 15)
diff = 62
canvas = []
for i in range(1, 36):
    canvas.append(button.Button(position, button_size, "", font, bg_color="white", on_click=pixel_clicked))
    position = (position[0] + diff, position[1])
    if i % 5 == 0:
        position = (x, position[1] + diff)

while True:
    window.fill((0, 0, 0))
    for ev in py.event.get():
        if ev.type == py.QUIT:
            py.quit()
            sys.exit(0)
        if py.mouse.get_pressed()[0]:
            for b in menu:
                b.click()
            for p in canvas:
                p.click()

    for p in canvas:
        p.draw(window)

    for b in menu:
        b.draw(window)
    output_screen.draw(window)
    py.display.update()
