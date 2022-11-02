from pico2d import *

# 이벤트 정의
RD, LD, RU, LU, TIMER, AR = range(6)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RD,
    (SDL_KEYDOWN, SDLK_LEFT): LD,
    (SDL_KEYUP, SDLK_RIGHT): RU,
    (SDL_KEYUP, SDLK_LEFT): LU,
    (SDL_KEYDOWN, SDLK_a): AR
}


# 클래스를 이용해서 상태를 만듦
class IDLE:
    @staticmethod
    def enter(self, event):
        print('ENTER IDLE')
        self.dir = 0
        self.timer = 1000

    @staticmethod
    def exit(self):
        print('EXIT IDLE')

    @staticmethod
    def do(self):
        self.frame = (self.frame + 1) % 8
        self.timer -= 1
        if self.timer == 0:  # 시간이 경과 하면
            # self.q.insert(TIMER)  # 객체 지향 프로그래밍에 위배, q에 직접 액세스 하고 있으니...
            self.add_event(TIMER)

    @staticmethod
    def draw(self):
        if self.face_dir == 1:
            self.image.clip_draw(self.frame * 100, 300, 100, 100, self.x, self.y)
        else:
            self.image.clip_draw(self.frame * 100, 200, 100, 100, self.x, self.y)


class RUN:
    def enter(self, event):
        print('ENTER RUN')
        if event == RD:
            self.dir += 1
        elif event == LD:
            self.dir -= 1
        elif event == RU:
            self.dir -= 1
        elif event == LU:
            self.dir += 1

    def exit(self):
        print('EXIT RUN')
        self.face_dir = self.dir  # idle은 run상태의 마지막 방향으로 바라보는 방향 결정

    def do(self):
        self.frame = (self.frame + 1) % 8
        self.x += self.dir * 1.5
        self.x = clamp(0, self.x, 800)

    def draw(self):
        if self.dir == -1:
            self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)
        elif self.dir == 1:
            self.image.clip_draw(self.frame * 100, 100, 100, 100, self.x, self.y)


class SLEEP:
    def enter(self, event):
        print('ENTER SLEEP')
        self.frame = 0

    def exit(self):
        pass

    def do(self):
        self.frame = (self.frame + 1) % 8

    def draw(self):
        if self.face_dir == 1:
            self.image.clip_composite_draw(self.frame * 100, 300, 100, 100, 3.141592 / 2, '', self.x - 25, self.y - 25,
                                           100, 100)
        else:
            self.image.clip_composite_draw(self.frame * 100, 200, 100, 100, -3.141592 / 2, '', self.x + 25, self.y - 25,
                                           100, 100)


class AUTO_RUN:
    def enter(self, event):
        print('ENTER AUTO_RUN')
        self.dir = self.face_dir

    def exit(self):
        self.face_dir = self.dir
        pass

    def do(self):
        self.frame = (self.frame + 1) % 8

        if self.dir == 1 and self.x < 800:
            self.x += self.dir
        elif self.dir == 1 and self.x >= 800:
            self.dir = -1
            self.x = clamp(0, self.x, 800)
        elif self.dir == -1 and self.x > 0:
            self.x += self.dir
        elif self.dir == -1 and self.x <= 0:
            self.dir = 1
            self.x = clamp(0, self.x, 800)

    def draw(self):
        if self.dir == 1:
            self.image.clip_composite_draw(self.frame * 100, 100, 100, 100, 0, '', self.x, self.y + 25, 200, 200)
        elif self.dir == -1:
            self.image.clip_composite_draw(self.frame * 100, 0, 100, 100, 0, '', self.x, self.y + 25, 200, 200)


next_state = {
    IDLE: {RU: RUN, LU: RUN, RD: RUN, LD: RUN, TIMER: SLEEP, AR: AUTO_RUN},
    RUN: {RU: IDLE, LU: IDLE, RD: IDLE, LD: IDLE, AR: AUTO_RUN},
    SLEEP: {RU: RUN, LU: RUN, RD: RUN, LD: RUN},
    AUTO_RUN: {RU: RUN, LU: RUN, RD: RUN, LD: RUN, AR: IDLE}
}


class Boy:
    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        self.dir, self.face_dir = 0, 1
        self.image = load_image('animation_sheet.png')

        self.q = []
        self.cur_state = IDLE
        self.cur_state.enter(self, None)

    def update(self):
        self.cur_state.do(self)

        if self.q:  # 큐에 뭔가 들어 있다면,
            event = self.q.pop()
            self.cur_state.exit(self)
            self.cur_state = next_state[self.cur_state][event]
            self.cur_state.enter(self, event)

        # self.frame = (self.frame + 1) % 8
        # self.x += self.dir * 1.5
        # self.x = clamp(0, self.x, 800)

    def draw(self):
        self.cur_state.draw(self)

        # if self.dir == -1:
        #     self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)
        # elif self.dir == 1:
        #     self.image.clip_draw(self.frame * 100, 100, 100, 100, self.x, self.y)
        # else:
        #     if self.face_dir == 1:
        #         self.image.clip_draw(self.frame * 100, 300, 100, 100, self.x, self.y)
        #     else:
        #         self.image.clip_draw(self.frame * 100, 200, 100, 100, self.x, self.y)

    def add_event(self, event):
        self.q.insert(0, event)

    def handle_event(self, event):  # 소년이 스스로 이벤트를 처리할 수 있게...
        # event 는 키 이벤트... 이 것을 내부 RD등으로 변환
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)  # 변환된 내부 key event를 큐에 추가

        # if event.type == SDL_KEYDOWN:
        #     match event.key:
        #         case pico2d.SDLK_LEFT:
        #             self.dir -= 1
        #         case pico2d.SDLK_RIGHT:
        #             self.dir += 1
        #
        # elif event.type == SDL_KEYUP:
        #     match event.key:
        #         case pico2d.SDLK_LEFT:
        #             self.dir += 1
        #             self.face_dir = -1
        #         case pico2d.SDLK_RIGHT:
        #             self.dir -= 1
        #             self.face_dir = 1
