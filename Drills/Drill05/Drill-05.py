from pico2d import *
os.chdir("C:\\git_2DGP\\2017180006-2DGP\\Drills\\Drill05")
os.getcwd()

open_canvas()

grass = load_image('grass.png')
character = load_image('animation_sheet.png')

#지정된 경로좌표
pos1_x, pos1_y = 203, 535
pos2_x, pos2_y = 132, 243
pos3_x, pos3_y = 535, 470
pos4_x, pos4_y = 477, 203
pos5_x, pos5_y = 715, 136
pos6_x, pos6_y = 316, 225
pos7_x, pos7_y = 510, 92
pos8_x, pos8_y = 692, 518
pos9_x, pos9_y = 682, 336
pos10_x, pos10_y = 712, 349


# 0918메모
# 함수를 사용하면 코드를 읽기가 쉬워진다.
# 함수 이름은 '항상 동사'로 시작되어야한다.
# 함수를 적절하게 사용하면 코더의 의도가 보인다.
# 800//2 -> 화면의 중심으로 이동시키는것을 바로 알아볼 수 있다.
# 코드가 실행이 가능할때 commit 한다.


def move_left_chart():
    x = 0
    frame = 0

    while x < 800:
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 100, 100, 100, x, 90)
        update_canvas()
        frame = (frame + 1) % 8
        x += 10
        delay(0.05)
        get_events()


def move_right_chart():
    pass

while (True):
    move_left_chart()
    #move_right_chart()


close_canvas()
