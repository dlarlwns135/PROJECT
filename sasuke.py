# 이것은 각 상태들을 객체로 구현한 것임.

from pico2d import *

import game_framework
import game_world
from skill import Skill1, Skill2, Attack_range

PIXEL_PER_METER = (10.0 / 0.3) # 10 pixel 30 cm
RUN_SPEED_KMPH = 50.0 # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

ground_y = 70
tele_dis = 220
player_num = 0

def up_down(e):
    if player_num == 1:
        return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_UP
    elif player_num == 2:
        return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_w

def up_up(e):
    if player_num == 1:
        return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_UP
    elif player_num == 2:
        return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_w

def down_down(e):
    if player_num == 1:
        return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_DOWN
    elif player_num == 2:
        return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_s

def down_up(e):
    if player_num == 1:
        return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_DOWN
    elif player_num == 2:
        return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_s

def right_down(e):
    if player_num == 1:
        return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_RIGHT
    elif player_num == 2:
        return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_d

def right_up(e):
    if player_num == 1:
        return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_RIGHT
    elif player_num == 2:
        return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_d

def left_down(e):
    if player_num == 1:
        return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_LEFT
    elif player_num == 2:
        return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_a

def left_up(e):
    if player_num == 1:
        return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_LEFT
    elif player_num == 2:
        return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_a

def space_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_SPACE

def teleport_down(e):
    if player_num == 1:
        return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_PERIOD
    elif player_num == 2:
        return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_v

def attack_down(e):
    if player_num == 1:
        return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_COMMA
    elif player_num == 2:
        return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_c

def skill_down(e):
    if player_num == 1:
        return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_SLASH
    elif player_num == 2:
        return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_b

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
    def enter(p1, e):
        pass

    @staticmethod
    def exit(p1, e):
        p1.frame = 0
        if down_down(e):
            p1.skill_num = 'special'
        if down_up(e):
            p1.skill_num = 'shuriken'
        if skill_down(e):
            p1.skill()
        if right_down(e):
            p1.right = True
        elif left_down(e):
            p1.left = True
        elif right_up(e):
            p1.right = False
        elif left_up(e):
            p1.left = False

    @staticmethod
    def do(p1):
        if p1.y > ground_y:
            p1.state_machine.handle_event(('JUMP_STATE', None))
        if p1.right and not p1.left:
            p1.state_machine.handle_event(('RUN_STATE', None))
        if not p1.right and p1.left:
            p1.state_machine.handle_event(('RUN_STATE', None))
        p1.frame = (p1.frame + 6 * 1 * game_framework.frame_time) % 6

    @staticmethod
    def draw(p1):
        if p1.dir == -1:
            p1.idle.clip_composite_draw(int(p1.frame) * 32, 0, 32, 64, 0, 'h', p1.x + 10, p1.y, 100, 200)
        elif p1.dir == 1:
            p1.idle.clip_composite_draw(int(p1.frame) * 32, 0, 32, 64, 0, '', p1.x - 10, p1.y, 100 , 200)


class Run:

    @staticmethod
    def enter(p1, e):

        p1.y -= 15

        if p1.right and not p1.left:
            p1.dir = 1
        elif p1.left and not p1.right:
            p1.dir = -1

    @staticmethod
    def exit(p1, e):
        p1.y += 15
        p1.frame = 0
        if skill_down(e):
            p1.skill()

    @staticmethod
    def do(p1):
        p1.frame = (p1.frame + 6 * 2 * game_framework.frame_time) % 6
        p1.x += p1.dir * RUN_SPEED_PPS * game_framework.frame_time

    @staticmethod
    def draw(p1):
        if p1.dir == -1:
            p1.run.clip_composite_draw(int(p1.frame) * 64, 0, 64, 32, 0, 'h', p1.x, p1.y, 200, 100)
        elif p1.dir == 1:
            p1.run.clip_composite_draw(int(p1.frame) * 64, 0, 64, 32, 0, '', p1.x, p1.y, 200, 100)


