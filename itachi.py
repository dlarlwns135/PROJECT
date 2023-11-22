# 이것은 각 상태들을 객체로 구현한 것임.

from pico2d import *

import game_framework
import game_world
from itachi_attack_range import Shuriken, Skill1, Skill2, Attack_range

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

def shuriken_down(e):
    if player_num == 1:
        return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_SLASH
    elif player_num == 2:
        return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_b

def skill1_down(e):
    if player_num == 1:
        return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_l
    elif player_num == 2:
        return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_f

def skill2_down(e):
    if player_num == 1:
        return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_SEMICOLON
    elif player_num == 2:
        return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_g

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
    def enter(p3, e):
        pass

    @staticmethod
    def exit(p3, e):
        p3.frame = 0

        if shuriken_down(e):
            p3.skill_num = 'shuriken'
            p3.skill()
        if skill1_down(e):
            p3.skill_num = 'skill1'
            # p3.skill()
            if p3.chakra >= 30:
                p3.chakra -= 30
                p3.chakra_lack = False
                # p3.skill()
            else:
                p3.chakra_lack = True
        if skill2_down(e):
            p3.skill_num = 'skill2'
            if p3.chakra >= 30:
                p3.chakra -= 30
                p3.chakra_lack = False
                p3.skill()
            else:
                p3.chakra_lack = True

        if right_down(e):
            p3.right = True
        elif left_down(e):
            p3.left = True
        elif right_up(e):
            p3.right = False
        elif left_up(e):
            p3.left = False

    @staticmethod
    def do(p3):
        if p3.win:
            p3.state_machine.cur_state = Win
        if p3.hp <= 0:
            p3.state_machine.cur_state = Lose

        if p3.y > ground_y:
            p3.state_machine.handle_event(('JUMP_STATE', None))
        if p3.right and not p3.left:
            p3.state_machine.handle_event(('RUN_STATE', None))
        if not p3.right and p3.left:
            p3.state_machine.handle_event(('RUN_STATE', None))
        p3.frame = (p3.frame + 4 * 1 * game_framework.frame_time) % 4

    @staticmethod
    def draw(p3):
        if p3.dir == -1:
            p3.idle.clip_composite_draw(int(p3.frame) * 32, 0, 32, 64, 0, 'h', p3.x, p3.y+15, 100, 200)
        elif p3.dir == 1:
            p3.idle.clip_composite_draw(int(p3.frame) * 32, 0, 32, 64, 0, '', p3.x, p3.y+15, 100 , 200)


class Run:

    @staticmethod
    def enter(p3, e):

        if p3.right and not p3.left:
            p3.dir = 1
        elif p3.left and not p3.right:
            p3.dir = -1

    @staticmethod
    def exit(p3, e):
        p3.frame = 0
        if shuriken_down(e):
            p3.skill_num = 'shuriken'
            p3.skill()

    @staticmethod
    def do(p3):
        p3.frame = (p3.frame + 6 * 2 * game_framework.frame_time) % 6
        p3.x += p3.dir * RUN_SPEED_PPS * game_framework.frame_time

    @staticmethod
    def draw(p3):
        if p3.dir == -1:
            p3.run.clip_composite_draw(int(p3.frame) * 64, 0, 64, 32, 0, 'h', p3.x, p3.y-15, 200, 100)
        elif p3.dir == 1:
            p3.run.clip_composite_draw(int(p3.frame) * 64, 0, 64, 32, 0, '', p3.x, p3.y-15, 200, 100)


