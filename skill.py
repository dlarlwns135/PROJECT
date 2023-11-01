from pico2d import *
import game_world
import p1

class Skill1:
    shuriken = None
    skill2_effect1 = None
    skill2_effect2 = None
    def __init__(self, x = 400, y = 300, velocity = 1, skill_num = 1, dir = 1):
        if Skill1.shuriken == None:
            Skill1.shuriken = load_image('shuriken1.png')
        if Skill1.skill2_effect1 == None:
            Skill1.skill2_effect1 = load_image('sasuke_skill2_effect1.png')
        if Skill1.skill2_effect2 == None:
            Skill1.skill2_effect2 = load_image('sasuke_skill2_effect2.png')
        self.x, self.y, self.velocity = x, y, velocity
        self.frame = 0
        self.skill_num = skill_num
        self.dir = dir
        self.count = 0

    def draw(self):
        if self.skill_num == 1:
            self.frame = (self.frame + 1) % 4
            self.shuriken.clip_composite_draw(self.frame * 44, 0, 44, 35, 0, '', self.x, self.y, 44, 35)
        elif self.skill_num == 2:
            if self.frame <= 7:
                self.skill2_effect2.clip_composite_draw(self.frame * 104, 0, 104, 77, 0, '',
                                                        self.x, self.y + 41, 325, 241)
            if self.frame >= 1:
                if self.dir == -1:
                    if self.frame > 7:
                        self.skill2_effect1.clip_composite_draw((self.frame - 1) * 104, 0, 104, 77, 0, 'h',
                                                                self.x + 30, self.y - 10, 325, 241)
                    else:
                        self.skill2_effect1.clip_composite_draw((self.frame - 1) * 104, 0, 104, 77, 0, 'h',
                                                                self.x + 30, self.y + 41 - 10, 325, 241)
                elif self.dir == 1:
                    if self.frame > 7:
                        self.skill2_effect1.clip_composite_draw((self.frame - 1) * 104, 0, 104, 77, 0, '',
                                                                self.x - 30, self.y - 10, 325, 241)
                    else:
                        self.skill2_effect1.clip_composite_draw((self.frame - 1) * 104, 0, 104, 77, 0, '',
                                                                self.x - 30, self.y + 41 - 10, 325, 241)
            pass

    def update(self):
        if self.skill_num == 1:
            self.x += self.velocity
            if self.x < 25 or self.x > 800 - 25:
                game_world.remove_object(self)
        elif self.skill_num == 2:
            self.count += 1
            self.frame = (self.count // 4) % 18
            if self.frame >= 7:
                self.x += self.dir * 15
            if self.frame == 17:
                game_world.remove_object(self)
            pass
