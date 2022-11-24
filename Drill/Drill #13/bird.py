from pico2d import *
import random
import game_framework
import game_world

# 1 : 이벤트 정의


# 2 : 상태의 정의

# 3. 상태 변환 구현

PIXEL_PER_METER = (10.0 / 0.01)
RUN_SPEED_KPH = 10.0
RUN_SPEED_MPM = RUN_SPEED_KPH * 1000 / 60
RUN_SPEED_MPS = RUN_SPEED_MPM / 60.0
RUN_SPEED_PPS = RUN_SPEED_MPS * PIXEL_PER_METER

TIME_PER_ACTION = 0.25
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 5


class Bird:

    def __init__(self):
        self.x, self.y = random.randint(0, 1600), random.randint(200, 500)
        self.frame = 0
        self.dir, self.face_dir = 0, 1
        self.image = load_image('bird_animation.png')

        self.font = load_font('ENCR10B.TTF', 16)

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 5

        if self.x < 1600 and self.dir == 1:
            self.x += self.dir * RUN_SPEED_PPS * game_framework.frame_time
        elif self.x >= 1600 and self.dir == 1:
            self.dir = -1
            self.x = clamp(0, self.x, 1600)
        elif self.x > 0 and self.dir == -1:
            self.x += self.dir * RUN_SPEED_PPS * game_framework.frame_time
        elif self.x <= 0 and self.dir == -1:
            self.dir = 1
            self.x = clamp(0, self.x, 1600)

    def draw(self):
        if self.dir == 1:
            self.image.clip_draw(int(self.frame) * 180, 360, 180, 180, self.x, self.y)
        elif self.dir == -1:
            self.image.clip_composite_draw(int(self.frame) * 180, 360, 180, 180, 0, 'v', self.x, self.y, 180, 180)

        self.font.draw(self.x - 60, self.y + 50, f'(Time: {get_time():.2f})', (255, 255, 0))

    def handle_event(self, event):
        pass
