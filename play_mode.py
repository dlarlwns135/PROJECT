from pico2d import *

from map import Map
from sasuke import SASUKE
from p2 import P2
from p3 import P3
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
            p3.handle_event(event)


def init():
    global running
    global world
    global p1
    global p2
    global p3
    global map

    running = True
    world = []

    map = Map()
    game_world.add_object(map, 1)

    if charactor_choose_mode.p1_choose_result() == 1:
        p2 = P2(1)
        game_world.add_object(p2, 1)
    elif charactor_choose_mode.p1_choose_result() == 2:
        p1 = SASUKE(1)
        game_world.add_object(p1, 1)

    if charactor_choose_mode.p2_choose_result() == 1:
        p2 = P2(2)
        game_world.add_object(p2, 1)
    elif charactor_choose_mode.p2_choose_result() == 2:
        p1 = SASUKE(2)
        game_world.add_object(p1, 1)


    # p1 = P1(2)
    # game_world.add_object(p1, 1)
    #
    # p2 = P2(1)
    # game_world.add_object(p2, 1)

    p3 = P3()
    # game_world.add_object(p3, 1)

def finish():
    pass
def update():
    game_world.update()

def draw():
    clear_canvas()
    game_world.render()
    delay(0.01)
    update_canvas()

