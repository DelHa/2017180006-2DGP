from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

# 0918메모
# 함수를 사용하면 코드를 읽기가 쉬워진다.
# 함수 이름은 '항상 동사'로 시작되어야한다.
# 함수를 적절하게 사용하면 코더의 의도가 보인다.
# 800//2 -> 화면의 중심으로 이동시키는것을 바로 알아볼 수 있다.
def move_from_center_to_right():
    x, y = 800 // 2, 90
    while x < 800 - 25:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x += 2
        delay(0.01)

def move_up():
    x, y = 800 - 25, 50 + 40
    while y < 600 - 50:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        y += 2
        delay(0.01)

def move_left():
    x, y = 800 - 25, 600 - 50
    while x > 0 + 25:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x -= 2
        delay(0.01)

def move_down():
    x, y = 0 + 25, 600 - 50
    while y > 50 + 40:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        y -= 2
        delay(0.01)


def move_left_to_center():
    x, y = 0 + 25, 50 + 40
    while x < 800//2:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x += 2
        delay(0.01)

# 검증된 코드는 #을 붙여서 생략하고 다음 확인해야 하는 코드를 확인한다.
def make_rectangle():
    move_from_center_to_right()
    move_up()
    move_left()
    move_down()
    move_left_to_center()


def make_circle():

    pass

while True:
    make_rectangle()
    make_circle()



close_canvas()
