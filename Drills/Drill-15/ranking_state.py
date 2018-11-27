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
score = None

def enter():
    # game world is prepared already in world_build_state
    global font
    global score
    font = load_font('ENCR10B.TTF', 20)


    with open('score.json', 'r') as f:
        score = json.load(f)
    for i in range(len(score)):
        if(score[i] < score[i+1]):
            tmp = score[i]
            score[i + 1] = score[i]
            score[i + 1] = tmp
        pass



def exit():
    game_world.clear()


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
    count = 0
    font.draw(800, 850, '[Total Ranking]', (0,0,0))
    for i in score:
        if(count < 10):
            font.draw(200, 800 - (count * 80), '(# %d)' % (count + 1), (0, 0, 0))
            font.draw(300, 800 - (count * 80 ), '(Time: %3.4f)' % (i), (0, 0, 0))
            count += 1
    update_canvas()






