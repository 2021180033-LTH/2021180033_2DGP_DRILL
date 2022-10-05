from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024


def handle_events():
    # fill here
    global running
    global dirx
    global diry
    global h
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dirx += 1
                h = 1
            elif event.key == SDLK_LEFT:
                dirx -= 1
                h = 2
            elif event.key == SDLK_UP:
                diry -= 1
            elif event.key == SDLK_DOWN:
                diry += 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dirx -= 1
                if(h > 3):
                    h -= 2
            elif event.key == SDLK_LEFT:
                dirx += 1
                h = 3
            elif event.key == SDLK_UP:
                diry += 1
            elif event.key == SDLK_DOWN:
                diry -= 1
    pass


open_canvas(TUK_WIDTH, TUK_HEIGHT)
TUK = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')

running = True
x = TUK_WIDTH // 2
y = TUK_HEIGHT // 2
frame = 0
dirx = 0
diry = 0
h = 3


while running and 0 < x < 800 and 0 < y < 1024:
    clear_canvas()
    TUK.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    character.clip_draw(frame * 100, 100 * h, 100, 100, x, y)
    update_canvas()

    handle_events()
    frame = (frame + 1) % 8
    x += dirx * 5
    y -= diry * 5
    delay(0.01)

close_canvas()

