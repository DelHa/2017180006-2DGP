from pico2d import *

#윈도우 생성전에 만든다.
KPU_WIDTH, KPU_HEIGHT = 1280, 1024


def handle_events():
    pass

def move_character():
    pass



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




