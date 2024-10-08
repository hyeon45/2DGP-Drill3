from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

def draw_boy(x, y):
    clear_canvas()
    grass.draw(400, 30)
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

    for x in range(800, 0, -10):
        draw_boy(x, 550)

def run_right():
    print('RIGHT')

    for y in range(80, 550, 10):
        draw_boy(750, y)

def run_bottom():
    print('BOTTOM')
    
    for x in range(0, 800, 10):
        draw_boy(x, 80)

def run_left():
    print('LEFT')
    
    for y in range(550, 80, -10):
        draw_boy(0, y)

def run_rectangle():
    print('RECTANGLE')

    run_top()
    run_left()
    run_bottom()
    run_right()
    
def run_tri_draw(x1, y1, x2, y2):
    print('TRIANGLE_SIDE_DROW')

    steps = 50
    dx = (x2 - x1) / steps
    dy = (y2 - y1) / steps

    for i in range(steps):
        x = x1 + dx * i
        y = y1 + dy * i
        
        draw_boy(x, y)

def run_side():
    print('SIDE')
    
    x1, x2, x3 = 50, 800, 800//2
    y1, y2, y3 = 80, 80, 600

    run_tri_draw(x1, y1, x2, y2)
    run_tri_draw(x2, y2, x3, y3)
    run_tri_draw(x3, y3, x1, y1)

def run_triangle():
    print('TRIANGLE')

    run_side()

while (True):
    run_circle()
    run_rectangle()
    run_triangle()
    

close_canvas()

