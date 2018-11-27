import random
import json
import pickle
import os

from pico2d import *
import game_framework
import game_world
import ranking_state
import world_build_state
name = "MainState"

#버틴 시간
safe_time = 0
array = []
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

twice_zombie = None

def enter():
    # game world is prepared already in world_build_state
    global boy
    global safe_time
    global twice_zombie
    boy = world_build_state.get_boy()
    twice_zombie = world_build_state.returnZombie
    safe_time = 0
    pass

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
        elif event.type == SDL_KEYDOWN and event.key == SDLK_s:
            game_world.save()
        else:
            boy.handle_event(event)

test_count = 0
def update():
    global safe_time
    global twice_zombie
    global test_count
    global array
    safe_time += 0.1

    for game_object in game_world.all_objects():
        game_object.update()

    for zombie_count in twice_zombie:
        if collide(boy, zombie_count):
            print(zombie_count)
            with open('score.json', 'r', encoding="utf-8") as f:
                array = json.load(f)

            

            with open('score.json', 'w', encoding="utf-8") as f:
                json.dump((safe_time), f, ensure_ascii=False, indent='\t')
            game_framework.change_state(ranking_state)
            break


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()





