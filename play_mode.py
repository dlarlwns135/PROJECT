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
            exit(1)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE and (p1.win or p2.win):
            exit(1)
        else:
            p1.handle_event(event)
            p2.handle_event(event)


def init():
    global running
    global world
    global p1
    global p2
    global map
    global health_bar, health_hp, naruto_mug, sasuke_mug, chakra_image, chakra_frame
    global ko, fight, fight_frame

    health_bar = load_image('health_bar.png')
    health_hp = load_image('health_hp.png')
    naruto_mug = load_image('naruto_mugshot.png')
    sasuke_mug = load_image('sasuke_mugshot.png')
    chakra_image = load_image('chakra.png')
    chakra_frame = 0
    ko = load_image('ko.png')
    fight = load_image('fight.png')
    fight_frame = 0

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

    p1.x = 900
    p1.dir = -1
    p2.x = 300

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
    global chakra_frame, fight_frame
    game_world.update()
    game_world.handle_collisions()
    chakra_frame = (chakra_frame + 4 * game_framework.frame_time) % 4
    if fight_frame <= 1500:
        fight_frame += game_framework.frame_time * 800
    if p1.hp <= 0:
        p2.win = True
    if p2.hp <= 0:
        p1.win = True

def draw():
    clear_canvas()
    game_world.render()
    health_bar.clip_composite_draw(0, 0, 402, 22, 0, '', 300, 570, 402, 30)
    health_bar.clip_composite_draw(0, 0, 402, 22, 0, '', 900, 570, 402, 30)
    health_hp.clip_composite_draw(0, 0, 8, 9, 0, '', 300-(400-p2.hp)//2, 570, p2.hp, 28)
    health_hp.clip_composite_draw(0, 0, 8, 9, 0, '', 900-(400-p1.hp)//2, 570, p1.hp, 28)
    if p2.chakra >= 30:
        chakra_image.clip_composite_draw(int(chakra_frame)*32, 0, 32, 56, 0, '', 120, 520, 32, 56)
    if p2.chakra >= 60:
        chakra_image.clip_composite_draw(int(chakra_frame)*32, 0, 32, 56, 0, '', 160, 520, 32, 56)
    if p2.chakra >= 90:
        chakra_image.clip_composite_draw(int(chakra_frame)*32, 0, 32, 56, 0, '', 200, 520, 32, 56)

    if p1.chakra >= 30:
        chakra_image.clip_composite_draw(int(chakra_frame)*32, 0, 32, 56, 0, '', 1080, 520, 32, 56)
    if p1.chakra >= 60:
        chakra_image.clip_composite_draw(int(chakra_frame)*32, 0, 32, 56, 0, '', 1040, 520, 32, 56)
    if p1.chakra >= 90:
        chakra_image.clip_composite_draw(int(chakra_frame)*32, 0, 32, 56, 0, '', 1000, 520, 32, 56)

    if charactor_choose_mode.p1_choose_result() == 1:
        naruto_mug.clip_composite_draw(0, 0, 104, 112, 0, '', 1150, 550, 80, 80)
    elif charactor_choose_mode.p1_choose_result() == 2:
        sasuke_mug.clip_composite_draw(0, 0, 96, 104, 0, '', 1150, 550, 80, 80)

    if charactor_choose_mode.p2_choose_result() == 1:
        naruto_mug.clip_composite_draw(0, 0, 104, 112, 0, '', 50, 550, 80, 80)
    elif charactor_choose_mode.p2_choose_result() == 2:
        sasuke_mug.clip_composite_draw(0, 0, 96, 104, 0, '', 50, 550, 80, 80)

    if fight_frame <= 600:
        fight.clip_composite_draw(0, 0, 1601, 786, 0, '', 600, 900-int(fight_frame), 473, 228)
    elif 600 < fight_frame <= 900:
        fight.clip_composite_draw(0, 0, 1601, 786, 0, '', 600, 300, 473, 228)
    elif 900 < fight_frame <= 1500:
        fight.clip_composite_draw(0, 0, 1601, 786, 0, '', 600, int(fight_frame)-600, 473, 228)

    if p1.win or p2.win:
        ko.clip_composite_draw(0, 0, 473, 228, 0, '', 600, 300, 473, 228)
    update_canvas()

