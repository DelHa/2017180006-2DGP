from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024

def handle_events():
    global mx, my
    global c_x, c_y
    global running
    global mouse_click_on
    events = get_events()
    for event in get_events():
        if event.type == SDL_MOUSEMOTION:
            mx, my = event.x, KPU_HEIGHT - 1 - event.y
            mouse_click_on = False
        elif event.type == SDL_MOUSEBUTTONDOWN:
            c_x, c_y = mx - 5, my - 5
            mouse_click_on = True
        elif event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


def move_charater():
    global c_x, c_y
    global old_x, old_y
    global move_x, move_y
    global mouse_click_on
    if mouse_click_on == True:
        move_x = old_x - 10

open_canvas(KPU_WIDTH, KPU_HEIGHT)

kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
hand = load_image('hand_arrow.png')

running = True
mouse_click_on = False
old_x, old_y = KPU_WIDTH // 2, KPU_HEIGHT // 2
c_x, c_y = KPU_WIDTH // 2, KPU_HEIGHT // 2
mx, my = KPU_WIDTH // 2, KPU_HEIGHT // 2
move_x, move_y = KPU_WIDTH // 2, KPU_HEIGHT // 2


frame = 0
hide_cursor()

while running:
    clear_canvas()

    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    hand.draw(mx, my)

    character.clip_draw(frame * 100, 100 * 1, 100, 100, move_x, move_y)
    update_canvas()
    frame = (frame + 1) % 8
    delay(0.01)
    move_charater()
    handle_events()

close_canvas()




