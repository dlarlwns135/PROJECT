from pico2d import *
import game_framework
import play_mode

character_count = 2

def init():
    global image1, naruto, sasuke
    global p1_x, p1_y, p2_x, p2_y, p1_choose, p2_choose
    image1 = load_image('title_main.png')
    naruto = load_image('naruto_idle.png')
    sasuke = load_image('sasuke_idle.png')
    p1_x = 600
    p1_y = 450
    p2_x = 600
    p2_y = 150
    p1_choose = 1
    p2_choose = 2
def finish():
    global image1, naruto, sasuke
    del image1, naruto, sasuke
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
    if p1_choose == 1:
        naruto.clip_composite_draw(0, 0, 192, 48, 0, '', p1_x, p1_y, 192, 48)
    elif p1_choose == 2:
        sasuke.clip_composite_draw(0, 0, 192, 64, 0, '', p1_x, p1_y, 192, 64)

    if p2_choose == 1:
        naruto.clip_composite_draw(0, 0, 192, 48, 0, '', p2_x, p2_y, 192, 48)
    elif p2_choose == 2:
        sasuke.clip_composite_draw(0, 0, 192, 64, 0, '', p2_x, p2_y, 192, 64)
    #delay(0.01)
    update_canvas()

def update():
    pass

def p1_choose_result():
    global p1_choose
    return p1_choose

def p2_choose_result():
    global p2_choose
    return p2_choose