class Jump:
    @staticmethod
    def enter(p3, e):
        if right_down(e):
            p3.right = True
        if left_down(e):
            p3.left = True
        if right_up(e):
            p3.right = False
        if left_up(e):
            p3.left = False
        if up_down(e):
            p3.up_tele = True
        if up_up(e):
            p3.up_tele = False
        if down_down(e):
            p3.down_tele = True
        if down_up(e):
            p3.down_tele = False
        if p3.right and not p3.left:
            p3.dir = 1
            p3.jump_move = True
        elif p3.left and not p3.right:
            p3.dir = -1
            p3.jump_move = True

        if jump_state(e):
            p3.frame = 2

        p3.jump_state = True

    @staticmethod
    def exit(p3, e):
        if up_down(e):
            p3.frame = 0
        if shuriken_down(e):
            p3.skill_num = 'shuriken'
            p3.frame = 0
            p3.skill()
        if teleport_down(e):
            p3.frame = 0
    @staticmethod
    def do(p3):
        if not p3.right and not p3.left:
            p3.jump_move = False
        if p3.right and p3.left:
            p3.jump_move = False
        if p3.frame >= 3:
            p3.frame = 3
        else:
            p3.frame = (p3.frame + 4 * 1.5 * game_framework.frame_time) % 4

        p3.y += 1.2 * RUN_SPEED_PPS * game_framework.frame_time * (2 - p3.frame)

        if p3.jump_move:
            p3.x += p3.dir * RUN_SPEED_PPS * game_framework.frame_time

        if p3.y <= ground_y:
            p3.y = ground_y
            p3.frame = 0
            p3.state_machine.handle_event(('JUMP_END', None))
            p3.jump_state = False
            p3.jump_move = False

    @staticmethod
    def draw(p3):
        if p3.dir == -1:
            p3.jump.clip_composite_draw(int(p3.frame) * 32, 0, 32, 64, 0, 'h', p3.x, p3.y, 100, 200)
        elif p3.dir == 1:
            p3.jump.clip_composite_draw(int(p3.frame) * 32, 0, 32, 64, 0, '', p3.x, p3.y, 100, 200)

class Teleport:
    @staticmethod
    def enter(p3, e):
        if right_down(e):
            p3.dir = 1
            p3.right = True
        elif left_down(e):
            p3.dir = -1
            p3.left = True
        elif right_up(e):
            p3.right = False
        elif left_up(e):
            p3.left = False

    @staticmethod
    def exit(p3, e):
        if p3.frame >= 3:
            if p3.up_tele:
                if p3.right and not p3.left:
                    p3.x += tele_dis
                elif p3.left and not p3.right:
                    p3.x -= tele_dis
                p3.y += tele_dis
                p3.up_tele = False
            elif p3.down_tele:
                if p3.right and not p3.left:
                    p3.x += tele_dis
                elif p3.left and not p3.right:
                    p3.x -= tele_dis
                p3.y -= tele_dis
                if p3.y <= ground_y:
                    p3.y = ground_y
                p3.down_tele = False
            else:
                if p3.right and not p3.left:
                    p3.x += tele_dis
                elif p3.left and not p3.right:
                    p3.x -= tele_dis

    @staticmethod
    def do(p3):
        p3.frame = p3.frame + 4 * 4 * game_framework.frame_time
        if p3.frame >= 3:
            p3.state_machine.handle_event(('TELEPORT', None))

    @staticmethod
    def draw(p3):
        if p3.dir == -1:
            p3.teleport.clip_composite_draw(int(p3.frame) * 32, 0, 32, 64, 0, 'h', p3.x, p3.y, 100, 200)
            p3.teleport_motion.clip_composite_draw(int(p3.frame) * 72, 0, 72, 75, 0, 'h', p3.x, p3.y, 150, 250)
        elif p3.dir == 1:
            p3.teleport.clip_composite_draw(int(p3.frame) * 32, 0, 32, 64, 0, '', p3.x, p3.y, 100, 200)
            p3.teleport_motion.clip_composite_draw(int(p3.frame) * 72, 0, 72, 75, 0, '', p3.x, p3.y, 150, 250)

