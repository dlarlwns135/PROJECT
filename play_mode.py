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
    global health_bar, health_hp, naruto_mug, sasuke_mug

    health_bar = load_image('health_bar.png')
    health_hp = load_image('health_hp.png')
    naruto_mug = load_image('naruto_mugshot.png')
    sasuke_mug = load_image('sasuke_mugshot.png')

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
    game_world.add_collision_pair('p2:p1_skill1', p2, None)
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
    health_bar.clip_composite_draw(0, 0, 402, 22, 0, '', 300, 570, 402, 30)
    health_bar.clip_composite_draw(0, 0, 402, 22, 0, '', 900, 570, 402, 30)
    health_hp.clip_composite_draw(0, 0, 8, 9, 0, '', 300-(400-p2.hp)//2, 570, p2.hp, 28)
    health_hp.clip_composite_draw(0, 0, 8, 9, 0, '', 900-(400-p1.hp)//2, 570, p1.hp, 28)

    if charactor_choose_mode.p1_choose_result() == 1:
        naruto_mug.clip_composite_draw(0, 0, 104, 112, 0, '', 1150, 550, 80, 80)
    elif charactor_choose_mode.p1_choose_result() == 2:
        sasuke_mug.clip_composite_draw(0, 0, 96, 104, 0, '', 1150, 550, 80, 80)

    if charactor_choose_mode.p2_choose_result() == 1:
        naruto_mug.clip_composite_draw(0, 0, 104, 112, 0, '', 50, 550, 80, 80)
    elif charactor_choose_mode.p2_choose_result() == 2:
        sasuke_mug.clip_composite_draw(0, 0, 96, 104, 0, '', 50, 550, 80, 80)
    update_canvas()

