from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x = 0
y = 0
while (x < 2 * math.pi):
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(400 + x, 300 + y)
    x = x + math.sin(1 / 360 * 2 * math.pi)
    y = y + math.cos(1 / 360 * 2 * math.pi)
    delay(0.01)

close_canvas()
