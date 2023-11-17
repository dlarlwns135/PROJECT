from pico2d import *

from map import Map
from sasuke import SASUKE
from naruto import NARUTO
import game_framework
import game_world
import charactor_choose_mode
def handle_events():
    global running

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        else:
            p1.handle_event(event)
            p2.handle_event(event)


def init():
    global running
    global world
    global p1
    global p2
    global map

    running = True
    world = []

    map = Map()
    game_world.add_object(map, 1)

    if charactor_choose_mode.p1_choose_result() == 1:
        p1 = NARUTO(1)
        game_world.add_object(p1, 1)
    elif charactor_choose_mode.p1_choose_result() == 2:
        p1 = SASUKE(1)
        game_world.add_object(p1, 1)

    if charactor_choose_mode.p2_choose_result() == 1:
        p2 = NARUTO(2)
        game_world.add_object(p2, 1)
    elif charactor_choose_mode.p2_choose_result() == 2:
        p2 = SASUKE(2)
        game_world.add_object(p2, 1)

    game_world.add_collision_pair('p1:p2_attack', p1, None)
    game_world.add_collision_pair('p1:p2_shuriken', p1, None)
    game_world.add_collision_pair('p1:p2_skill1', p1, None)
    game_world.add_collision_pair('p1:p2_skill2', p1, None)

    game_world.add_collision_pair('p2:p1_attack', p2, None)
    game_world.add_collision_pair('p2:p1_shuriken', p2, None)
    game_world.add_collision_pair('p1:p2_skill1', p2, None)
    game_world.add_collision_pair('p2:p1_skill2', p2, None)
    # p1 = P1(2)
    # game_world.add_object(p1, 1)
    #
    # p2 = P2(1)
    # game_world.add_object(p2, 1)

    # p3 = P3()
    # game_world.add_object(p3, 1)

def finish():
    pass
def update():
    game_world.update()
    game_world.handle_collisions()

def draw():
    clear_canvas()
    game_world.render()
   # delay(0.01)
    update_canvas()

