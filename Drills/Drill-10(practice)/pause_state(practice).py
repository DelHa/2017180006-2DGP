import game_framework
import main_state
from pico2d import *
import main_state

#따로 뺀 py

name = "PauseState"
image = None


def enter():
    global image
    image = load_image('pause.png')
    pass


def exit():
    global image
    del(image)
    pass
Sel = False

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if(event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type , event.key) == (SDL_KEYDOWN , SDLK_p):
                game_framework.pop_state()
    pass


i = 0


def draw():
    global i
    global image
    if(i%2 == 0):
        clear_canvas()
        main_state.draw()
        image.draw(400, 300)
        update_canvas()
        delay(0.5)
    else:
        clear_canvas()
        main_state.draw()
        update_canvas()
        delay(0.5)

    i += 1
    pass

def update():
    pass


def pause():
    pass


def resume():
    pass