class Jump:
    @staticmethod
    def enter(p1, e):
        if right_down(e):
            p1.right = True
        if left_down(e):
            p1.left = True
        if right_up(e):
            p1.right = False
        if left_up(e):
            p1.left = False
        if up_down(e):
            p1.up_tele = True
        if up_up(e):
            p1.up_tele = False
        if down_down(e):
            p1.down_tele = True
        if down_up(e):
            p1.down_tele = False
        if p1.right and not p1.left:
            p1.dir = 1
            p1.jump_move = True
        elif p1.left and not p1.right:
            p1.dir = -1
            p1.jump_move = True

        if jump_state(e):
            p1.frame = 2

        p1.jump_state = True

    @staticmethod
    def exit(p1, e):
        if up_down(e):
            p1.frame = 0
        if skill_down(e):
            p1.frame = 0
            p1.skill()
        if teleport_down(e):
            p1.frame = 0
        pass

    @staticmethod
    def do(p1):
        if not p1.right and not p1.left:
            p1.jump_move = False
        if p1.right and p1.left:
            p1.jump_move = False
        if p1.frame >= 3:
            p1.frame = 3
        else:
            p1.frame = (p1.frame + 4 * 1.5 * game_framework.frame_time) % 4

        p1.y += 1.2 * RUN_SPEED_PPS * game_framework.frame_time * (2 - p1.frame)

        if p1.jump_move:
            p1.x += p1.dir * RUN_SPEED_PPS * game_framework.frame_time

        if p1.y <= ground_y:
            p1.y = ground_y
            p1.frame = 0
            p1.state_machine.handle_event(('JUMP_END', None))
            print("JUMP_END")
            p1.jump_state = False
            p1.jump_move = False

    @staticmethod
    def draw(p1):
        if p1.dir == -1:
            p1.jump.clip_composite_draw(int(p1.frame) * 32, 0, 32, 64, 0, 'h', p1.x, p1.y, 100, 200)
        elif p1.dir == 1:
            p1.jump.clip_composite_draw(int(p1.frame) * 32, 0, 32, 64, 0, '', p1.x, p1.y, 100, 200)

class Teleport:
    @staticmethod
    def enter(p1, e):
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
        if p1.frame >= 3:
            if p1.up_tele:
                p1.y += tele_dis
                p1.up_tele = False
            elif p1.down_tele:
                p1.y -= tele_dis
                if p1.y <= ground_y:
                    p1.y = ground_y
                p1.down_tele = False
            else:
                if p1.right and not p1.left:
                    p1.x += tele_dis
                elif p1.left and not p1.right:
                    p1.x -= tele_dis

    @staticmethod
    def do(p1):
        p1.frame = p1.frame + 4 * 5 * game_framework.frame_time
        if p1.frame >= 3:
            p1.state_machine.handle_event(('TELEPORT', None))

    @staticmethod
    def draw(p1):
        if p1.dir == -1:
            p1.teleport.clip_composite_draw(int(p1.frame) * 32, 0, 32, 64, 0, 'h', p1.x, p1.y, 100, 200)
            p1.teleport_motion.clip_composite_draw(int(p1.frame) * 72, 0, 72, 75, 0, 'h', p1.x, p1.y, 150, 250)
        elif p1.dir == 1:
            p1.teleport.clip_composite_draw(int(p1.frame) * 32, 0, 32, 64, 0, '', p1.x, p1.y, 100, 200)
            p1.teleport_motion.clip_composite_draw(int(p1.frame) * 72, 0, 72, 75, 0, '', p1.x, p1.y, 150, 250)

class Attack:
    @staticmethod
    def enter(p1, e):
        if get_time() - p1.wait_time > 0.5:
            p1.attack_num = 1
        if right_down(e):
            p1.right = True
        elif left_down(e):
            p1.left = True
        elif right_up(e):
            p1.right = False
        elif left_up(e):
            p1.left = False
        else:
            p1.attack()

    @staticmethod
    def exit(p1, e):
        pass

    @staticmethod
    def do(p1):
        p1.frame = p1.frame + 7 * 3 * game_framework.frame_time
        if p1.attack_num == 1:
            if p1.frame >= 4:
                p1.state_machine.handle_event(('STOP', None))
                p1.attack_num = 2
                p1.frame = 0
                p1.wait_time = get_time()
        if p1.attack_num == 2:
            if p1.frame >= 5:
                p1.state_machine.handle_event(('STOP', None))
                p1.attack_num = 3
                p1.frame = 0
                p1.wait_time = get_time()
        if p1.attack_num == 3:
            if p1.frame >= 7:
                p1.state_machine.handle_event(('STOP', None))
                p1.attack_num = 4
                p1.frame = 0
                p1.wait_time = get_time()
        if p1.attack_num == 4:
            if p1.frame >= 6.5:
                p1.state_machine.handle_event(('STOP', None))
                p1.attack_num = 1
                p1.frame = 0
                p1.wait_time = get_time()

    @staticmethod
    def draw(p1):
        if p1.attack_num == 1:
            if p1.dir == -1:
                p1.attack1.clip_composite_draw(int(p1.frame) * 61, 0, 61, 64, 0, 'h', p1.x-35, p1.y, 191, 200)
            elif p1.dir == 1:
                p1.attack1.clip_composite_draw(int(p1.frame) * 61, 0, 61, 64, 0, '', p1.x+35, p1.y, 191, 200)
        elif p1.attack_num == 2:
            if p1.dir == -1:
                p1.attack2.clip_composite_draw(int(p1.frame) * 64, 0, 64, 64, 0, 'h', p1.x-40, p1.y, 200, 200)
            elif p1.dir == 1:
                p1.attack2.clip_composite_draw(int(p1.frame) * 64, 0, 64, 64, 0, '', p1.x+40, p1.y, 200, 200)
        elif p1.attack_num == 3:
            if p1.dir == -1:
                    p1.attack3.clip_composite_draw(int(p1.frame) * 77, 0, 77, 64, 0, 'h', p1.x - 70, p1.y, 241, 200)
            elif p1.dir == 1:
                    p1.attack3.clip_composite_draw(int(p1.frame) * 77, 0, 77, 64, 0, '', p1.x + 70, p1.y, 241, 200)
        elif p1.attack_num == 4:
            if p1.dir == -1:
                    p1.attack4.clip_composite_draw(int(p1.frame) * 72, 0, 72, 66, 0, 'h', p1.x - 62, p1.y+3, 225, 206)
            elif p1.dir == 1:
                    p1.attack4.clip_composite_draw(int(p1.frame) * 72, 0, 72, 66, 0, '', p1.x + 62, p1.y+3, 225, 206)

