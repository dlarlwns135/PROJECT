# 이것은 각 상태들을 객체로 구현한 것임.

from pico2d import *

import game_framework
import game_world
from skill import Skill1, Skill2

PIXEL_PER_METER = (10.0 / 0.3) # 10 pixel 30 cm
RUN_SPEED_KMPH = 50.0 # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# state event check
# ( state event type, event value )

ground_y = 70
tele_dis = 220

def up_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_UP

def up_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_UP

def down_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_DOWN

def down_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_DOWN

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

def comma_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_COMMA

def slash_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_SLASH

def w_down(e):
    return  e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_w

def w_up(e):
    return  e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_w

def s_down(e):
    return  e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_s

def s_up(e):
    return  e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_s

def a_down(e):
    return  e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_a

def a_up(e):
    return  e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_a

def d_down(e):
    return  e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_d

def d_up(e):
    return  e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_d

def c_down(e):
    return  e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_c

def c_up(e):
    return  e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_c

def v_down(e):
    return  e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_v

def v_up(e):
    return  e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_v

def b_down(e):
    return  e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_b

def b_up(e):
    return  e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_b




def time_out(e):
    return e[0] == 'TIME_OUT'

def jump_end(e):
    return e[0] == 'JUMP_END'

def jump_end_run(e):
    return e[0] == 'JUMP_END_RUN'

def teleport(e):
    return e[0] == 'TELEPORT'

def jump_state(e):
    return e[0] == 'JUMP_STATE'

def run_state(e):
    return e[0] == 'RUN_STATE'

def stop(e):
    return e[0] == 'STOP'

class Idle:

    @staticmethod
    def enter(p2, e):
        # print(p2.skill_num)
        p2.frame = 0
        if d_up(e):
            p2.right = False
        elif a_up(e):
            p2.left = False
        elif d_down(e):
            p2.right = True
        elif a_down(e):
            p2.left = True
        #p2.wait_time = get_time() # pico2d import 필요
        pass

    @staticmethod
    def exit(p2, e):
        print(p2.skill_num)
        p2.frame = 0
        if s_down(e):
            p2.skill_num = 2
        if s_up(e):
            p2.skill_num = 1
        if b_down(e):
            p2.skill()
        if d_down(e):
            p2.right = True
        elif a_down(e):
            p2.left = True
        elif d_up(e):
            p2.right = False
        elif a_up(e):
            p2.left = False

    @staticmethod
    def do(p2):
        if p2.y > ground_y:
            p2.state_machine.handle_event(('JUMP_STATE', None))
        if p2.right and not p2.left:
            p2.state_machine.handle_event(('RUN_STATE', None))
        if not p2.right and p2.left:
            p2.state_machine.handle_event(('RUN_STATE', None))
        # if not (p2.right and p2.left):
        #     p2.state_machine.handle_event(('RUN_STATE', None))
        p2.frame = (p2.frame + 6 * 1 * game_framework.frame_time) % 6
        #delay(0.1)

    @staticmethod
    def draw(p2):
        if p2.dir == -1:
            p2.idle.clip_composite_draw(int(p2.frame) * 32, 0, 32, 48, 0, 'h', p2.x, p2.y - 15, 90, 135)
        elif p2.dir == 1:
            p2.idle.clip_composite_draw(int(p2.frame) * 32, 0, 32, 48, 0, '', p2.x, p2.y - 15, 90, 135)


class Run:

    @staticmethod
    def enter(p2, e):

        p2.y -= 15
        if d_down(e):
            p2.right = True
        elif a_down(e):
            p2.left = True
        elif d_up(e):
            p2.right = False
            # p2.dir = -1
        elif a_up(e):
            p2.left = False
            # p2.dir = 1

        if p2.right and not p2.left:
            p2.dir = 1
        elif p2.left and not p2.right:
            p2.dir = -1
        elif not p2.right and p2.left:
            p2.dir = -1
        elif not p2.left and p2.right:
            p2.dir = 1
    @staticmethod
    def exit(p2, e):
        p2.y += 15
        p2.frame = 0

    @staticmethod
    def do(p2):
        # if p2.right and p2.left:
        #     p2.state_machine.handle_event(('STOP', None))
        # if not p2.right and not p2.left:
        #     p2.state_machine.handle_event(('STOP', None))
        p2.frame = (p2.frame + 6 * 2 * game_framework.frame_time) % 6
        p2.x += p2.dir * RUN_SPEED_PPS * game_framework.frame_time
        #delay(0.01)

    @staticmethod
    def draw(p2):
        if p2.dir == -1:
            p2.run.clip_composite_draw(int(p2.frame) * 48, 0, 48, 48, 0, 'h', p2.x, p2.y, 135, 135)
        elif p2.dir == 1:
            p2.run.clip_composite_draw(int(p2.frame) * 48, 0, 48, 48, 0, '', p2.x, p2.y, 135, 135)


