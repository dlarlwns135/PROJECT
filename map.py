from pico2d import *

class Map:
    def __init__(self):
        self.uchihamap = load_image('uchihamap.png')
        # self.ruler_image = load_image('ruler.png')

    def update(self):
        pass

    def draw(self):
        self.uchihamap.clip_composite_draw(0, 0, 506, 318, 0, 'h', 400, 300, 800, 600)
        # self.image.draw(1200, 30)