class Attack:
    @staticmethod
    def enter(p3, e):
        if get_time() - p3.wait_time > 0.5:
            p3.attack_num = 1
        if right_down(e):
            p3.right = True
        elif left_down(e):
            p3.left = True
        elif right_up(e):
            p3.right = False
        elif left_up(e):
            p3.left = False
        else:
            p3.attack()

    @staticmethod
    def exit(p3, e):
        pass

    @staticmethod
    def do(p3):
        p3.frame = p3.frame + 7 * 3 * game_framework.frame_time
        if p3.attack_num == 1:
            if p3.frame >= 4:
                p3.state_machine.handle_event(('STOP', None))
                p3.attack_num = 2
                p3.frame = 0
                p3.wait_time = get_time()
        if p3.attack_num == 2:
            if p3.frame >= 5:
                p3.state_machine.handle_event(('STOP', None))
                p3.attack_num = 3
                p3.frame = 0
                p3.wait_time = get_time()
        if p3.attack_num == 3:
            if p3.frame >= 7:
                p3.state_machine.handle_event(('STOP', None))
                p3.attack_num = 4
                p3.frame = 0
                p3.wait_time = get_time()
        if p3.attack_num == 4:
            if p3.frame >= 6.5:
                p3.state_machine.handle_event(('STOP', None))
                p3.attack_num = 1
                p3.frame = 0
                p3.wait_time = get_time()

    @staticmethod
    def draw(p3):
        if p3.attack_num == 1:
            if p3.dir == -1:
                p3.attack1.clip_composite_draw(int(p3.frame) * 61, 0, 61, 64, 0, 'h', p3.x-35, p3.y, 191, 200)
            elif p3.dir == 1:
                p3.attack1.clip_composite_draw(int(p3.frame) * 61, 0, 61, 64, 0, '', p3.x+35, p3.y, 191, 200)
        elif p3.attack_num == 2:
            if p3.dir == -1:
                p3.attack2.clip_composite_draw(int(p3.frame) * 64, 0, 64, 64, 0, 'h', p3.x-40, p3.y, 200, 200)
            elif p3.dir == 1:
                p3.attack2.clip_composite_draw(int(p3.frame) * 64, 0, 64, 64, 0, '', p3.x+40, p3.y, 200, 200)
        elif p3.attack_num == 3:
            if p3.dir == -1:
                    p3.attack3.clip_composite_draw(int(p3.frame) * 77, 0, 77, 64, 0, 'h', p3.x - 70, p3.y, 241, 200)
            elif p3.dir == 1:
                    p3.attack3.clip_composite_draw(int(p3.frame) * 77, 0, 77, 64, 0, '', p3.x + 70, p3.y, 241, 200)
        elif p3.attack_num == 4:
            if p3.dir == -1:
                    p3.attack4.clip_composite_draw(int(p3.frame) * 72, 0, 72, 66, 0, 'h', p3.x - 62, p3.y+3, 225, 206)
            elif p3.dir == 1:
                    p3.attack4.clip_composite_draw(int(p3.frame) * 72, 0, 72, 66, 0, '', p3.x + 62, p3.y+3, 225, 206)

class Run_Attack:
    @staticmethod
    def enter(p3, e):
        p3.frame = 0
        p3.attack_num = 'run'
        p3.attack()

    @staticmethod
    def exit(p3, e):
        p3.attack_num = 1
        p3.frame = 0
    @staticmethod
    def do(p3):
        p3.frame = p3.frame + 6 * 3 * game_framework.frame_time
        if p3.frame >= 5.9:
            p3.state_machine.handle_event(('STOP', None))
        p3.x += p3.dir * RUN_SPEED_PPS * 1 * game_framework.frame_time

    @staticmethod
    def draw(p3):
        if p3.dir == -1:
            p3.run_attack.clip_composite_draw(int(p3.frame) * 79, 0, 79, 64, 0, 'h', p3.x-35, p3.y, 247, 200)
        elif p3.dir == 1:
            p3.run_attack.clip_composite_draw(int(p3.frame) * 79, 0, 79, 64, 0, '', p3.x+35, p3.y, 247, 200)

