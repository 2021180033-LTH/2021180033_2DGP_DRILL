from pico2d import *
import random
import server
import game_world

class Ball:
    image = None
    def __init__(self):
        if Ball.image is None:
            Ball.image = load_image('ball21x21.png')
        self.x = random.randint(0, get_canvas_width())
        self.y = random.randint(0, get_canvas_height())

    def update(self):
        pass

    def draw(self):
        self.image.clip_draw(0, 0, 23, 23, self.x, self.y)
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 11.5, self.y - 11.5, self.x + 11.5, self.y + 11.5

    def handle_collision(self, other, group):
        if group == 'boy:ball':
            game_world.remove_collision_object(self)
            game_world.remove_object(self)