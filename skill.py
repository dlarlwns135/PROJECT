from pico2d import *

import game_framework
import game_world
PIXEL_PER_METER = (10.0 / 0.3) # 10 pixel 30 cm
RUN_SPEED_KMPH = 50.0 # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

class Skill1:
    shuriken = None
    def __init__(self, x = 400, y = 300, dir = 1):
        if Skill1.shuriken == None:
            Skill1.shuriken = load_image('shuriken1.png')
        self.x, self.y = x, y,
        self.frame = 0
        self.dir = dir
        self.count = 0

    def draw(self):
        self.shuriken.clip_composite_draw(int(self.frame) * 44, 0, 44, 35, 0, '', self.x, self.y, 44, 35)

    def update(self):
        self.frame = (self.frame + 4 * 4 * game_framework.frame_time) % 4
        self.x += self.dir * RUN_SPEED_PPS * 3 * game_framework.frame_time
        if self.x < 0 or self.x > 1200:
            game_world.remove_object(self)

class Skill2:
    skill2_effect1 = None
    skill2_effect2 = None
    def __init__(self, x = 400, y = 300, dir = 1):
        if Skill2.skill2_effect1 == None:
            Skill2.skill2_effect1 = load_image('sasuke_skill2_effect1.png')
        if Skill2.skill2_effect2 == None:
            Skill2.skill2_effect2 = load_image('sasuke_skill2_effect2.png')
        self.x, self.y = x, y
        self.frame = 0
        self.dir = dir
        self.count = 0

    def draw(self):
        if self.frame <= 7:
            self.skill2_effect2.clip_composite_draw(int(self.frame) * 104, 0, 104, 77, 0, '',
                                                    self.x, self.y + 41, 325, 241)
            # p1.skill1_stand.clip_composite_draw(int(p1.frame) * 40, 0, 40, 64, 0, 'h', p1.x, p1.y, 125, 200)
        if self.frame >= 1:
            if self.dir == -1:
                if self.frame > 7:
                    self.skill2_effect1.clip_composite_draw((int(self.frame) - 1) * 104, 0, 104, 77, 0, 'h',
                                                            self.x + 30, self.y - 10, 325, 241)
                else:
                    self.skill2_effect1.clip_composite_draw((int(self.frame) - 1) * 104, 0, 104, 77, 0, 'h',
                                                            self.x + 30, self.y + 41 - 10, 325, 241)
            elif self.dir == 1:
                if self.frame > 7:
                    self.skill2_effect1.clip_composite_draw((int(self.frame) - 1) * 104, 0, 104, 77, 0, '',
                                                            self.x - 30, self.y - 10, 325, 241)
                else:
                    self.skill2_effect1.clip_composite_draw((int(self.frame) - 1) * 104, 0, 104, 77, 0, '',
                                                            self.x - 30, self.y + 41 - 10, 325, 241)
            pass

    def update(self):
        self.count += 1
        self.frame = (self.frame + 18 * 1 * game_framework.frame_time) % 18
        if self.frame >= 7:
            self.x += self.dir * RUN_SPEED_PPS * 2 * game_framework.frame_time
        if self.frame >= 17:
            game_world.remove_object(self)
        pass