import pico2d

import game_framework

import title_mode as start_mode

pico2d.open_canvas(sync = True)
game_framework.run(start_mode)
pico2d.close_canvas()