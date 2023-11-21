from pico2d import *

import game_framework
import game_world
PIXEL_PER_METER = (10.0 / 0.3) # 10 pixel 30 cm
RUN_SPEED_KMPH = 50.0 # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

class Shuriken:
    shuriken = None
    def __init__(self, x = 400, y = 300, dir = 1):
        if Shuriken.shuriken == None:
            Shuriken.shuriken = load_image('shuriken1.png')
        self.x, self.y = x, y,
        self.frame = 0
        self.dir = dir
        self.count = 0
        self.damage = 200

    def draw(self):
        self.shuriken.clip_composite_draw(int(self.frame) * 44, 0, 44, 35, 0, '', self.x, self.y, 44, 35)
        draw_rectangle(*self.get_bb())

    def update(self):
        self.frame = (self.frame + 4 * 4 * game_framework.frame_time) % 4
        self.x += self.dir * RUN_SPEED_PPS * 1.5 * game_framework.frame_time
        if self.x < 0 or self.x > 1200:
            game_world.remove_object(self)

    def get_bb(self):
        return self.x - 22, self.y - 18, self.x + 22, self.y + 18

    def handle_collision(self, group, other):
        if group == 'p1:p2_shuriken' or group == 'p2:p1_shuriken':
            # print("충돌")
            if not other.invincible:
                game_world.remove_object(self)

class Skill1:
    skill1_effect = None
    def __init__(self, x = 400, y = 300, dir = 1):
        if Skill1.skill1_effect == None:
            Skill1.skill1_effect = load_image('naruto_skill1_effect.png')
        self.x, self.y = x, y
        self.frame = 0
        self.dir = dir
        self.count = 0
        self.damage = 60

    def draw(self):
        if self.dir == 1:
            self.skill1_effect.clip_composite_draw(int(self.frame) * 193, 0, 193, 136, 0, '',
                                                   self.x, self.y+20, 543, 382)
        elif self.dir == -1:
            self.skill1_effect.clip_composite_draw(int(self.frame) * 193, 0, 193, 136, 0, 'h',
                                                   self.x, self.y+20, 543, 382)
        draw_rectangle(*self.get_bb())

    def update(self):
        self.frame = (self.frame + 10 * 2 * game_framework.frame_time) % 10
        if self.frame >= 9.5:
            game_world.remove_object(self)

    def get_bb(self):
        if self.dir == 1:
            return self.x - 200, self.y - 130, self.x + 270, self.y + 180
        elif self.dir == -1:
            return self.x - 270, self.y - 130, self.x + 200, self.y + 180

    def handle_collision(self, group, other):
        if not other.invincible:
            if group == 'p1:p2_skill1' or group == 'p2:p1_skill1':
                print("skill1 맞음")
            # game_world.remove_object(self)

class Skill2:
    skill2_effect = None
    def __init__(self, x = 400, y = 300, dir = 1):
        if Skill2.skill2_effect == None:
            Skill2.skill2_effect = load_image('naruto_skill2_effect.png')
        self.x, self.y = x, y
        self.frame = 0
        self.dir = dir
        self.count = 0
        self.damage = 60

    def draw(self):
        if self.frame >= 7:
            if self.dir == 1:
                self.skill2_effect.clip_composite_draw((int(self.frame)-7) * 159, 0, 159, 88, 0, '',
                                                       self.x, self.y , 447, 247)
            elif self.dir == -1:
                self.skill2_effect.clip_composite_draw((int(self.frame)-7) * 159, 0, 159, 88, 0, 'h',
                                                       self.x, self.y, 447, 247)
        draw_rectangle(*self.get_bb())

    def update(self):
        self.frame = (self.frame + 16 * 1 * game_framework.frame_time) % 16
        if self.frame >= 7:
            self.x += self.dir * RUN_SPEED_PPS * 1 * game_framework.frame_time
            if self.frame >= 15:
                self.frame = 12
        if self.x < 0 or self.x > 1200:
            game_world.remove_object(self)
        pass

    def get_bb(self):
        if self.dir == 1:
            return self.x - 80, self.y - 130, self.x + 220, self.y + 110
        elif self.dir == -1:
            return self.x - 220, self.y - 130, self.x + 80, self.y + 110

    def handle_collision(self, group, other):
        if not other.invincible:
            if group == 'p1:p2_skill2' or group == 'p2:p1_skill2':
                print("나선환 맞음")
            # game_world.remove_object(self)


class Attack_range:
    def __init__(self, x = 400, y = 300, dir = 1, attack_num = 0):
        self.x, self.y = x, y
        self.frame = 0
        self.dir = dir
        self.attack_x_dis = 30
        self.attack_y_dis = 0
        self.attack_num = attack_num
        self.attack_range_x = 0
        self.attack_range_y = 0
        self.damage = 0
        if self.attack_num == 1:
            self.attack_range_x = 50
            self.attack_range_y = 20
            self.attack_x_dis = 40
            self.attack_y_dis = 10
            self.damage = 10
        elif self.attack_num == 2:
            self.attack_range_x = 50
            self.attack_range_y = 40
            self.attack_x_dis = 30
            self.attack_y_dis = 20
            self.damage = 10
        elif self.attack_num == 3:
            self.attack_range_x = 50
            self.attack_range_y = 60
            self.attack_x_dis = 30
            self.attack_y_dis = 10
            self.damage = 15
        elif self.attack_num == 4:
            self.attack_range_x = 40
            self.attack_range_y = 80
            self.attack_x_dis = 0
            self.attack_y_dis = 0
            self.damage = 20
        elif self.attack_num == 'run':
            self.attack_range_x = 40
            self.attack_range_y = 50
            self.attack_x_dis = 30
            self.attack_y_dis = -20
            self.damage = 30
        elif self.attack_num == 'jump':
            self.attack_range_x = 50
            self.attack_range_y = 60
            self.attack_x_dis = 30
            self.attack_y_dis = 20
            self.damage = 30
    def update(self):
        self.frame = self.frame + 7 * 3 * game_framework.frame_time
        if self.attack_num == 1:
            if self.frame >= 4:
                self.frame = 0
                game_world.remove_object(self)
        if self.attack_num == 2:
            if self.frame >= 5:
                self.frame = 0
                game_world.remove_object(self)
        if self.attack_num == 3:
            if self.frame >= 7:
                self.frame = 0
                game_world.remove_object(self)
        if self.attack_num == 4:
            if self.frame >= 6.5:
                self.frame = 0
                game_world.remove_object(self)
        if self.attack_num == 'run':
            self.x += self.dir * RUN_SPEED_PPS * 1 * game_framework.frame_time
            if self.frame >= 6.5:
                self.frame = 0
                game_world.remove_object(self)
        if self.attack_num == 'jump':
            if self.frame >= 3:
                self.frame = 0
                game_world.remove_object(self)

    def draw(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return (self.x - self.attack_range_x + self.dir * self.attack_x_dis,
                self.y - self.attack_range_y + self.attack_y_dis,
                self.x + self.attack_range_x + self.dir * self.attack_x_dis,
                self.y + self.attack_range_y + self.attack_y_dis)

    def handle_collision(self, group, other):
        if not other.invincible:
            if group == 'p1:p2_attack' or group == 'p2:p1_attack':
                # print("충돌")
                game_world.remove_object(self)
        pass