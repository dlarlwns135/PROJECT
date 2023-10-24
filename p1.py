# 이것은 각 상태들을 객체로 구현한 것임.

from pico2d import *

import game_world

# state event check
# ( state event type, event value )


def right_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_RIGHT


def right_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_RIGHT


def left_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_LEFT


def left_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_LEFT

def space_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_SPACE

def time_out(e):
    return e[0] == 'TIME_OUT'

def jump_end(e):
    return e[0] == 'JUMP_END'
# def jump_end(e):
#     global P1
#     if P1.jump_count >= 40:
#         return e[0] == 'jump_end'
#     pass


class Idle:

    @staticmethod
    def enter(p1, e):
        if p1.face_dir == -1:
            p1.action = 0
        elif p1.face_dir == 1:
            p1.action = 1
        p1.dir = 0
        p1.frame = 0
        p1.wait_time = get_time() # pico2d import 필요
        pass

    @staticmethod
    def exit(p1, e):
        pass

    @staticmethod
    def do(p1):
        p1.frame = (p1.frame + 1) % 6
        delay(0.1)

    @staticmethod
    def draw(p1):
        # p1.image.clip_draw(p1.frame * 34, 0, 30, 64, p1.x, p1.y)
        if p1.action == 0:
            p1.sasuke_idle.clip_composite_draw(p1.frame * 32, 0, 32, 64, 0, 'h', p1.x, p1.y, 100, 200)
        elif p1.action == 1:
            p1.sasuke_idle.clip_composite_draw(p1.frame * 32, 0, 32, 64, 0, '', p1.x, p1.y, 100 , 200)


class Run:

    @staticmethod
    def enter(p1, e):
        p1.y -= 15
        if right_down(e) or left_up(e): # 오른쪽으로 RUN
            p1.dir, p1.face_dir, p1.action = 1, 1, 1
        elif left_down(e) or right_up(e): # 왼쪽으로 RUN
            p1.dir, p1.face_dir, p1.action = -1, -1, 0

    @staticmethod
    def exit(p1, e):
        p1.y += 15

    @staticmethod
    def do(p1):
        p1.frame = (p1.frame + 1) % 6
        p1.x += p1.dir * 10
        delay(0.01)

    @staticmethod
    def draw(p1):
       # p1.sasuke_run.clip_draw(p1.frame * 64, p1.action * 31, 100, 100, p1.x, p1.y)
        if p1.action == 0:
            p1.sasuke_run.clip_composite_draw(p1.frame * 64, 0, 64, 32, 0, 'h', p1.x, p1.y, 200, 100)
        elif p1.action == 1:
            p1.sasuke_run.clip_composite_draw(p1.frame * 64, 0, 64, 32, 0, '', p1.x, p1.y, 200, 100)


def key_event(SDL_KEYUP, SDLK_SPACE):
    pass


class Jump:

    @staticmethod
    def enter(p1, e):
        p1.jump_count = 0
        p1.dir = 1
        p1.frame = 0
        if right_down(e) or left_up(e): # 오른쪽으로 RUN
            p1.dir, p1.face_dir, p1.action = 1, 1, 1
        elif left_down(e) or right_up(e): # 왼쪽으로 RUN
            p1.dir, p1.face_dir, p1.action = -1, -1, 0

    @staticmethod
    def exit(p1, e):
        p1.jump_count = 0
        p1.frame = 0
        pass

    @staticmethod
    def do(p1):
        p1.jump_count += 1

        # if right_down(e):
        #     p1.x += p1.dir * 10  # 오른쪽 방향으로 이동
        # elif left_down(e):
        #     p1.x += p1.dir * 10  # 왼쪽 방향으로 이동

        if p1.jump_count % 10 == 0:
            p1.frame = (p1.frame + 1) % 4
            #p1.jump_count = 0

        if p1.frame < 2:
            p1.y += p1.dir * 10
        else:
            p1.y -= p1.dir * 10

        if p1.jump_count >= 40:
            p1.state_machine.handle_event(('JUMP_END', None))
        delay(0.01)

    @staticmethod
    def draw(p1):
        if p1.action == 0:
            p1.sasuke_jump.clip_composite_draw(p1.frame * 32, 0, 32, 64, 0, 'h', p1.x, p1.y, 100, 200)
        elif p1.action == 1:
            p1.sasuke_jump.clip_composite_draw(p1.frame * 32, 0, 32, 64, 0, '', p1.x, p1.y, 100, 200)



class StateMachine:
    def __init__(self, p1):
        self.p1 = p1
        self.cur_state = Idle
        self.transitions = {
            Idle: {right_down: Run, left_down: Run, left_up: Run, right_up: Run, space_down: Jump},
            Run: {right_down: Idle, left_down: Idle, right_up: Idle, left_up: Idle, space_down: Jump},
            Jump: {jump_end: Idle}
        }

    def start(self):
        self.cur_state.enter(self.p1, ('NONE', 0))

    def update(self):
        self.cur_state.do(self.p1)

    def handle_event(self, e):
        for check_event, next_state in self.transitions[self.cur_state].items():
            if check_event(e):
                self.cur_state.exit(self.p1, e)
                self.cur_state = next_state
                self.cur_state.enter(self.p1, e)
                return True

        return False

    def draw(self):
        self.cur_state.draw(self.p1)





class P1:
    def __init__(self):
        self.up = None
        self.x, self.y = 400, 70
        self.frame = 0
        self.action = 3
        self.dir = 0
        self.face_dir = 1
        self.sasuke_idle = load_image('sasuke_idle.png')
        self.sasuke_run = load_image('sasuke_run.png')
        self.sasuke_jump = load_image('sasuke_jump.png')
        self.state_machine = StateMachine(self)
        self.state_machine.start()
        self.jump_count = 0

    def update(self):
        self.state_machine.update()

    def handle_event(self, event):
        self.state_machine.handle_event(('INPUT', event))

    def draw(self):
        self.state_machine.draw()
