import turtle
import random
from pico2d import *
#캐릭터 업로드
os.chdir("C:\\git\\2017180006-2DGP\\Drills\\Drill-07")

KPU_WIDTH, KPU_HEIGHT = 1280, 1024
open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')

def stop():
    turtle.bye()


def draw_point(p):
    turtle.goto(p)
    #turtle.dot(5, random.random(), random.random(), random.random())


def draw_line_basic(p1, p2):
    #draw_big_point(p1)
    #draw_big_point(p2)

    x1, y1 = p1[0], p2[1]
    x2, y2 = p1[0], p2[1]

    a=(y2 - y1)/ (x2 - x1)
    b= y1 - x1 * a

    for x in range (x1, x2+1,10):
        y=a*x + b
        draw_point((x,y))

    #draw_point(p2)


look = 1
frame = 0
#running => roof controll variable
running = True
again_click = False
character = load_image('animation_sheet.png')

def draw_line(p1, p2):
    global look
    global frame
    global again_click
    global x
    global y

    #draw_big_point(p1)
    #draw_big_point(p2)

    if p1[0] > p2[0]:
        look = 0
    else:
        look = 1

    for i in range(0,100 + 1, 1):
        t = i / 100
        x = (1-t) * p1[0] + t*p2[0]
        y = (1-t) * p1[1] + t*p2[1]
        clear_canvas()
        kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        character.clip_draw(frame * 100, 100 * look, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8

    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    character.clip_draw(frame * 100, 100 * look, 100, 100, x, y)
    update_canvas()
    frame = (frame + 1) % 8


size = 20
points = [(random.randint(100 , KPU_WIDTH - 100), random.randint(100,KPU_HEIGHT - 100)) for i in range(size)]

n = 1

while True:
    draw_line(points[n-1],points[n])
    n = (n+1) % size

turtle.done()
close_canvas()