class Jump:
    @staticmethod
    def enter(p2, e):
        if d_down(e):
            p2.dir = 1
            p2.right = True
            p2.jump_move = True
            p2.up_tele = False
        if a_down(e):
            p2.dir = -1
            p2.left = True
            p2.jump_move = True
            p2.up_tele = False
        if d_up(e):
            p2.right = False
        if a_up(e):
            p2.left = False
        if w_down(e):
            p2.up_tele = True
        if w_up(e):
            p2.up_tele = False
        if jump_state(e):
            p2.frame = 2
        if p2.right or p2.left:
            p2.jump_move = True
        p2.jump_state = True
        pass

    @staticmethod
    def exit(p2, e):
        if w_down(e):
            p2.frame = 0
        if b_down(e):
            p2.skill()
        pass

    @staticmethod
    def do(p2):
        if not p2.right and not p2.left:
            p2.jump_move = False
        if p2.frame >= 3:
            p2.frame = 3
        else:
            p2.frame = (p2.frame + 4 * 2 * game_framework.frame_time) % 4

        if p2.frame < 2:
            p2.y += 1.5 * RUN_SPEED_PPS * game_framework.frame_time
        else:
            p2.y -= 1.5 * RUN_SPEED_PPS * game_framework.frame_time

        if p2.jump_move and  (p2.right or p2.left):
            p2.x += p2.dir * RUN_SPEED_PPS * game_framework.frame_time

        if p2.y <= ground_y:
            p2.y = ground_y
            p2.frame = 0
            # if p2.jump_move:
            #     pass
            #     # p2.state_machine.handle_event(('JUMP_END_RUN', None))
            #     # print("JUMP_END_RUN")
            # else:
            p2.state_machine.handle_event(('JUMP_END', None))
            print("JUMP_END")
            p2.jump_state = False
            p2.jump_move = False
        #delay(0.01)

    @staticmethod
    def draw(p2):
        if p2.dir == -1:
            if int(p2.frame) < 2:
                p2.jump.clip_composite_draw(int(p2.frame) * 32, 0, 32, 48, 0, 'h', p2.x, p2.y, 90, 135)
            else:
                p2.jump.clip_composite_draw(64 + (int(p2.frame) - 2) * 40, 0, 40, 48, 0, 'h', p2.x, p2.y, 90, 135)
        elif p2.dir == 1:
            if int(p2.frame) < 2:
                p2.jump.clip_composite_draw(int(p2.frame) * 32, 0, 32, 48, 0, '', p2.x, p2.y, 90, 135)
            else:
                p2.jump.clip_composite_draw(64 + (int(p2.frame) - 2) * 40, 0, 40, 48, 0, '', p2.x, p2.y, 90, 135)

class Teleport:
    @staticmethod
    def enter(p2, e):
        p2.frame = 0
        if d_down(e):
            p2.dir = 1
            p2.right = True
        elif a_down(e):
            p2.dir = -1
            p2.left = True
        elif d_up(e):
            p2.right = False
        elif a_up(e):
            p2.left = False
        pass

    @staticmethod
    def exit(p2, e):
        if p2.frame >= 3:
            if p2.up_tele:
                p2.y += tele_dis
                p2.up_tele = False
            else:
                if p2.right:
                    p2.x += tele_dis
                elif p2.left:
                    p2.x -= tele_dis
        pass

    @staticmethod
    def do(p2):
        p2.frame = p2.frame + 4 * 5 * game_framework.frame_time
        if p2.frame >= 3:
            p2.state_machine.handle_event(('TELEPORT', None))
        #delay(0.01)
        pass

    @staticmethod
    def draw(p2):
        if p2.dir == -1:
            p2.teleport.clip_composite_draw(int(p2.frame) * 32, 0, 32, 64, 0, 'h', p2.x, p2.y, 100, 200)
            p2.teleport_motion.clip_composite_draw(int(p2.frame) * 72, 0, 72, 75, 0, 'h', p2.x, p2.y, 150, 250)
        elif p2.dir == 1:
            p2.teleport.clip_composite_draw(int(p2.frame) * 32, 0, 32, 64, 0, '', p2.x, p2.y, 100, 200)
            p2.teleport_motion.clip_composite_draw(int(p2.frame) * 72, 0, 72, 75, 0, '', p2.x, p2.y, 150, 250)

