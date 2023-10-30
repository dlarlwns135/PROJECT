from pico2d import *
from p1 import P1
import game_framework
import game_world
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

def init():
    global running
    global world
    global p1

    running = True
    world = []

    p1 = P1()
    game_world.add_object(p1, 1)

def finish():
    pass
def update():
    game_world.update()

def draw():
    clear_canvas()
    game_world.render()
    delay(0.01)
    update_canvas()