class Run_Attack:
    @staticmethod
    def enter(p1, e):
        p1.frame = 0
        p1.attack_num = 'run'
        p1.attack()

    @staticmethod
    def exit(p1, e):
        p1.attack_num = 1
        p1.frame = 0
    @staticmethod
    def do(p1):
        p1.frame = p1.frame + 6 * 3 * game_framework.frame_time
        if p1.frame >= 5.9:
            p1.state_machine.handle_event(('STOP', None))
        p1.x += p1.dir * RUN_SPEED_PPS * 1 * game_framework.frame_time

    @staticmethod
    def draw(p1):
        if p1.dir == -1:
            p1.run_attack.clip_composite_draw(int(p1.frame) * 79, 0, 79, 64, 0, 'h', p1.x-35, p1.y, 247, 200)
        elif p1.dir == 1:
            p1.run_attack.clip_composite_draw(int(p1.frame) * 79, 0, 79, 64, 0, '', p1.x+35, p1.y, 247, 200)

class Jump_Attack:
    @staticmethod
    def enter(p1, e):
        p1.frame = 0
        p1.attack_num = 'jump'
        p1.attack()

    @staticmethod
    def exit(p1, e):
        p1.attack_num = 1
        p1.frame = 2

    @staticmethod
    def do(p1):
        p1.frame = p1.frame + 5 * 3.5 * game_framework.frame_time
        if p1.frame >= 4.9:
            p1.state_machine.handle_event(('STOP', None))

    @staticmethod
    def draw(p1):
        if p1.dir == -1:
            p1.jump_attack.clip_composite_draw(int(p1.frame) * 56, 0, 56, 64, 0, 'h', p1.x, p1.y, 175, 200)
        elif p1.dir == 1:
            p1.jump_attack.clip_composite_draw(int(p1.frame) * 56, 0, 56, 64, 0, '', p1.x, p1.y, 175, 200)

class Skill_motion:
    @staticmethod
    def enter(p1, e):
        if right_down(e):
            p1.right = True
        elif left_down(e):
            p1.left = True
        elif right_up(e):
            p1.right = False
        elif left_up(e):
            p1.left = False

    @staticmethod
    def exit(p1, e):
        pass

    @staticmethod
    def do(p1):
        if p1.skill_num == 'special':
            p1.frame = (p1.frame + 19 * 1.0 * game_framework.frame_time) % 19
            if p1.frame >= 8:
                p1.x += p1.dir * RUN_SPEED_PPS * 2 * game_framework.frame_time
            if p1.frame >= 18:
                p1.skill_num = 'shuriken'
                p1.frame = 0
                p1.state_machine.handle_event(('STOP', None))
        elif p1.skill_num == 'shuriken':
            p1.frame = (p1.frame + 4 * 4 * game_framework.frame_time) % 4
            if p1.frame >= 3:
                p1.skill_num = 'shuriken'
                p1.frame = 0
                p1.state_machine.handle_event(('STOP', None))
        pass

    @staticmethod
    def draw(p1):
        if p1.skill_num == 'special':
            if p1.dir == -1:
                p1.skill2.clip_composite_draw(int(p1.frame) * 104, 0, 104, 77, 0, 'h', p1.x, p1.y+41, 325, 241)
            elif p1.dir == 1:
                p1.skill2.clip_composite_draw(int(p1.frame) * 104, 0, 104, 77, 0, '', p1.x, p1.y+41, 325, 241)
        elif p1.skill_num == 'shuriken':
            if p1.jump_state:
                if p1.dir == -1:
                    p1.skill1_jump.clip_composite_draw(int(p1.frame) * 40, 0, 40, 64, 0, 'h', p1.x, p1.y, 125, 200)
                elif p1.dir == 1:
                    p1.skill1_jump.clip_composite_draw(int(p1.frame) * 40, 0, 40, 64, 0, '', p1.x, p1.y, 125, 200)
            else:
                if p1.dir == -1:
                    p1.skill1_stand.clip_composite_draw(int(p1.frame) * 40, 0, 40, 64, 0, 'h', p1.x, p1.y, 125, 200)
                elif p1.dir == 1:
                    p1.skill1_stand.clip_composite_draw(int(p1.frame) * 40, 0, 40, 64, 0, '', p1.x, p1.y, 125, 200)

