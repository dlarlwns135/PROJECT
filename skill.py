from pico2d import *
import game_world

class Skill:
    image = None

    def __init__(self, x = 400, y = 300, velocity = 1):
        if Skill.image == None:
            Skill.image = load_image('shuriken1.png')
        self.x, self.y, self.velocity = x, y, velocity
        self.frame = 0

    def draw(self):
        # self.image.draw(self.x, self.y)
        self.frame = (self.frame + 1) % 4
        self.image.clip_composite_draw(self.frame * 44, 0, 44, 35, 0, '', self.x, self.y, 44, 35)

    def update(self):
        self.x += self.velocity

        if self.x < 25 or self.x > 800 - 25:
            game_world.remove_object(self)
