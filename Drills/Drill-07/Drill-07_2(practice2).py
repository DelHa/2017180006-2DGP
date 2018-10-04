from pico2d import *
import turtle
import random

#윈도우 생성전에 만든다.
KPU_WIDTH, KPU_HEIGHT = 1280, 1024
os.chdir("C:\\git\\2017180006-2DGP\\Drills\\Drill-07")

x = 0
y = 0

start_x, start_y = 0,0
move_x, move_y = 0,0
end_x, end_y = 0,0

def draw_curve_4_points(end, move,start):
    global frame
    global x
    global y
    global count
    #draw_big_point(p1)
    #draw_big_point(p2)
    #draw_big_point(p3)
    #draw_big_point(p4)

    # draw p1-p2
    for i in range(0, 50, 2):
        t = i / 100
        x = (2*t**2-3*t+1)*end[0]+(-4*t**2+4*t)*move[0]+(2*t**2-t)*start[0]
        y = (2*t**2-3*t+1)*end[1]+(-4*t**2+4*t)*move[1]+(2*t**2-t)*start[1]
        clear_canvas()
        kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        character.clip_draw(frame * 100, 100 * look, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        #draw_point((x, y))
    #draw_point(p2)

    #draw_point(p1)

def move_character(end, move,start):
    global look
    global frame
    global again_click
    global x
    global y

    frame = 0
    #핸들이벤트를 받는다.

    for i in range(0, 100):
        draw_curve_4_points(end, move,start)
        clear_canvas()
        kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        character.clip_draw(frame * 100, 100 * look, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8


open_canvas(KPU_WIDTH, KPU_HEIGHT)

kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')

look = 1
frame = 0
#running => roof controll variable
running = True
again_click = False

start = 0,0
move = 0.0
end = 0,0

size = 20
start = [(random.randint(100, KPU_WIDTH - 200), random.randint(100, KPU_HEIGHT - 200)) for i in range(size)]

n = 1
while True:
    #핸들 이벤트를 받는다.
    #캐릭터를 그린다.

    move_character(start[n-1], start[n], start[n+1])
    n = (n + 1)% size

close_canvas()