class Jump_Attack:
    @staticmethod
    def enter(p3, e):
        p3.frame = 0
        p3.attack_num = 'jump'
        p3.attack()

    @staticmethod
    def exit(p3, e):
        p3.attack_num = 1
        p3.frame = 2

    @staticmethod
    def do(p3):
        p3.frame = p3.frame + 5 * 3.5 * game_framework.frame_time
        if p3.frame >= 4.9:
            p3.state_machine.handle_event(('STOP', None))

    @staticmethod
    def draw(p3):
        if p3.dir == -1:
            p3.jump_attack.clip_composite_draw(int(p3.frame) * 56, 0, 56, 64, 0, 'h', p3.x, p3.y, 175, 200)
        elif p3.dir == 1:
            p3.jump_attack.clip_composite_draw(int(p3.frame) * 56, 0, 56, 64, 0, '', p3.x, p3.y, 175, 200)

class Skill_motion:
    @staticmethod
    def enter(p3, e):
        if right_down(e):
            p3.right = True
        elif left_down(e):
            p3.left = True
        elif right_up(e):
            p3.right = False
        elif left_up(e):
            p3.left = False

        p3.invincible = True

        if p3.chakra_lack:
            p3.invincible = False
            p3.state_machine.cur_state = Idle



    @staticmethod
    def exit(p3, e):
        p3.invincible = False
        pass

    @staticmethod
    def do(p3):
        if p3.skill_num == 'skill1':
            p3.frame = (p3.frame + 12 * 0.8 * game_framework.frame_time) % 12
            if p3.frame >= 11:
                p3.skill()
                p3.frame = 0
                p3.state_machine.handle_event(('STOP', None))
        elif p3.skill_num == 'skill2':
            p3.frame = (p3.frame + 19 * 1.0 * game_framework.frame_time) % 19
            if p3.frame >= 8:
                p3.x += p3.dir * RUN_SPEED_PPS * 2 * game_framework.frame_time
            if p3.frame >= 18:
                p3.frame = 0
                p3.state_machine.handle_event(('STOP', None))
        elif p3.skill_num == 'shuriken':
            p3.frame = (p3.frame + 4 * 4 * game_framework.frame_time) % 4
            if p3.frame >= 3:
                p3.frame = 0
                p3.state_machine.handle_event(('STOP', None))

    @staticmethod
    def draw(p3):
        if p3.skill_num == 'skill1':
            if p3.dir == -1:
                p3.skill1.clip_composite_draw(int(p3.frame) * 37, 0, 37, 64, 0, 'h', p3.x, p3.y+22, 115, 200)
            elif p3.dir == 1:
                p3.skill1.clip_composite_draw(int(p3.frame) * 37, 0, 37, 64, 0, '', p3.x, p3.y+22, 115, 200)
        elif p3.skill_num == 'skill2':
            if p3.dir == -1:
                p3.skill2.clip_composite_draw(int(p3.frame) * 104, 0, 104, 77, 0, 'h', p3.x, p3.y+41, 325, 241)
            elif p3.dir == 1:
                p3.skill2.clip_composite_draw(int(p3.frame) * 104, 0, 104, 77, 0, '', p3.x, p3.y+41, 325, 241)
        elif p3.skill_num == 'shuriken':
            if p3.jump_state:
                if p3.dir == -1:
                    p3.shuriken_jump.clip_composite_draw(int(p3.frame) * 40, 0, 40, 64, 0, 'h', p3.x, p3.y, 125, 200)
                elif p3.dir == 1:
                    p3.shuriken_jump.clip_composite_draw(int(p3.frame) * 40, 0, 40, 64, 0, '', p3.x, p3.y, 125, 200)
            else:
                if p3.dir == -1:
                    p3.shuriken_stand.clip_composite_draw(int(p3.frame) * 40, 0, 40, 64, 0, 'h', p3.x, p3.y, 125, 200)
                elif p3.dir == 1:
                    p3.shuriken_stand.clip_composite_draw(int(p3.frame) * 40, 0, 40, 64, 0, '', p3.x, p3.y, 125, 200)