class Attack:
    @staticmethod
    def enter(p2, e):
        if d_down(e):
            p2.right = True
        if a_down(e):
            p2.left = True
        if d_up(e):
            p2.right = False
        if a_up(e):
            p2.left = False
        if get_time() - p2.wait_time > 0.5:
            p2.attack_num = 1
        pass

    @staticmethod
    def exit(p2, e):
        pass

    @staticmethod
    def do(p2):
        p2.frame = p2.frame + 7 * 3 * game_framework.frame_time
        if p2.attack_num == 1:
            if p2.frame >= 4:
                p2.state_machine.handle_event(('STOP', None))
                p2.attack_num = 2
                p2.frame = 0
                p2.wait_time = get_time()
        if p2.attack_num == 2:
            if p2.frame >= 5:
                p2.state_machine.handle_event(('STOP', None))
                p2.attack_num = 3
                p2.frame = 0
                p2.wait_time = get_time()
        if p2.attack_num == 3:
            if p2.frame >= 7:
                p2.state_machine.handle_event(('STOP', None))
                p2.attack_num = 4
                p2.frame = 0
                p2.wait_time = get_time()
        if p2.attack_num == 4:
            if p2.frame >= 6.5:
                p2.state_machine.handle_event(('STOP', None))
                p2.attack_num = 1
                p2.frame = 0
                p2.wait_time = get_time()
        pass

    @staticmethod
    def draw(p2):
        if p2.attack_num == 1:
            if p2.dir == -1:
                p2.attack1.clip_composite_draw(int(p2.frame) * 56, 0, 56, 48, 0, 'h', p2.x-34, p2.y - 15, 158, 135)
            elif p2.dir == 1:
                p2.attack1.clip_composite_draw(int(p2.frame) * 56, 0, 56, 48, 0, '', p2.x + 10, p2.y - 15, 158, 135)
        elif p2.attack_num == 2:
            if p2.dir == -1:
                p2.attack2.clip_composite_draw(int(p2.frame) * 64, 0, 64, 64, 0, 'h', p2.x-50, p2.y, 200, 200)
            elif p2.dir == 1:
                p2.attack2.clip_composite_draw(int(p2.frame) * 64, 0, 64, 64, 0, '', p2.x+50, p2.y, 200, 200)
        elif p2.attack_num == 3:
            if p2.dir == -1:
                    p2.attack3.clip_composite_draw(int(p2.frame) * 77, 0, 77, 64, 0, 'h', p2.x - 70, p2.y, 241, 200)
            elif p2.dir == 1:
                    p2.attack3.clip_composite_draw(int(p2.frame) * 77, 0, 77, 64, 0, '', p2.x + 70, p2.y, 241, 200)
        elif p2.attack_num == 4:
            if p2.dir == -1:
                    p2.attack4.clip_composite_draw(int(p2.frame) * 72, 0, 72, 66, 0, 'h', p2.x - 62, p2.y+3, 225, 206)
            elif p2.dir == 1:
                    p2.attack4.clip_composite_draw(int(p2.frame) * 72, 0, 72, 66, 0, '', p2.x + 62, p2.y+3, 225, 206)


class Skill_motion:
    @staticmethod
    def enter(p2, e):
        if d_down(e):
            p2.right = True
        elif a_down(e):
            p2.left = True
        elif d_up(e):
            p2.right = False
        elif a_up(e):
            p2.left = False
        pass

    @staticmethod
    def exit(p2, e):

        pass

    @staticmethod
    def do(p2):
        if p2.skill_num == 2:
            p2.frame = (p2.frame + 19 * 1.0 * game_framework.frame_time) % 19
            if p2.frame >= 8:
                p2.x += p2.dir * RUN_SPEED_PPS * 2 * game_framework.frame_time
            if p2.frame >= 18:
                p2.skill_num = 1
                p2.frame = 0
                p2.state_machine.handle_event(('STOP', None))
        elif p2.skill_num == 1:
            p2.frame = (p2.frame + 4 * 4 * game_framework.frame_time) % 4
            if p2.frame >= 3:
                p2.skill_num = 1
                p2.frame = 0
                p2.state_machine.handle_event(('STOP', None))
        pass

    @staticmethod
    def draw(p2):
        # p2.attack4.clip_composite_draw(p2.frame * 72, 0, 72, 66, 0, 'h', p2.x - 62, p2.y - 3, 225, 206)
        if p2.skill_num == 2:
            if p2.dir == -1:
                p2.skill2.clip_composite_draw(int(p2.frame) * 104, 0, 104, 77, 0, 'h', p2.x, p2.y+41, 325, 241)
            elif p2.dir == 1:
                p2.skill2.clip_composite_draw(int(p2.frame) * 104, 0, 104, 77, 0, '', p2.x, p2.y+41, 325, 241)
        elif p2.skill_num == 1:
            if p2.jump_state:
                if p2.dir == -1:
                    p2.skill1_jump.clip_composite_draw(int(p2.frame) * 40, 0, 40, 64, 0, 'h', p2.x, p2.y, 125, 200)
                elif p2.dir == 1:
                    p2.skill1_jump.clip_composite_draw(int(p2.frame) * 40, 0, 40, 64, 0, '', p2.x, p2.y, 125, 200)
            else:
                if p2.dir == -1:
                    p2.skill1_stand.clip_composite_draw(int(p2.frame) * 40, 0, 40, 64, 0, 'h', p2.x, p2.y, 125, 200)
                elif p2.dir == 1:
                    p2.skill1_stand.clip_composite_draw(int(p2.frame) * 40, 0, 40, 64, 0, '', p2.x, p2.y, 125, 200)
        pass

