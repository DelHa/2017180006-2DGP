import math

from pico2d import *
os.chdir("C:\\git_2DGP\\2017180006-2DGP\\Drills\\Drill-03\\Lecture03")
os.getcwd()
open_canvas()
grass = load_image('grass.png')
character = load_image('character.png')
x=0
y =90
while(True):
    while(x < 750):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x = x+5
        delay(0.02)

    while(y < 550):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        y = y+5
        delay(0.02)

    
    while(x > 50):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x = x-5
        delay(0.02)

    while(y > 100):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        y = y-5
        delay(0.02)

    while(x < 300):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x = x+5
        delay(0.02)
    rad=0
    rad_x = 0
    rad_y = 0
    while(rad < 170):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x + rad_x, -(y+rad_y))
        rad =rad + 2
        rad_x = math.sin((rad* 3.14/80)) * 250 + 100
        rad_y = math.cos((rad* 3.14/80)) * 250 - 400
        delay(0.02)
    



close_canvas()