class Easy_hit:
    @staticmethod
    def enter(p3, e):
        if right_down(e):
            p3.right = True
        elif left_down(e):
            p3.left = True
        elif right_up(e):
            p3.right = False
        elif left_up(e):
            p3.left = False

    @staticmethod
    def exit(p3, e):
        pass

    @staticmethod
    def do(p3):
        p3.frame = p3.frame + 2 * 5 * game_framework.frame_time
        if p3.frame >= 1.9:
            p3.frame = 0
            p3.state_machine.handle_event(('STOP', None))


    @staticmethod
    def draw(p3):
        if p3.dir == -1:
            p3.easy_hit.clip_composite_draw(int(p3.frame) * 40, 0, 40, 64, 0, 'h', p3.x, p3.y, 125, 200)
        elif p3.dir == 1:
            p3.easy_hit.clip_composite_draw(int(p3.frame) * 40, 0, 40, 64, 0, '', p3.x, p3.y, 125, 200)

class Hard_hit:
    @staticmethod
    def enter(p3, e):
        if right_down(e):
            p3.right = True
        elif left_down(e):
            p3.left = True
        elif right_up(e):
            p3.right = False
        elif left_up(e):
            p3.left = False

    @staticmethod
    def exit(p3, e):
        pass

    @staticmethod
    def do(p3):
        p3.frame = p3.frame + 4 * 2 * game_framework.frame_time
        if p3.frame >= 15:
            p3.invincible = False
            p3.frame = 0
            p3.state_machine.handle_event(('STOP', None))
        if p3.frame < 2.8:
            p3.x += -p3.dir * RUN_SPEED_PPS * 1 * game_framework.frame_time
        if p3.y > ground_y and p3.frame >= 2.8:
            p3.x += -p3.dir * RUN_SPEED_PPS * 0.7 * game_framework.frame_time
            p3.y -= RUN_SPEED_PPS * game_framework.frame_time * (15 - p3.frame) // 15
            if p3.y < ground_y:
                p3.y = ground_y


    @staticmethod
    def draw(p3):
        if p3.frame > 3:
            if p3.dir == -1:
                p3.hard_hit.clip_composite_draw(3 * 64, 0, 64, 40, 0, 'h', p3.x, p3.y - 15, 200, 125)
            elif p3.dir == 1:
                p3.hard_hit.clip_composite_draw(3 * 64, 0, 64, 40, 0, '', p3.x, p3.y - 15, 200, 125)
        else:
            if p3.dir == -1:
                p3.hard_hit.clip_composite_draw(int(p3.frame) * 64, 0, 64, 40, 0, 'h', p3.x, p3.y-15, 200, 125)
            elif p3.dir == 1:
                p3.hard_hit.clip_composite_draw(int(p3.frame) * 64, 0, 64, 40, 0, '', p3.x, p3.y-15, 200, 125)

class Win:
    @staticmethod
    def enter(p3, e):
        p3.frame = 0
        pass

    @staticmethod
    def exit(p3, e):
        pass

    @staticmethod
    def do(p3):
        p3.frame = (p3.frame + 12 * 1 * game_framework.frame_time) % 12

    @staticmethod
    def draw(p3):
        if p3.dir == 1:
            p3.win_image.clip_composite_draw(int(p3.frame) * 34, 0, 34, 64, 0, '', p3.x-10, p3.y-6, 103, 200)
        elif p3.dir == -1:
            p3.win_image.clip_composite_draw(int(p3.frame) * 34, 0, 34, 64, 0, 'h', p3.x + 10, p3.y - 6, 103, 200)

