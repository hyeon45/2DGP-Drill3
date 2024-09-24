from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

def run_circle():
    print('CIRCLE')

    r, cx, cy = 300, 800//2, 600//2

    for degree in range(0, 360, 3):
        theta = math.radians(degree)
        x = r * math.cos(theta) + cx
        y = r * math.sin(theta) + cy
    
        clear_canvas()
        character.draw_now(x, y)
        delay(0.1)

def run_rectangle():
    print('RECTANGLE')
    pass

while (True):
    run_circle()
    run_rectangle()
    break #빠르게 확인하는 용도
    

close_canvas()

