from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x = 0
y = 0
while (x < 360):
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(400 + 4 * 60 * math.cos(x / 360 * 2 * math.pi), 330 + 4 * 60 * math.sin(y / 360 * 2 * math.pi))
    x = x + 1
    y = y + 1
    delay(0.01)

close_canvas()
