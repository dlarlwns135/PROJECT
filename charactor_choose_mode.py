from pico2d import *
import game_framework
import play_mode

character_count = 2

def init():
    global image1, naruto, sasuke
    global p1_x, p1_y, p2_x, p2_y, p1_choose, p2_choose, p1_image, p2_image
    global naruto_frame, sasuke_frame
    image1 = load_image('title_main.png')
    naruto = load_image('naruto_idle.png')
    sasuke = load_image('sasuke_idle.png')
    p1_image = load_image('p1_image.png')
    p2_image = load_image('p2_image.png')
    p1_x = 900
    p1_y = 360
    p2_x = 300
    p2_y = 360
    p1_choose = 1
    p2_choose = 2
    naruto_frame, sasuke_frame = 0, 0
def finish():
    global image1, naruto, sasuke, p1_image, p2_image
    del image1, naruto, sasuke, p1_image, p2_image
def handle_events():
    events = get_events()
    global p1_choose, p2_choose, character_count
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            if p1_choose != p2_choose:
                game_framework.change_mode(play_mode)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_a:
            p2_choose = (p2_choose - 1) % character_count
            if p2_choose == 0:
                p2_choose = character_count
        elif event.type == SDL_KEYDOWN and event.key == SDLK_d:
            p2_choose = (p2_choose + 1) % character_count
            if p2_choose == 0:
                p2_choose = character_count
        elif event.type == SDL_KEYDOWN and event.key == SDLK_LEFT:
            p1_choose = (p1_choose - 1) % character_count
            if p1_choose == 0:
                p1_choose = character_count
        elif event.type == SDL_KEYDOWN and event.key == SDLK_RIGHT:
            p1_choose = (p1_choose + 1) % character_count
            if p1_choose == 0:
                p1_choose = character_count

def running():
    pass
def draw():
    clear_canvas()
    image1.clip_composite_draw(0, 0, 900, 507, 0, '', 600, 300, 1200, 600)
    p1_image.clip_composite_draw(0, 0, 64, 32, 0, '', 300, 500, 120, 60)
    p2_image.clip_composite_draw(0, 0, 64, 32, 0, '', 900, 500, 120, 60)
    if p1_choose == 1:
        naruto.clip_composite_draw(int(naruto_frame)*32, 0, 32, 48, 0, '', p1_x, p1_y, 100, 150)
    elif p1_choose == 2:
        sasuke.clip_composite_draw(int(sasuke_frame)*32, 0, 32, 64, 0, '', p1_x, p1_y, 100, 200)

    if p2_choose == 1:
        naruto.clip_composite_draw(int(naruto_frame)*32, 0, 32, 48, 0, '', p2_x, p2_y, 100, 150)
    elif p2_choose == 2:
        sasuke.clip_composite_draw(int(sasuke_frame)*32, 0, 32, 64, 0, '', p2_x, p2_y, 100, 200)
    #delay(0.01)
    update_canvas()

def update():
    global naruto_frame, sasuke_frame
    naruto_frame = (naruto_frame + 6 * game_framework.frame_time) % 6
    sasuke_frame = (sasuke_frame + 6 * game_framework.frame_time) % 6


def p1_choose_result():
    global p1_choose
    return p1_choose

def p2_choose_result():
    global p2_choose
    return p2_choose