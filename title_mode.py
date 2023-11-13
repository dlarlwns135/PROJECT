from pico2d import *

import charactor_choose_mode
import game_framework
import play_mode


def init():
    global image1, image2
    image1 = load_image('title_main.png')
    image2 = load_image('naruto_logo.png')
def finish():
    global image1, image2
    del image1, image2
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
    image2.draw(600, 300)
    #delay(0.01)
    update_canvas()

def update():
    pass