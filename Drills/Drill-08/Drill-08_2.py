import turtle
import random
from pico2d import *
#캐릭터 업로드
os.chdir("C:\\git\\2017180006-2DGP\\Drills\\Drill-08")

KPU_WIDTH, KPU_HEIGHT = 1280, 1024
open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')

def stop():
    turtle.bye()


look = 1
frame = 0
running = True
again_click = False
character = load_image('animation_sheet.png')
save_frame1 = 0
save_frame2 = 0
save_frame3 = 0


def draw_big_point(p):
    turtle.goto(p)
    turtle.color(0.8, 0.9, 0)
    turtle.dot(15)
    turtle.write('     '+str(p))


def draw_point(p):
    global look
    global frame
    global again_click
    global x
    global y

    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)

    character.clip_draw(frame * 100, 100 * look, 100, 100, x, y)
    update_canvas()
    frame = (frame + 1) % 8



def draw_curve_3_points(p1, p2, p3, p4):
    global look
    global frame
    global again_click
    global x
    global y
    global save_frame1
    global save_frame2
    global save_frame3

    # draw p1-p2
    character.clip_draw(save_frame1 * 100, 100 * look, 100, 100, p1[0], p1[1])

    for i in range(0, 50, 1):
        t = i / 100
        x = (2 * t ** 2 - 3 * t + 1) * p1[0] + (-4 * t ** 2 + 4 * t) * p2[0] + (2 * t ** 2 - t) * p3[0]
        y = (2 * t ** 2 - 3 * t + 1) * p1[1] + (-4 * t ** 2 + 4 * t) * p2[1] + (2 * t ** 2 - t) * p3[1]

        if(i <49):
            clear_canvas()

        kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)

        if p1[0] > p2[0]:
            look = 0
        else:
            look = 1

        character.clip_draw(frame * 100, 100 * look, 100, 100, x, y)
        update_canvas()
        if i >= 50:
            character.clip_draw(save_frame1 * 100, 100 * look, 100, 100, p1[0], p1[1])
            update_canvas()

        frame = (frame + 1) % 8
        save_frame1 = frame

    # draw p2-p3
    for i in range(0, 100, 1):
        t = i / 100
        x = ((-t ** 3 + 2 * t ** 2 - t) * p1[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p2[0] + (
                    -3 * t ** 3 + 4 * t ** 2 + t) * p3[0] + (t ** 3 - t ** 2) * p4[0]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * p1[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p2[1] + (
                    -3 * t ** 3 + 4 * t ** 2 + t) * p3[1] + (t ** 3 - t ** 2) * p4[1]) / 2
        clear_canvas()

        kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)

        if p2[0] > p3[0]:
            look = 0
        else:
            look = 1

        character.clip_draw(frame * 100, 100 * look, 100, 100, x, y)
        if i >= 50:
            character.clip_draw(save_frame2 * 100, 100 * look, 100, 100, p2[0], p2[1])
            update_canvas()
        else:
            update_canvas()

        frame = (frame + 1) % 8
        save_frame2 = frame

    # draw p3-p4
    for i in range(0, 100, 1):
        t = i / 100
        x = ((-t ** 3 + 2 * t ** 2 - t) * p2[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p3[0] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * p4[0] + (t ** 3 - t ** 2) * p1[0]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * p2[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p3[1] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * p4[1] + (t ** 3 - t ** 2) * p1[1]) / 2

        clear_canvas()
        kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)

        if p3[0] > p4[0]:
            look = 0
        else:
            look = 1

        character.clip_draw(frame * 100, 100 * look, 100, 100, x, y)
        if i >= 50:
            character.clip_draw(save_frame3 * 100, 100 * look, 100, 100, p3[0], p3[1])

        update_canvas()

        frame = (frame + 1) % 8
        save_frame3 = frame


#prepare_turtle_canvas()

size = 20
points = [(random.randint(300 , KPU_WIDTH - 100), random.randint(300,KPU_HEIGHT - 100)) for i in range(size)]

n = 3

while True:
    draw_curve_3_points(points[n-3],points[n-2],points[n-1], points[n])
    n = (n+3) % size

close_canvas()
turtle.done()