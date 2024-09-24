from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

def run_circle():
    print('CIRCLE')

    clear_canvas()
    character.draw_now(400, 30)
    delay(0.1)

def run_rectangle():
    print('RECTANGLE')
    pass

while (True):
    run_circle()
    run_rectangle()
    break #빠르게 확인하는 용도
    

close_canvas()

