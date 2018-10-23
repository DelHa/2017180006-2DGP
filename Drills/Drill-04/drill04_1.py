from pico2d import *

open_canvas()

grass = load_image('grass.png')
back_character = load_image('mid_character.png')
x = 0
frame =0
while(True):
    while (x < 800):
        clear_canvas()
        grass.draw(400, 30)
        back_character.clip_draw(frame * 146 + 10, 10 , 126 , 140 , x, 90 , 180 , 200)
                                #input 위치 x/ y , input w / h , output x  / y ,  output w / h
        update_canvas()
        frame = (frame + 1) % 8
        x += 10
        delay(0.05)
        get_events()

    while (x > 0):
        clear_canvas()
        grass.draw(400, 30)
        back_character.clip_draw(frame * 146 + 10, 10, 126, 140, x, 90)
        update_canvas()
        frame = (frame + 1) % 8
        x -= 10
        # 속도를 증가시키려면 x를 증가시킨다.
        delay(0.05)
        get_events()

close_canvas()