class StateMachine:
    def __init__(self, p1):
        self.p1 = p1
        self.cur_state = Idle
        # if player_num == 1:
        self.transitions = {
            Idle: {right_down: Run, left_down: Run, right_up: Idle, left_up: Idle, run_state: Run,
                   up_down: Jump, jump_state: Jump, attack_down: Attack, skill_down: Skill_motion,
                   down_down: Idle, down_up: Idle},
            Run: {right_up: Idle, left_up: Idle, right_down: Idle, left_down: Idle, up_down: Jump, stop: Idle
                  , teleport_down: Teleport, attack_down: Run_Attack, skill_down: Skill_motion},
            Jump: {jump_end: Idle, jump_end_run: Run, up_down: Jump, up_up: Jump, down_down: Jump, down_up: Jump,
                   teleport_down: Teleport, skill_down: Skill_motion, attack_down: Jump_Attack,
                   right_down: Jump, left_down: Jump, right_up: Jump, left_up: Jump},
            Teleport: {right_down: Teleport, left_down: Teleport, right_up: Teleport, left_up: Teleport,
                       teleport: Idle},
            Attack: {stop: Idle, right_down: Attack, left_down: Attack, right_up: Attack, left_up: Attack},
            Run_Attack: {stop: Idle},
            Jump_Attack: {stop: Jump},
            Skill_motion: {stop: Idle, right_up: Skill_motion, left_up: Skill_motion,
                           right_down: Skill_motion, left_down: Skill_motion}
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





class SASUKE:
    global skill_num
    def __init__(self, p_num):
        self.x, self.y = 400, ground_y
        self.frame = 0
        self.dir = 1
        self.idle = load_image('sasuke_idle.png')
        self.run = load_image('sasuke_run.png')
        self.jump = load_image('sasuke_jump.png')
        self.teleport = load_image('sasuke_teleport.png')
        self.teleport_motion = load_image('teleport.png')
        self.attack1 = load_image('sasuke_attack1.png')
        self.attack2 = load_image('sasuke_attack2.png')
        self.attack3 = load_image('sasuke_attack3.png')
        self.attack4 = load_image('sasuke_attack4.png')
        self.skill1_stand = load_image('sasuke_skill1_stand.png')
        self.skill1_jump = load_image('sasuke_skill1_jump.png')
        self.skill2 = load_image('sasuke_skill2.png')
        self.run_attack = load_image('sasuke_run_attack.png')
        self.jump_attack = load_image('sasuke_jump_attack.png')
        self.state_machine = StateMachine(self)
        self.state_machine.start()
        self.jump_move = False
        self.jump_state = False
        self.right = False
        self.left = False
        self.up_tele = False
        self.down_tele = False
        self.attack_num = 1
        self.wait_time = 0
        self.skill_num = 'shuriken'
        global player_num
        player_num = p_num

    def skill(self):
        if self.skill_num == 'shuriken':
            skill1 = Skill1(self.x, self.y + 10, self.dir)
            game_world.add_object(skill1, 2)
        elif self.skill_num == 'special':
            skill2 = Skill2(self.x, self.y + 10, self.dir)
            game_world.add_object(skill2, 2)

    def attack(self):
        attack_range = Attack_range(self.x, self.y, self.dir, self.attack_num)
        game_world.add_object(attack_range, 2)
    def update(self):
        self.state_machine.update()

    def handle_event(self, event):
        self.state_machine.handle_event(('INPUT', event))
        if right_up(('INPUT', event)):
            self.right = False
        if left_up(('INPUT', event)):
            self.left = False
        if right_down(('INPUT', event)):
            self.right = True
        if left_down(('INPUT', event)):
            self.left = True

    def draw(self):
        self.state_machine.draw()
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 30, self.y - 70, self.x + 30, self.y + 70