import random
import json
import pickle
import os

from pico2d import *
import game_framework
import game_world
import main_state
import world_build_state

name = "RankingState"
font = None

score = []

def collide(a, b):
    # fill here
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True

boy = None

def enter():
    # game world is prepared already in world_build_state
    global font
    global score
    font = load_font('ENCR10B.TTF', 40)
    print(main_state.safe_time)

    with open('score.json', 'r', encoding="utf-8") as f:
        score = json.load(f)


def exit():
    game_world.clear()

def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(world_build_state)


def update():
    for game_object in game_world.all_objects():
        game_object.update()


def draw():
    global font
    clear_canvas()
#    for game_object in game_world.all_objects():
#        game_object.draw()
    for i in score:
        font.draw(300, 400, '(Time: %3.2f)' % (score[i]), (0, 0, 0))

    update_canvas()






