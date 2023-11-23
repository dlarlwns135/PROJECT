from pico2d import *
import play_mode
class Map:
    def __init__(self):
        self.uchihamap = load_image('resource/uchihamap.png')
        self.cw = get_canvas_width()
        self.ch = get_canvas_height()
        self.w = self.uchihamap.w
        self.h = self.uchihamap.h
        # self.ruler_image = load_image('ruler.png')

    def update(self):

        self.window_left = clamp(0, int((play_mode.p1.x+play_mode.p2.x)//2) - self.cw // 2,
                                 self.w - self.cw - 1)
        # if abs(play_mode.p1.x - play_mode.p2.x) >= self.cw - 100:
        #     if play_mode.p1.x > play_mode.p2.x:
        #         play_mode.p1.x =
        #     # self.window_left = min(int(play_mode.p1.x)-self.cw,int(play_mode.p2.x)-self.cw)aaaaaaaaaa
        #     self.window_left = clamp(0, min(int(play_mode.p1.x), int(play_mode.p2.x)) - self.cw // 2,
        #                              max(int(play_mode.p1.x), int(play_mode.p2.x)) - self.cw // 2)
        # if play_mode.p1.x > play_mode.p2.x:
        #     if play_mode.p1.x >= self.window_left + self.cw - 50:
        #         self.window_left = int(play_mode.p1.x) - self.cw + 50
        #         if abs(play_mode.p1.x-play_mode.p2.x) > self.cw - 100:
        #             play_mode.p1.x = play_mode.p2.x + self.cw - 100
        #             play_mode.p2.x = play_mode.p1.x - self.cw + 100
        #
        #
        #
        #     # if play_mode.p2.x <= self.window_left + 50:
        #     #     play_mode.p2.x = self.window_left + 50
        # # if play_mode.p1.x <= self.window_left + 20:
        # #     self.window_left
        # if play_mode.p2.x >= self.window_left + self.cw - 20:
        #     self.window_left = int(play_mode.p2.x) - self.cw + 20
        #     if play_mode.p1.x <= self.window_left + 50:
        #         play_mode.p1.x = self.window_left + 50
        self.window_bottom = clamp(0, int((play_mode.p1.y+play_mode.p2.y)//2) - self.ch // 2,
                                   self.h - self.ch - 1)
        # self.cw = int(abs(play_mode.p1.x - play_mode.p2.x)) + 300
        # self.ch = int(abs(play_mode.p1.y - play_mode.p2.y)) + 400

    def draw(self):
        # self.uchihamap.clip_composite_draw(int(min(play_mode.p1.x,play_mode.p2.x)),
        #                                    int(min(play_mode.p1.y,play_mode.p2.y)),
        #                                    int(abs(play_mode.p1.x - play_mode.p2.x)) + 300,
        #                                    int(abs(play_mode.p1.y - play_mode.p2.y)) + 400,
        #                                    0, '', self.cw//2, self.ch//2, self.cw, self.ch
        #                                    )
        self.uchihamap.clip_draw_to_origin(self.window_left, self.window_bottom, self.cw, self.ch, 0, 0)
        # self.uchihamap.clip_draw_to_origin(self.window_left, self.window_bottom,
        #                                    int(abs(play_mode.p1.x - play_mode.p2.x)) + 300,
        #                                    int(abs(play_mode.p1.y - play_mode.p2.y)) + 400, 0, 0)

        # self.image.draw(1200, 30)