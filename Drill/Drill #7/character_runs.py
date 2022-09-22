from pico2d import *
open_canvas()
grass = load_image('grass.png')
character = load_image('char_sheet_2.png')

x = 0
#여기를 채우세요.
frame = 0
while(x < 800):
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(frame * 210, 0, 200, 120, x, 100)
    update_canvas()
    frame = (frame + 1) % 8
    x += 5
    delay(0.05)
    get_events()

close_canvas()

