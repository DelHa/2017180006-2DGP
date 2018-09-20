from pico2d import *

#윈도우 생성전에 만든다.
KPU_WIDTH, KPU_HEIGHT = 1280, 1024


def handle_events():
    global running
    global click_x, click_y
    global mouse_x, mouse_y
    events = get_events()
    for event in get_events():
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            mouse_x, mouse_y = event.x, KPU_HEIGHT - 1 - event.y
        elif event.type == SDL_MOUSEBUTTONDOWN:
            click_x, click_y = mouse_x - 20, mouse_y + 21
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

def move_character():
    global char_x, char_y
    global move_x, move_y
    global look
    global frame
    frame = 0
    handle_events()

    if click_x > char_x:
        look = 1
    elif click_x < char_x:
        look = 0

    move_x = (click_x - char_x)
    move_y = (click_y - char_y)

    for i in range(0, 100):
        clear_canvas()
        kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        character.clip_draw(frame * 100, 100 * look, 100, 100, char_x, char_y)
        hand.draw_now(mouse_x, mouse_y)
        handle_events()
        update_canvas()
        frame = (frame + 1) % 8
        char_y += move_y // 100
        char_x += move_x // 100


open_canvas(KPU_WIDTH, KPU_HEIGHT)

kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
hand = load_image('hand_arrow.png')

click_x, click_y = KPU_WIDTH // 2, KPU_HEIGHT // 2
mouse_x, mouse_y = KPU_WIDTH // 2, KPU_HEIGHT // 2
char_x, char_y = KPU_WIDTH // 2, KPU_HEIGHT // 2
move_x, move_y = KPU_WIDTH // 2, KPU_HEIGHT // 2

look = 1
frame = 0
#running => roof controll variable
running = True
hide_cursor()

while running:
    handle_events()
    move_character()

close_canvas()




