from pico2d import *

import charactor_choose_mode
import game_framework
import play_mode

def init():
    global image1, image2, naruto, sasuke, title_frame, sasuke_x, naruto_x
    global mode_num, logo_frame
    image1 = load_image('title_main.png')
    image2 = load_image('naruto_logo.png')
    naruto = load_image('title_naruto.png')
    sasuke = load_image('title_sasuke.png')
    title_frame = 0
    naruto_x, sasuke_x = 1200, 0
    mode_num = 1
    logo_frame = 0
def finish():
    global image1, image2, naruto, sasuke
    del image1, image2, naruto, sasuke
def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            game_framework.change_mode(charactor_choose_mode)

def running():
    pass
def draw():
    clear_canvas()
    image1.clip_composite_draw(0, 0, 900, 507, 0, '', 600, 300, 1200, 600)
    sasuke.clip_composite_draw(0, 0, 256, 191, 0, '', sasuke_x + title_frame, 300, 500, 380)
    naruto.clip_composite_draw(0, 0, 216, 192, 0, '', naruto_x - title_frame, 300, 430, 380)
    # image2.draw(600, 300)
    image2.clip_composite_draw(0, 0, 300, 144, 0, '', 600, 800 - logo_frame, 500, 230)
    update_canvas()

def update():
    global title_frame, mode_num, logo_frame
    if mode_num == 1:
        title_frame = title_frame + 300 * game_framework.frame_time
        if title_frame >= 800:
            mode_num = 2
    elif mode_num == 2:
        logo_frame = logo_frame + 300 * game_framework.frame_time
        if logo_frame >= 500:
            mode_num = 3


