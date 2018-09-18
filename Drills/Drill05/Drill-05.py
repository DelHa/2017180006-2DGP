from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

# 0918메모
# 함수를 사용하면 코드를 읽기가 쉬워진다.
# 함수 이름은 '항상 동사'로 시작되어야한다.
# 함수를 적절하게 사용하면 코더의 의도가 보인다.
def move_from_center_to_right():
    pass
def move_up():
    pass
def move_left():
    pass
def move_down():
    pass
def move_left_to_center():
    pass


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
