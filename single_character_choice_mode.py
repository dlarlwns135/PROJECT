from pico2d import *
import game_framework
import round1

character_count = 3

def init():
    global image1, naruto, sasuke, itachi
    global p1_x, p1_y, p2_x, p2_y, p1_choose, p2_choose, p1_image, p2_image, character_back
    global vs, press_space
    global naruto_frame, sasuke_frame, itachi_frame, space_frame, space_up
    global duplicate, dup_on, dup_wait_time
    image1 = load_image('resource/title_main.png')
    naruto = load_image('resource/naruto_idle.png')
    sasuke = load_image('resource/sasuke_idle.png')
    itachi = load_image('resource/itachi_idle.png')
    # p1_image = load_image('resource/p1_image.png')
    # p2_image = load_image('resource/p2_image.png')
    character_back = load_image('resource/charactor_back.png')
    # vs = load_image('resource/vs.png')
    press_space = load_image('resource/press_space.png')
    # duplicate = load_image('resource/duplicate.png')
    p1_x = 600
    p1_y = 360
    # p2_x = 300
    # p2_y = 360
    p1_choose = 1
    # p2_choose = 3
    naruto_frame, sasuke_frame, itachi_frame = 0, 0, 0
    space_frame = 0
    space_up = True
    dup_on = False
    dup_wait_time = 0
def finish():
    global image1, naruto, sasuke, itachi, character_back, press_space
    del image1, naruto, sasuke, itachi, character_back, press_space
def handle_events():
    events = get_events()
    global p1_choose, p2_choose, character_count, dup_on, dup_wait_time
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            # if p1_choose != p2_choose:
            game_framework.change_mode(round1)
            # else:
            #     dup_on = True
            #     dup_wait_time = get_time()
        # elif event.type == SDL_KEYDOWN and event.key == SDLK_a:
        #     p2_choose = (p2_choose - 1) % character_count
        #     if p2_choose == 0:
        #         p2_choose = character_count
        # elif event.type == SDL_KEYDOWN and event.key == SDLK_d:
        #     p2_choose = (p2_choose + 1) % character_count
        #     if p2_choose == 0:
        #         p2_choose = character_count
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
    # vs.clip_composite_draw(0, 0, 2500, 2500, 0, '', 600, 300, 200, 200)
    character_back.clip_composite_draw(0, 0, 64, 76, 0, '', 600, 300, 340, 430)
    # character_back.clip_composite_draw(0, 0, 64, 76, 0, '', 900, 300, 340, 430)
    # p1_image.clip_composite_draw(0, 0, 64, 32, 0, '', 900, 500, 120, 60)
    # p2_image.clip_composite_draw(0, 0, 64, 32, 0, '', 300, 500, 120, 60)
    if p1_choose == 1:
        naruto.clip_composite_draw(int(naruto_frame)*32, 0, 32, 48, 0, 'h', p1_x, p1_y, 100, 150)
    elif p1_choose == 2:
        sasuke.clip_composite_draw(int(sasuke_frame)*32, 0, 32, 64, 0, 'h', p1_x, p1_y, 100, 200)
    elif p1_choose == 3:
        itachi.clip_composite_draw(int(itachi_frame)*32, 0, 32, 64, 0, 'h', p1_x, p1_y+15, 100, 200)

    # if p2_choose == 1:
    #     naruto.clip_composite_draw(int(naruto_frame)*32, 0, 32, 48, 0, '', p2_x, p2_y, 100, 150)
    # elif p2_choose == 2:
    #     sasuke.clip_composite_draw(int(sasuke_frame)*32, 0, 32, 64, 0, '', p2_x, p2_y, 100, 200)
    # elif p2_choose == 3:
    #     itachi.clip_composite_draw(int(itachi_frame) * 32, 0, 32, 64, 0, '', p2_x, p2_y+15, 100, 200)

    if space_up:
        press_space.clip_composite_draw(0, 0, 1920, 1080, 0, '', 600, 60 + space_frame, 900, 500)
    else:
        press_space.clip_composite_draw(0, 0, 1920, 1080, 0, '', 600, 70 - space_frame, 900, 500)

    if dup_on:
        duplicate.clip_composite_draw(0, 0, 5906, 4135, 0, '', 600, 300, 600, 300)
    update_canvas()

def update():
    global naruto_frame, sasuke_frame, itachi_frame, space_frame, space_up, dup_wait_time, dup_on
    naruto_frame = (naruto_frame + 6 * game_framework.frame_time) % 6
    sasuke_frame = (sasuke_frame + 6 * game_framework.frame_time) % 6
    itachi_frame = (itachi_frame + 4 * game_framework.frame_time) % 4
    space_frame = space_frame + 10 * game_framework.frame_time
    if space_frame >= 9:
        if space_up:
            space_up = False
        else:
            space_up = True
        space_frame = 0

    # if p1_choose == p2_choose:
    #     dup_wait_time = get_time()
    #     dup_on = True

    if get_time() - dup_wait_time > 1:
        dup_on = False


def p1_choose_result():
    global p1_choose
    return p1_choose

def p2_choose_result():
    global p2_choose
    return p2_choose