class Lose:
    @staticmethod
    def enter(p3, e):
        p3.frame = 0
        pass

    @staticmethod
    def exit(p3, e):
        pass

    @staticmethod
    def do(p3):
        if p3.frame <= 3:
            p3.frame = p3.frame + 4 * 0.5 * game_framework.frame_time

    @staticmethod
    def draw(p3):
        if p3.dir == -1:
            p3.hard_hit.clip_composite_draw(int(p3.frame) * 64, 0, 64, 40, 0, 'h', p3.x, p3.y - 15, 200, 125)
        elif p3.dir == 1:
            p3.hard_hit.clip_composite_draw(int(p3.frame) * 64, 0, 64, 40, 0, '', p3.x, p3.y - 15, 200, 125)

class StateMachine:
    def __init__(self, p3):
        self.p3 = p3
        self.cur_state = Idle
        self.transitions = {
            Idle: {right_down: Run, left_down: Run, right_up: Idle, left_up: Idle, run_state: Run,
                   up_down: Jump, jump_state: Jump, attack_down: Attack, shuriken_down: Skill_motion,
                   skill1_down: Skill_motion, skill2_down: Skill_motion},
            Run: {right_up: Idle, left_up: Idle, right_down: Idle, left_down: Idle, up_down: Jump, stop: Idle
                  , teleport_down: Teleport, attack_down: Run_Attack, shuriken_down: Skill_motion},
            Jump: {jump_end: Idle, jump_end_run: Run, up_down: Jump, up_up: Jump, down_down: Jump, down_up: Jump,
                   teleport_down: Teleport, shuriken_down: Skill_motion, attack_down: Jump_Attack,
                   right_down: Jump, left_down: Jump, right_up: Jump, left_up: Jump},
            Teleport: {right_down: Teleport, left_down: Teleport, right_up: Teleport, left_up: Teleport,
                       teleport: Idle},
            Attack: {stop: Idle, right_down: Attack, left_down: Attack, right_up: Attack, left_up: Attack},
            Run_Attack: {stop: Idle},
            Jump_Attack: {stop: Jump},
            Easy_hit: {stop: Idle}, Hard_hit: {stop: Idle},
            Skill_motion: {stop: Idle, right_up: Skill_motion, left_up: Skill_motion,
                           right_down: Skill_motion, left_down: Skill_motion},
            Win: {stop: Idle}, Lose: {stop: Idle}
        }

    def start(self):
        self.cur_state.enter(self.p3, ('NONE', 0))

    def update(self):
        self.cur_state.do(self.p3)

    def handle_event(self, e):
        for check_event, next_state in self.transitions[self.cur_state].items():
            if check_event(e):
                self.cur_state.exit(self.p3, e)
                self.cur_state = next_state
                self.cur_state.enter(self.p3, e)
                return True

        return False

    def draw(self):
        self.cur_state.draw(self.p3)


