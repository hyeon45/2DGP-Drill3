from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

def draw_boy(x, y):
    clear_canvas()
    character.draw_now(x, y)
    delay(0.1)

def run_circle():
    print('CIRCLE')

    r, cx, cy = 300, 800//2, 600//2

    for degree in range(0, 360, 3):
        theta = math.radians(degree)
        x = r * math.cos(theta) + cx
        y = r * math.sin(theta) + cy

        draw_boy(x, y)
    
def run_top():
    print('TOP')

    for x in range(0, 800, 10):
        draw_boy(x, 550)

def run_right():
    print('RIGHT')

    for y in range(550, 0, -10):
        draw_boy(790, y)

def run_bottom():
    print('BOTTOM')
    
    for x in range(800, 0, -10):
        draw_boy(x, 0)

def run_left():
    print('LEFT')
    
    for y in range(0, 550, 10):
        draw_boy(0, y)

def run_rectangle():
    print('RECTANGLE')

    run_top()
    run_right()
    run_bottom()
    run_left()
    
def run_tri_bottom(x1, y1, x2, y2):
    print('TRIANGLE_SIDE_BOTTOM')

    steps = 30
    dx = (x2 - x1) / steps
    dy = (y2 - y1) / steps

    for i in range(steps):
        x = x1 + dx * i
        y = y1 + dy * i
        
        draw_boy(x, y)

def run_tri_right(x2, y2, x3, y3):
    print('TRIANGLE_SIDE_RIGHT')

    steps = 30
    dx = (x3 - x2) / steps
    dy = (y3 - y2) / steps

    for i in range(steps):
        x = x2 + dx * i
        y = y2 + dy * i
        
        draw_boy(x, y)

def run_tri_left(x3, y3, x1, y1):
    print('TRIANGLE_SIDE_LEFT')

    steps = 30
    dx = (x1 - x3) / steps
    dy = (y1 - y3) / steps

    for i in range(steps):
        x = x3 + dx * i
        y = y3 + dy * i
        
        draw_boy(x, y)

def run_side():
    print('SIDE')
    
    x1, x2, x3 = 0, 800, 800//2
    y1, y2, y3 = 0, 0, 600

    run_tri_bottom(x1, y1, x2, y2)
    run_tri_right(x2, y2, x3, y3)
    run_tri_left(x3, y3, x1, y1)

def run_triangle():
    print('TRIANGLE')

    run_side()

while (True):
    #run_circle()
    #run_rectangle()
    run_triangle()
    break #빠르게 확인하는 용도
    

close_canvas()

