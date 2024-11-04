from pico2d import *

import game_world
from grass import Grass
from boy import Boy


# Game object class here


def handle_events():
    global running

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        else:
            boy.handle_event(event)


def reset_world():
    global running
    global boy

    running = True

    boy = Boy() # 영속 객체
    game_world.add_object(boy, 1) # 포그라운드 깊이에 그린다 (앞)

    grass = Grass(400, 30)  # 영속 객체, 월드가 존재하는 한 계속 살아있는 객체
    game_world.add_object(grass, 0 ) # 백그라운드 깊이에 그린다 (뒤)

    grass2 = Grass(400, 10)  # 영속 객체, 월드가 존재하는 한 계속 살아있는 객체
    game_world.add_object(grass2, 2)  # 소년보다 앞 깊이에 그린다.



def update_world():
    game_world.update()
    pass


def render_world():
    clear_canvas()
    game_world.render()
    update_canvas()


open_canvas()
reset_world()
# game loop
while running:
    handle_events()
    update_world()
    render_world()
    delay(0.01)
# finalization code
close_canvas()