class ITACHI:
    global skill_num
    def __init__(self, p_num):
        self.x, self.y = 400, ground_y
        self.frame = 0
        self.dir = 1
        self.idle = load_image('resource/itachi_idle.png')
        self.run = load_image('resource/sasuke_run.png')
        self.jump = load_image('resource/sasuke_jump.png')
        self.teleport = load_image('resource/sasuke_teleport.png')
        self.teleport_motion = load_image('resource/teleport.png')
        self.attack1 = load_image('resource/sasuke_attack1.png')
        self.attack2 = load_image('resource/sasuke_attack2.png')
        self.attack3 = load_image('resource/sasuke_attack3.png')
        self.attack4 = load_image('resource/sasuke_attack4.png')
        self.shuriken_stand = load_image('resource/sasuke_shuriken_stand.png')
        self.shuriken_jump = load_image('resource/sasuke_shuriken_jump.png')
        self.skill1 = load_image('resource/sasuke_skill1.png')
        self.skill2 = load_image('resource/sasuke_skill2.png')
        self.run_attack = load_image('resource/sasuke_run_attack.png')
        self.jump_attack = load_image('resource/sasuke_jump_attack.png')
        self.easy_hit = load_image('resource/sasuke_easy_hit.png')
        self.hard_hit = load_image('resource/sasuke_hard_hit.png')
        self.win_image = load_image('resource/sasuke_win.png')
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
        self.invincible = False
        self.hp = 400
        self.chakra = 0
        self.chakra_lack = False
        self.win = False

    def skill(self):
        if self.skill_num == 'shuriken':
            shuriken = Shuriken(self.x, self.y + 10, self.dir)
            game_world.add_object(shuriken, 2)
            if player_num == 1:
                game_world.add_collision_pair('p2:p1_shuriken', None, shuriken)
            elif player_num == 2:
                game_world.add_collision_pair('p1:p2_shuriken', None, shuriken)
        elif self.skill_num == 'skill1':
            skill1 = Skill1(self.x, self.y, self.dir)
            game_world.add_object(skill1, 2)
            if player_num == 1:
                game_world.add_collision_pair('p2:p1_skill1', None, skill1)
            elif player_num == 2:
                game_world.add_collision_pair('p1:p2_skill1', None, skill1)
        elif self.skill_num == 'skill2':
            skill2 = Skill2(self.x, self.y, self.dir)
            game_world.add_object(skill2, 2)
            if player_num == 1:
                game_world.add_collision_pair('p2:p1_skill2', None, skill2)
            elif player_num == 2:
                game_world.add_collision_pair('p1:p2_skill2', None, skill2)

    def attack(self):
        attack_range = Attack_range(self.x, self.y, self.dir, self.attack_num)
        game_world.add_object(attack_range, 2)
        if player_num == 1:
            game_world.add_collision_pair('p2:p1_attack', None, attack_range)
        elif player_num == 2:
            game_world.add_collision_pair('p1:p2_attack', None, attack_range)
    def update(self):
        self.state_machine.update()
        if self.chakra <= 100:
            self.chakra += 8 * game_framework.frame_time
            pass

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

    def handle_collision(self, group, other):
        if not self.invincible:
            if player_num == 1:
                if group == 'p1:p2_attack':
                    self.dir = -other.dir
                    print(other.damage)
                    self.hp -= other.damage
                    print("p2한테 맞음")
                    self.frame = 0
                    self.state_machine.cur_state = Easy_hit
                if group == 'p1:p2_shuriken':
                    self.dir = -other.dir
                    print(other.damage)
                    self.hp -= other.damage
                    print("p2한테 표창 맞음")
                    self.frame = 0
                    self.state_machine.cur_state = Easy_hit
                if group == 'p1:p2_skill1':
                    self.invincible = True
                    self.dir = -other.dir
                    print(other.damage)
                    self.hp -= other.damage
                    print("p2한테 skill1 맞음")
                    self.frame = 0
                    self.state_machine.cur_state = Hard_hit
                if group == 'p1:p2_skill2':
                    self.invincible = True
                    self.dir = -other.dir
                    print(other.damage)
                    self.hp -= other.damage
                    print("p2한테 special 맞음")
                    self.frame = 0
                    self.state_machine.cur_state = Hard_hit
            elif player_num == 2:
                if group == 'p2:p1_attack':
                    self.dir = -other.dir
                    print(other.damage)
                    self.hp -= other.damage
                    print("p1한테 맞음")
                    self.frame = 0
                    self.state_machine.cur_state = Easy_hit
                if group == 'p2:p1_shuriken':
                    self.dir = -other.dir
                    print(other.damage)
                    self.hp -= other.damage
                    print("p1한테 표창 맞음")
                    self.frame = 0
                    self.state_machine.cur_state = Easy_hit
                if group == 'p2:p1_skill1':
                    self.invincible = True
                    self.dir = -other.dir
                    print(other.damage)
                    self.hp -= other.damage
                    print("p2한테 skill1 맞음")
                    self.frame = 0
                    self.state_machine.cur_state = Hard_hit
                if group == 'p2:p1_skill2':
                    self.invincible = True
                    self.dir = -other.dir
                    print(other.damage)
                    self.hp -= other.damage
                    print("p1한테 special 맞음")
                    self.frame = 0
                    self.state_machine.cur_state = Hard_hit