# 이것은 각 상태들을 객체로 구현한 것임.

from pico2d import *

import game_world

# state event check
# ( state event type, event value )

ground_y = 70

def up_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_UP


def up_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_UP

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

def period_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_PERIOD

def time_out(e):
    return e[0] == 'TIME_OUT'

def jump_end(e):
    return e[0] == 'JUMP_END'

def jump_end_run(e):
    return e[0] == 'JUMP_END_RUN'

def teleport(e):
    return e[0] == 'TELEPORT'

def stop(e):
    return e[0] == 'STOP'

class Idle:

    @staticmethod
    def enter(p1, e):
        p1.frame = 0
        if right_up(e):
            p1.right = False
        elif left_up(e):
            p1.left = False
        #p1.wait_time = get_time() # pico2d import 필요
        pass

    @staticmethod
    def exit(p1, e):
        p1.frame = 0
        p1.idle_count = 0
        if right_up(e):
            p1.dir = -1
        elif left_up(e):
            p1.dir = 1
        pass

    @staticmethod
    def do(p1):
        p1.frame = (p1.frame + 1) % 6
        #delay(0.1)

    @staticmethod
    def draw(p1):
        if p1.dir == -1:
            p1.idle.clip_composite_draw(p1.frame * 32, 0, 32, 64, 0, 'h', p1.x, p1.y, 100, 200)
        elif p1.dir == 1:
            p1.idle.clip_composite_draw(p1.frame * 32, 0, 32, 64, 0, '', p1.x, p1.y, 100 , 200)


class Run:

    @staticmethod
    def enter(p1, e):

        p1.y -= 15
        if right_down(e):
            p1.dir = 1
            p1.right = True
        elif left_down(e):
            p1.dir = -1
            p1.left = True
        elif right_up(e):
            p1.right = False
        elif left_up(e):
            p1.left = False

    @staticmethod
    def exit(p1, e):
        p1.y += 15
        p1.frame = 0

    @staticmethod
    def do(p1):
        if p1.right and p1.left:
            if p1.dir == 1:
                p1.dir = -1
            elif p1.dir == -1:
                p1.dir = 1
            p1.state_machine.handle_event(('STOP', None))
        if not p1.right and not p1.left:
            p1.state_machine.handle_event(('STOP', None))
            p1.right = False
            p1.left = False
        p1.frame = (p1.frame + 1) % 6
        p1.x += p1.dir * 10
        #delay(0.01)

    @staticmethod
    def draw(p1):
        if p1.dir == -1:
            p1.run.clip_composite_draw(p1.frame * 64, 0, 64, 32, 0, 'h', p1.x, p1.y, 200, 100)
        elif p1.dir == 1:
            p1.run.clip_composite_draw(p1.frame * 64, 0, 64, 32, 0, '', p1.x, p1.y, 200, 100)


class Jump:
    @staticmethod
    def enter(p1, e):
        if right_down(e):
            p1.dir = 1
            p1.right = True
            p1.jump_move = True
        elif left_down(e):
            p1.dir = -1
            p1.left = True
            p1.jump_move = True
        elif right_up(e):
            p1.right = False
        elif left_up(e):
            p1.left = False
        pass

    @staticmethod
    def exit(p1, e):
        if up_down(e):
            p1.frame = 0
            p1.jump_count = 0
        pass

    @staticmethod
    def do(p1):
        if not p1.right and not p1.left:
            p1.jump_move = False
        p1.jump_count += 1

        if p1.jump_count >= 40:
            p1.frame = 3
        else:
            p1.frame = p1.jump_count // 10

        if p1.frame < 2:
            p1.y += 10
        else:
            p1.y -= 10

        if p1.jump_move and  (p1.right or p1.left):
            p1.x += p1.dir * 5

        if p1.y <= ground_y:
            p1.y = ground_y
            p1.jump_count = 0
            p1.frame = 0

            if p1.jump_move:
                p1.state_machine.handle_event(('JUMP_END_RUN', None))
                print("JUMP_END_RUN")
            else:
                p1.state_machine.handle_event(('JUMP_END', None))
                print("JUMP_END")
            p1.jump_move = False
        #delay(0.01)

    @staticmethod
    def draw(p1):
        if p1.dir == -1:
            p1.jump.clip_composite_draw(p1.frame * 32, 0, 32, 64, 0, 'h', p1.x, p1.y, 100, 200)
        elif p1.dir == 1:
            p1.jump.clip_composite_draw(p1.frame * 32, 0, 32, 64, 0, '', p1.x, p1.y, 100, 200)

class Teleport:
    @staticmethod
    def enter(p1, e):

        pass

    @staticmethod
    def exit(p1, e):
        p1.tele_count = 0
        if p1.dir == 1:
            p1.x += 300
        elif p1.dir == -1:
            p1.x -= 300
        pass

    @staticmethod
    def do(p1):
        p1.tele_count += 1
        p1.frame = p1.tele_count // 2
        if p1.frame >= 5:
            p1.state_machine.handle_event(('TELEPORT', None))

        #delay(0.01)
        pass

    @staticmethod
    def draw(p1):
        if p1.dir == -1:
            p1.teleport.clip_composite_draw(p1.frame * 32, 0, 32, 64, 0, 'h', p1.x, p1.y, 100, 200)
            p1.teleport_motion.clip_composite_draw(p1.frame * 72, 0, 72, 75, 0, 'h', p1.x, p1.y, 150, 250)
        elif p1.dir == 1:
            p1.teleport.clip_composite_draw(p1.frame * 32, 0, 32, 64, 0, '', p1.x, p1.y, 100, 200)
            p1.teleport_motion.clip_composite_draw(p1.frame * 72, 0, 72, 75, 0, '', p1.x, p1.y, 150, 250)



class StateMachine:
    def __init__(self, p1):
        self.p1 = p1
        self.cur_state = Idle
        self.transitions = {
            Idle: {right_down: Run, left_down: Run, right_up: Run, left_up: Run,
                   up_down: Jump, period_down: Teleport},
            Run: {right_up: Run, left_up: Run, right_down: Run, left_down: Run, up_down: Jump, stop: Idle},
            Jump: {jump_end: Idle, jump_end_run: Run, up_down: Jump,
                   right_down: Jump, left_down: Jump, right_up: Jump, left_up: Jump},
            Teleport: {teleport: Idle}
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
        self.x, self.y = 400, ground_y
        self.frame = 0
        self.dir = 1
        self.idle_count = 0
        self.tele_count = 0
        self.idle = load_image('sasuke_idle.png')
        self.run = load_image('sasuke_run.png')
        self.jump = load_image('sasuke_jump.png')
        self.teleport = load_image('sasuke_teleport.png')
        self.teleport_motion = load_image('teleport.png')
        self.state_machine = StateMachine(self)
        self.state_machine.start()
        self.jump_count = 0
        self.jump_move = False
        self.run_check = 0
        self.right = False
        self.left = False

    def update(self):
        self.state_machine.update()

    def handle_event(self, event):
        self.state_machine.handle_event(('INPUT', event))

    def draw(self):
        self.state_machine.draw()