class StateMachine:
    def __init__(self, p2):
        self.p2 = p2
        self.cur_state = Idle
        self.transitions = {
            Idle: {d_down: Run, a_down: Run, d_up: Idle, a_up: Idle, run_state: Run,
                   w_down: Jump, jump_state: Jump, c_down: Attack, b_down: Skill_motion,
                   s_down: Idle, s_up: Idle},
            Run: {d_up: Idle, a_up: Idle, d_down: Idle, a_down: Idle, w_down: Jump, stop: Idle
                  , v_down: Teleport},
            Jump: {jump_end: Idle, jump_end_run: Run, w_down: Jump, w_up: Jump,
                   v_down: Teleport, b_down: Skill_motion,
                   d_down: Jump, a_down: Jump, d_up: Jump, a_up: Jump},
            Teleport: {d_down: Teleport, a_down: Teleport, d_up: Teleport, a_up: Teleport,
                       teleport: Idle},
            Attack: {stop: Idle, d_down: Attack, a_down: Attack, d_up: Attack, a_up: Attack},
            Skill_motion: {stop: Idle, d_up: Skill_motion, a_up: Skill_motion,
                           d_down: Skill_motion, a_down: Skill_motion}
        }

    def start(self):
        self.cur_state.enter(self.p2, ('NONE', 0))

    def update(self):
        self.cur_state.do(self.p2)

    def handle_event(self, e):
        for check_event, next_state in self.transitions[self.cur_state].items():
            if check_event(e):
                self.cur_state.exit(self.p2, e)
                self.cur_state = next_state
                self.cur_state.enter(self.p2, e)
                return True

        return False

    def draw(self):
        self.cur_state.draw(self.p2)





class P2:
    global skill_num
    def __init__(self):
        self.up = None
        self.x, self.y = 400, ground_y
        self.frame = 0
        self.dir = 1
        self.idle = load_image('naruto_idle.png')
        self.run = load_image('naruto_run.png')
        self.jump = load_image('naruto_jump.png')
        self.teleport = load_image('sasuke_teleport.png')
        self.teleport_motion = load_image('teleport.png')
        self.attack1 = load_image('naruto_attack1.png')
        self.attack2 = load_image('sasuke_attack2.png')
        self.attack3 = load_image('sasuke_attack3.png')
        self.attack4 = load_image('sasuke_attack4.png')
        self.skill1_stand = load_image('sasuke_skill1_stand.png')
        self.skill1_jump = load_image('sasuke_skill1_jump.png')
        self.skill2 = load_image('sasuke_skill2.png')
        self.state_machine = StateMachine(self)
        self.state_machine.start()
        self.jump_move = False
        self.jump_state = False
        self.run_check = 0
        self.right = False
        self.left = False
        self.up_tele = False
        self.attack_num = 1
        self.wait_time = 0
        self.skill_num = 1

    def skill(self):
        if self.skill_num == 1:
            skill1 = Skill1(self.x, self.y + 10, self.dir)
            game_world.add_object(skill1, 2)
        elif self.skill_num == 2:
            skill2 = Skill2(self.x, self.y + 10, self.dir)
            game_world.add_object(skill2, 2)
        pass
    def update(self):
        self.state_machine.update()

    def handle_event(self, event):
        self.state_machine.handle_event(('INPUT', event))

    def draw(self):
        self.state_machine.draw()
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 30, self.y - 70, self.x + 30, self.y + 70
