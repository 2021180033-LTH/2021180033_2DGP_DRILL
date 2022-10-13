import pico2d
from pico2d import *
import game_framework
import play_state

image = None

def enter():
    global image
    global boynum
    image = load_image('add_Delete_boy.png')
    # fill here
    pass


def exit():
    global image
    del image
    # fill here
    pass


def update():
    # fill here
    pass


def draw():
    # fill here
    clear_canvas()
    game_framework.stack[-2].draw_world()
    image.draw(400, 300)
    update_canvas()
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            match event.key:
                case pico2d.SDLK_ESCAPE:
                    game_framework.pop_state()
                case pico2d.SDLK_KP_PLUS:
                    game_framework.stack[-2].boy.numb += 1
                    game_framework.pop_state()
                case pico2d.SDLK_KP_MINUS:
                    if game_framework.stack[-2].boy.numb >= 2:
                        game_framework.stack[-2].boy.numb -= 1
                    game_framework.pop_state()


def test_self():
    import sys
    this_module = sys.modules['__main__']
    pico2d.open_canvas()
    game_framework.run(this_module)
    pico2d.close_canvas()


if __name__ == '__main__':
    test_self()